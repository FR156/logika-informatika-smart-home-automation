"""Entry point CLI: navigasi menu dan integrasi seluruh modul.

Jalankan dengan:  python main.py
Semua input divalidasi; input salah menampilkan pesan dan meminta ulang.
Mengetik 0 pada sub-menu kembali ke menu sebelumnya. Hasil energi adalah SIMULASI.
"""

from typing import List, Optional

import research
from appliances import ApplianceManager
from boolean_operations import OPERATOR_NAMES, evaluate_operator, format_truth_table, operator_arity
from config import (CATEGORY_ESSENTIAL, CONFIG_PATH, AppConfig, DeviceSpec, UsageLimits,
                    default_config, load_config, save_config, validate_device_spec)
from energy_manager import (Context, EnergyPolicy, device_energy_kwh, enforce_policy,
                            evaluate_device, nonessential_allowed, request_turn_on, total_energy_kwh)
from lighting import LightingMode, evaluate_lighting, parse_lighting_mode
from security import evaluate_security
from sensors import (SensorState, describe_state, diagnostics_incomplete, door_mismatch,
                     no_activity, parse_bool)

LINE = "=" * 40
THIN = "-" * 40
FIELDS = {
    "security_mode": "Mode keamanan (ON/OFF)",
    "door_open": "Sensor pintu utama (OPEN/CLOSED)",
    "door_open_redundant": "Sensor pintu redundan (OPEN/CLOSED)",
    "motion_detected": "Sensor gerak (DETECTED/NOT DETECTED)",
    "motion_sensor_online": "Sensor gerak online (YES/NO)",
    "occupied": "Ruangan ditempati (YES/NO)",
    "dark": "Ruangan gelap (YES/NO)",
    "energy_saving_mode": "Mode hemat energi (ON/OFF)",
}
SECURITY_FIELDS = ["security_mode", "door_open", "motion_detected", "door_open_redundant"]


def title(text: str) -> None:
    """Mencetak judul bagian dengan pemisah."""
    print(f"\n{LINE}\n  {text}\n{LINE}")


def read_text(prompt: str) -> str:
    """Membaca satu baris input. Saat input berakhir (EOF/Ctrl+C), program keluar dengan rapi."""
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print("\nInput dihentikan. Sampai jumpa.")
        raise SystemExit(0)


def read_choice(prompt: str, valid: List[str]) -> str:
    """Meminta pilihan sampai salah satu nilai valid dimasukkan."""
    while True:
        value = read_text(prompt)
        if value in valid:
            return value
        print(f"Pilihan tidak valid. Pilih salah satu: {', '.join(valid)}")


def read_bool(prompt: str) -> Optional[bool]:
    """Meminta nilai bool (mis. on/off, yes/no, open/closed). Kosong = batal (None)."""
    while True:
        value = read_text(prompt + " [kosong = batal]: ")
        if value == "":
            return None
        parsed = parse_bool(value)
        if parsed is not None:
            return parsed
        print("Masukan tidak dikenali. Gunakan 1/0, on/off, yes/no, true/false, open/closed.")


def read_int(prompt: str, minimum: int = 0) -> Optional[int]:
    """Meminta bilangan bulat >= minimum. Kosong = batal (None)."""
    while True:
        value = read_text(prompt + " [kosong = batal]: ")
        if value == "":
            return None
        if value.isdigit() and int(value) >= minimum:
            return int(value)
        print(f"Masukkan bilangan bulat >= {minimum}.")


class SmartHome:
    """Keadaan aplikasi: sensor, mode lampu, perangkat, dan kebijakan energi."""

    def __init__(self, config: AppConfig) -> None:
        """Membuat keadaan awal; perangkat Essential langsung ON."""
        self.config = config
        self.state = SensorState()
        self.mode = LightingMode.AUTO
        self.manager = ApplianceManager(config.devices)
        self.policy = EnergyPolicy(config.shutdown_enabled, config.limits_enabled)
        for device in self.manager.devices:
            if device.spec.category == CATEGORY_ESSENTIAL:
                self.manager.turn_on(device.spec.name)
        self.refresh()

    def context(self) -> Context:
        """Membangun Context kebijakan dari keadaan sensor dan keputusan lampu."""
        lamp = evaluate_lighting(self.mode, self.state.occupied, self.state.dark).lamp_on
        return Context(self.state.occupied, self.state.energy_saving_mode, lamp)

    def refresh(self) -> List[str]:
        """Menyelaraskan perangkat dengan kondisi terbaru; mengembalikan pesan perubahan."""
        ctx = self.context()
        messages: List[str] = []
        for device in self.manager.devices:
            if device.spec.condition == "lamp":
                if ctx.lamp_on and not device.is_on:
                    if request_turn_on(self.manager, device.spec.name, ctx, self.policy).allowed:
                        messages.append(f"{device.spec.name} dinyalakan otomatis (lampu ON).")
                elif not ctx.lamp_on and device.is_on:
                    self.manager.turn_off(device.spec.name)
                    messages.append(f"{device.spec.name} dimatikan otomatis (lampu OFF).")
        messages += enforce_policy(self.manager, ctx, self.policy)
        return messages


def show_messages(messages: List[str]) -> None:
    """Mencetak pesan perubahan otomatis, bila ada."""
    for message in messages:
        print(f"  * {message}")


def edit_fields(home: SmartHome, keys: List[str]) -> None:
    """Sub-menu mengubah field sensor yang dipilih."""
    while True:
        print()
        for number, key in enumerate(keys, 1):
            print(f"{number}. {FIELDS[key]:<42} = {getattr(home.state, key)}")
        print("0. Kembali")
        choice = read_choice("Pilih yang diubah: ", [str(i) for i in range(len(keys) + 1)])
        if choice == "0":
            return
        key = keys[int(choice) - 1]
        value = read_bool(f"Nilai baru untuk '{FIELDS[key]}'")
        if value is not None:
            setattr(home.state, key, value)
            print(f"Diubah: {FIELDS[key]} -> {value}")
            show_messages(home.refresh())


def menu_sensors(home: SmartHome) -> None:
    """Menu 1: konfigurasi seluruh sensor dan kondisi rumah."""
    title("HOME SENSOR CONFIGURATION")
    print(describe_state(home.state))
    edit_fields(home, list(FIELDS))


def menu_security(home: SmartHome) -> None:
    """Menu 2: sistem keamanan, dengan diagnostik XOR/NOR/NAND."""
    while True:
        title("SECURITY SYSTEM")
        s = home.state
        result = evaluate_security(s.security_mode, s.door_open, s.motion_detected)
        print("Rumus: alarm_active = security_mode AND (door_open OR motion_detected)")
        print(f"security_mode={s.security_mode} door_open={s.door_open} motion_detected={s.motion_detected}")
        print(f"Aktivitas terdeteksi (OR): {result.activity_detected}")
        print(f"STATUS ALARM: {'AKTIF' if result.alarm_active else 'MATI'}")
        print(f"Alasan: {result.reason}")
        print(THIN)
        print("Diagnostik sensor:")
        print(f"  XOR  pintu utama vs redundan berbeda : {door_mismatch(s)}"
              + ("  (periksa sensor; belum tentu ada yang rusak)" if door_mismatch(s) else ""))
        print(f"  NOR  tidak ada aktivitas             : {no_activity(s)}")
        print(f"  NAND diagnostik tidak lengkap        : {diagnostics_incomplete(s)}")
        print(THIN)
        print("1. Ubah sensor / mode keamanan\n0. Kembali ke menu utama")
        if read_choice("Pilih: ", ["0", "1"]) == "0":
            return
        edit_fields(home, SECURITY_FIELDS)


def menu_lighting(home: SmartHome) -> None:
    """Menu 3: otomatisasi lampu dengan mode AUTO/ON/OFF."""
    while True:
        title("LIGHTING AUTOMATION")
        result = evaluate_lighting(home.mode, home.state.occupied, home.state.dark)
        print("Rumus AUTO: lamp_on = occupied AND dark")
        print(f"Mode kontrol: {home.mode.value} | occupied={home.state.occupied} dark={home.state.dark}")
        print(f"Keputusan otomatis (occupied AND dark): {result.auto_decision}")
        print(f"STATUS LAMPU: {'ON' if result.lamp_on else 'OFF'}")
        print(f"Alasan: {result.reason}")
        print(THIN)
        print("1. Ganti mode (AUTO/ON/OFF)\n2. Ubah occupied/dark\n0. Kembali")
        choice = read_choice("Pilih: ", ["0", "1", "2"])
        if choice == "0":
            return
        if choice == "2":
            edit_fields(home, ["occupied", "dark"])
            continue
        mode = None
        while mode is None:
            text = read_text("Mode baru (1=AUTO, 2=ON, 3=OFF) [kosong = batal]: ")
            if text == "":
                break
            mode = parse_lighting_mode(text)
            if mode is None:
                print("Mode tidak valid.")
        if mode is not None:
            print(f"Mode lampu berubah: {home.mode.value} -> {mode.value}")
            home.mode = mode
            show_messages(home.refresh())


def print_devices(home: SmartHome) -> None:
    """Mencetak tabel perangkat beserta keputusan kebijakan dan alasannya."""
    ctx = home.context()
    print(f"{'No':<3}{'Perangkat':<21}{'Kategori':<14}{'Daya':>6}  {'Status':<7}{'Menit':>6}{'Aktv':>5}{'Idle':>6}")
    print(THIN * 2)
    for number, d in enumerate(home.manager.devices, 1):
        print(f"{number:<3}{d.spec.name:<21}{d.spec.category:<14}{d.spec.power_w:>5.0f}W  "
              f"{'ON' if d.is_on else 'OFF':<7}{d.minutes_today:>6}{d.activations_today:>5}{d.idle_minutes:>6}")
        decision = evaluate_device(d, ctx, home.policy, activation=not d.is_on)
        print(f"    -> {decision.reason}")


def menu_appliances(home: SmartHome) -> None:
    """Menu 4: melihat dan mengubah status perangkat (simulasi)."""
    while True:
        title("HOME APPLIANCES (nilai daya = asumsi simulasi)")
        print_devices(home)
        print(THIN * 2)
        number = read_int(f"Nomor perangkat untuk ON/OFF (1-{len(home.manager.devices)}), 0 = kembali", 0)
        if number is None or number == 0:
            return
        if number > len(home.manager.devices):
            print("Nomor perangkat tidak ada.")
            continue
        device = home.manager.devices[number - 1]
        if device.is_on:
            if device.spec.category == CATEGORY_ESSENTIAL:
                print("Ditolak: perangkat esensial harus tetap aktif.")
            else:
                home.manager.turn_off(device.spec.name)
                print(f"{device.spec.name} dimatikan.")
        else:
            decision = request_turn_on(home.manager, device.spec.name, home.context(), home.policy)
            print(("Berhasil dinyalakan. " if decision.allowed else "Ditolak. ") + decision.reason)


def edit_limit(home: SmartHome) -> None:
    """Mengubah satu batas penggunaan perangkat dan menyimpannya ke data/config.json."""
    number = read_int(f"Nomor perangkat (1-{len(home.manager.devices)})", 1)
    if number is None or number > len(home.manager.devices):
        print("Dibatalkan atau nomor tidak ada.")
        return
    spec = home.manager.devices[number - 1].spec
    options = {"1": "max_daily_minutes", "2": "max_daily_activations", "3": "inactivity_timeout_minutes"}
    print("1. Batas durasi harian (menit)\n2. Batas frekuensi aktivasi/hari\n3. Inactivity timeout (menit)")
    field = options[read_choice("Pilih batas: ", list(options))]
    value = read_int("Nilai baru (bilangan bulat > 0)", 1)
    if value is None:
        return
    values = {"max_daily_minutes": spec.limits.max_daily_minutes,
              "max_daily_activations": spec.limits.max_daily_activations,
              "inactivity_timeout_minutes": spec.limits.inactivity_timeout_minutes}
    values[field] = value
    new_spec = DeviceSpec(spec.name, spec.category, spec.power_w, spec.condition, UsageLimits(**values))
    try:
        validate_device_spec(new_spec)
    except ValueError as error:
        print(f"Ditolak: {error}")
        return
    home.manager.devices[number - 1].spec = new_spec
    home.config.devices[number - 1] = new_spec
    save_config(home.config)
    print(f"Batas {field} untuk {spec.name} = {value} (disimpan ke {CONFIG_PATH.name}). "
          "Batas hanya diterapkan kebijakan pada perangkat Non-essential.")


def menu_energy(home: SmartHome) -> None:
    """Menu 5: kebijakan hemat energi, waktu simulasi, laporan konsumsi."""
    while True:
        title("ENERGY MANAGEMENT (SIMULASI)")
        ctx = home.context()
        print("Strategy 1: nonessential_allowed = occupied AND NOT energy_saving_mode")
        print(f"  occupied={ctx.occupied} energy_saving_mode={ctx.energy_saving_mode} -> "
              f"nonessential_allowed={nonessential_allowed(ctx, home.policy)}")
        print(f"  Strategy 1 (shutdown): {'ON' if home.policy.shutdown_enabled else 'OFF'} | "
              f"Strategy 2 (batas penggunaan): {'ON' if home.policy.limits_enabled else 'OFF'}")
        print(THIN)
        print("1. Lihat perangkat & keputusan    2. Ubah mode hemat energi")
        print("3. Saklar Strategy 1              4. Saklar Strategy 2")
        print("5. Majukan waktu simulasi (menit) 6. Laporan konsumsi hari ini")
        print("7. Ubah batas penggunaan          8. Hari baru (reset penghitung)")
        print("9. Bandingkan skenario energi     0. Kembali")
        choice = read_choice("Pilih: ", [str(i) for i in range(10)])
        if choice == "0":
            return
        if choice == "1":
            print_devices(home)
        elif choice == "2":
            value = read_bool("Mode hemat energi")
            if value is not None:
                home.state.energy_saving_mode = value
                show_messages(home.refresh())
        elif choice == "3":
            home.policy.shutdown_enabled = not home.policy.shutdown_enabled
            show_messages(home.refresh())
        elif choice == "4":
            home.policy.limits_enabled = not home.policy.limits_enabled
            show_messages(home.refresh())
        elif choice == "5":
            minutes = read_int("Berapa menit dimajukan", 0)
            if minutes is not None:
                for _ in range(minutes):
                    home.manager.advance_minutes(1)
                    show_messages(home.refresh())
                print(f"Waktu simulasi maju {minutes} menit.")
        elif choice == "6":
            for d in home.manager.devices:
                print(f"{d.spec.name:<21}{d.minutes_today:>5} menit  {device_energy_kwh(d):8.4f} kWh")
            print(f"{'TOTAL':<21}{'':>12}{total_energy_kwh(home.manager):8.4f} kWh  (simulasi)")
        elif choice == "7":
            edit_limit(home)
        elif choice == "8":
            home.manager.reset_day()
            print("Penghitung harian di-reset.")
        else:
            print(research.format_experiment_3(research.run_experiment_3(home.config)))


def menu_boolean(home: SmartHome) -> None:
    """Menu 6: demonstrasi enam operator Boolean."""
    while True:
        title("BOOLEAN OPERATIONS DEMONSTRATION")
        for number, name in enumerate(OPERATOR_NAMES, 1):
            print(f"{number}. {name}")
        print("7. Tampilkan semua tabel kebenaran\n0. Kembali")
        choice = read_choice("Pilih: ", [str(i) for i in range(8)])
        if choice == "0":
            return
        if choice == "7":
            for name in OPERATOR_NAMES:
                print(f"\n{name}\n{format_truth_table(name)}")
            continue
        name = OPERATOR_NAMES[int(choice) - 1]
        values: List[bool] = []
        for label in ["A", "B"][:operator_arity(name)]:
            value = read_bool(f"Nilai {label}")
            if value is None:
                break
            values.append(value)
        if len(values) == operator_arity(name):
            shown = ", ".join(f"{int(v)}" for v in values)
            print(f"\n{name}({shown}) = {int(evaluate_operator(name, *values))}")
            print(format_truth_table(name))


def menu_research(home: SmartHome) -> None:
    """Menu 7: menjalankan mini research dan menyimpan CSV."""
    title("MINI RESEARCH & SIMULATION REPORT")
    print(research.run_all(home.config))
    read_text("\nTekan Enter untuk kembali...")


def main() -> None:
    """Memuat konfigurasi lalu menjalankan loop menu utama."""
    try:
        config = load_config()
    except ValueError as error:
        print(f"Peringatan: {error}\nMemakai konfigurasi default.")
        config = default_config()
    home = SmartHome(config)
    actions = {"1": menu_sensors, "2": menu_security, "3": menu_lighting, "4": menu_appliances,
               "5": menu_energy, "6": menu_boolean, "7": menu_research}
    while True:
        title("SMART HOME AUTOMATION SYSTEM")
        print("1. Home Sensor Configuration\n2. Security System\n3. Lighting Automation\n"
              "4. Home Appliances\n5. Energy Management\n6. Boolean Operations Demonstration\n"
              "7. Mini Research & Simulation Report\n8. Exit")
        choice = read_choice("\nSelect menu: ", [str(i) for i in range(1, 9)])
        if choice == "8":
            print("Terima kasih.")
            return
        actions[choice](home)


if __name__ == "__main__":
    main()
