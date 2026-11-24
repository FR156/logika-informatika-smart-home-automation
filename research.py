"""Mini research: tiga eksperimen dan penyimpanan CSV.

Tujuan file:
    Experiment 1: validasi enam operator Boolean terhadap referensi aritmetika 0/1.
    Experiment 2: delapan kombinasi skenario keamanan.
    Experiment 3: simulasi energi sehari (1440 menit) pada tiga skenario.

DATA ASUMSI  : daya perangkat, batas penggunaan (config.py) dan profil jam di bawah.
INPUT SIMULASI: profil hunian, gelap, dan kebiasaan pengguna per jam (konstanta di bawah).
HASIL PENGUJIAN: hanya nilai yang dihasilkan fungsi di file ini saat dijalankan.
Semua hasil energi adalah SIMULASI, bukan pengukuran listrik nyata.
"""

import csv
from dataclasses import dataclass
from itertools import product
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

from appliances import ApplianceManager
from boolean_operations import OPERATOR_NAMES, evaluate_operator, input_combinations, reference_result
from config import CATEGORY_NON_ESSENTIAL, CSV_PATH, AppConfig, default_config
from energy_manager import (Context, EnergyPolicy, compute_savings, device_energy_kwh,
                            enforce_policy, percent_change, request_turn_on, total_energy_kwh)
from lighting import LightingMode, evaluate_lighting
from security import evaluate_security

MINUTES_PER_DAY = 1440

# --- INPUT SIMULASI (asumsi profil satu hari) ---
OCCUPIED_HOURS: Set[int] = set(range(0, 8)) | set(range(18, 24))   # rumah kosong jam 08-17
DARK_HOURS: Set[int] = set(range(0, 6)) | set(range(18, 24))       # gelap jam 18-05
ECO_HOURS: Set[int] = set(range(0, 6))                              # mode hemat aktif jam 00-05
USER_WANTS_HOURS: Dict[str, Set[int]] = {                           # kebiasaan tanpa otomatisasi
    "Refrigerator": set(range(0, 24)),
    "Main Lighting": set(range(17, 24)) | set(range(0, 8)),
    "Fan": set(range(10, 24)),
    "Television": set(range(12, 24)),
    "Decorative Lighting": set(range(17, 24)) | set(range(0, 3)),
}
INTERACTION_INTERVAL_MINUTES: Dict[str, int] = {"Television": 30}   # pengguna menyentuh TV tiap 30 menit

# Ekspektasi manual untuk Experiment 2: (security_mode, door_open, motion_detected) -> alarm.
EXPECTED_ALARM: Dict[Tuple[bool, bool, bool], bool] = {
    (False, False, False): False, (False, False, True): False,
    (False, True, False): False, (False, True, True): False,
    (True, False, False): False, (True, False, True): True,
    (True, True, False): True, (True, True, True): True,
}


@dataclass(frozen=True)
class Scenario:
    """Pengaturan satu skenario energi (automation, shutdown, limits, saving)."""

    name: str
    automation: bool
    shutdown: bool
    limits: bool
    saving: bool


SCENARIOS: Tuple[Scenario, ...] = (
    Scenario("A_tanpa_otomatisasi", False, False, False, False),
    Scenario("B_otomatisasi", True, True, False, False),
    Scenario("C_otomatisasi_hemat_dan_batas", True, True, True, True),
)


@dataclass(frozen=True)
class ScenarioResult:
    """Hasil simulasi satu skenario: baris per perangkat (nama, menit ON, kWh) dan total kWh."""

    scenario: Scenario
    rows: Tuple[Tuple[str, int, float], ...]
    total_kwh: float


def run_experiment_1() -> List[Tuple[str, int, int, float]]:
    """Validasi Boolean. Returns daftar (operator, total, benar, akurasi%)."""
    results = []
    for name in OPERATOR_NAMES:
        total = correct = 0
        for inputs in input_combinations(name):
            total += 1
            if evaluate_operator(name, *inputs) == reference_result(name, inputs):
                correct += 1
        results.append((name, total, correct, correct / total * 100.0))
    return results


def run_experiment_2() -> List[Tuple[bool, bool, bool, bool, bool]]:
    """Uji 8 kombinasi keamanan. Returns (mode, door, motion, ekspektasi, aktual)."""
    rows = []
    for mode, door, motion in product([False, True], repeat=3):
        actual = evaluate_security(mode, door, motion).alarm_active
        rows.append((mode, door, motion, EXPECTED_ALARM[(mode, door, motion)], actual))
    return rows


def simulate_day(scenario: Scenario, config: Optional[AppConfig] = None) -> ScenarioResult:
    """Mensimulasikan satu hari menit demi menit memakai logika sistem yang sebenarnya.

    Skenario A: perangkat ON mengikuti kebiasaan pengguna tanpa kebijakan.
    Skenario B/C: permintaan penyalaan melewati request_turn_on dan enforce_policy.
    Permintaan Non-essential hanya dibuat di awal jam (pengguna menekan tombol).
    """
    cfg = config or default_config()
    manager = ApplianceManager(cfg.devices)
    policy = EnergyPolicy(scenario.shutdown, scenario.limits)
    for minute in range(MINUTES_PER_DAY):
        hour = minute // 60
        occupied = hour in OCCUPIED_HOURS
        lamp_on = evaluate_lighting(LightingMode.AUTO, occupied, hour in DARK_HOURS).lamp_on
        context = Context(occupied, scenario.saving and hour in ECO_HOURS, lamp_on)
        for device in manager.devices:
            name = device.spec.name
            wants = hour in USER_WANTS_HOURS.get(name, set())
            if not scenario.automation:
                if wants:
                    manager.turn_on(name)
                else:
                    manager.turn_off(name)
            elif wants and not device.is_on:
                if device.spec.category != CATEGORY_NON_ESSENTIAL or minute % 60 == 0:
                    request_turn_on(manager, name, context, policy)
            elif not wants and device.is_on:
                manager.turn_off(name)
            elif device.is_on:
                interval = INTERACTION_INTERVAL_MINUTES.get(name)
                if interval and minute % interval == 0:
                    manager.touch(name)
        if scenario.automation:
            enforce_policy(manager, context, policy)
        manager.advance_minutes(1)
    rows = tuple((d.spec.name, d.minutes_today, device_energy_kwh(d)) for d in manager.devices)
    return ScenarioResult(scenario, rows, total_energy_kwh(manager))


def run_experiment_3(config: Optional[AppConfig] = None) -> List[ScenarioResult]:
    """Menjalankan tiga skenario energi dan mengembalikan hasilnya."""
    return [simulate_day(s, config) for s in SCENARIOS]


def format_experiment_1(results: List[Tuple[str, int, int, float]]) -> str:
    """Teks tabel hasil Experiment 1 termasuk akurasi keseluruhan."""
    lines = ["Operator | Total | Benar | Salah | Akurasi", "-" * 44]
    for name, total, correct, accuracy in results:
        lines.append(f"{name:<8} | {total:>5} | {correct:>5} | {total - correct:>5} | {accuracy:6.1f}%")
    all_total = sum(r[1] for r in results)
    all_correct = sum(r[2] for r in results)
    lines.append(f"TOTAL    | {all_total:>5} | {all_correct:>5} | {all_total - all_correct:>5} | "
                 f"{all_correct / all_total * 100:6.1f}%")
    return "\n".join(lines)


def format_experiment_2(rows: List[Tuple[bool, bool, bool, bool, bool]]) -> str:
    """Teks tabel hasil Experiment 2 (ekspektasi vs aktual)."""
    def t(v: bool) -> str:
        return "1" if v else "0"
    lines = ["Mode Door Motion | Ekspektasi Aktual Status", "-" * 46]
    for mode, door, motion, expected, actual in rows:
        status = "PASS" if expected == actual else "FAIL"
        lines.append(f"  {t(mode)}    {t(door)}     {t(motion)}   |     {t(expected)}        {t(actual)}    {status}")
    passed = sum(1 for r in rows if r[3] == r[4])
    lines.append(f"Lulus {passed}/{len(rows)} skenario")
    return "\n".join(lines)


def format_experiment_3(results: List[ScenarioResult]) -> str:
    """Teks hasil Experiment 3 (SIMULASI, bukan pengukuran nyata)."""
    baseline = results[0].total_kwh
    lines = ["[SIMULASI - bukan pengukuran listrik nyata]"]
    for result in results:
        lines.append(f"\nSkenario {result.scenario.name}")
        for name, minutes, kwh in result.rows:
            lines.append(f"  {name:<20} {minutes:>5} menit ({minutes / 60:5.2f} jam)  {kwh:7.3f} kWh")
        lines.append(f"  {'TOTAL':<20} {'':>25}{result.total_kwh:7.3f} kWh")
        if result is not results[0]:
            saving, pct = compute_savings(baseline, result.total_kwh)
            lines.append(f"  Penghematan vs A: {saving:.3f} kWh ({pct:.2f}%), "
                         f"perubahan konsumsi {percent_change(baseline, result.total_kwh):+.2f}%")
    return "\n".join(lines)


def build_csv_rows(exp1, exp2, exp3: List[ScenarioResult]) -> List[List[str]]:
    """Menyusun baris CSV format panjang: experiment, case, item, metric, value, unit, data_type."""
    rows: List[List[str]] = []
    for name, total, correct, accuracy in exp1:
        rows += [["1_boolean_validation", name, "all_inputs", "total_tests", str(total), "count", "hasil_pengujian"],
                 ["1_boolean_validation", name, "all_inputs", "correct", str(correct), "count", "hasil_pengujian"],
                 ["1_boolean_validation", name, "all_inputs", "accuracy", f"{accuracy:.1f}", "percent", "hasil_pengujian"]]
    for mode, door, motion, expected, actual in exp2:
        case = f"mode={int(mode)};door={int(door)};motion={int(motion)}"
        rows += [["2_security_scenarios", case, "alarm", "expected", str(int(expected)), "bool", "asumsi_ekspektasi"],
                 ["2_security_scenarios", case, "alarm", "actual", str(int(actual)), "bool", "hasil_pengujian"]]
    baseline = exp3[0].total_kwh
    for result in exp3:
        for name, minutes, kwh in result.rows:
            rows += [["3_energy_simulation", result.scenario.name, name, "on_minutes", str(minutes), "minute", "hasil_simulasi"],
                     ["3_energy_simulation", result.scenario.name, name, "energy", f"{kwh:.4f}", "kWh", "hasil_simulasi"]]
        rows.append(["3_energy_simulation", result.scenario.name, "TOTAL", "energy", f"{result.total_kwh:.4f}", "kWh", "hasil_simulasi"])
        saving, pct = compute_savings(baseline, result.total_kwh)
        rows += [["3_energy_simulation", result.scenario.name, "TOTAL", "saving_vs_A", f"{saving:.4f}", "kWh", "hasil_simulasi"],
                 ["3_energy_simulation", result.scenario.name, "TOTAL", "saving_percent", f"{pct:.2f}", "percent", "hasil_simulasi"]]
    for spec in default_config().devices:
        rows.append(["3_energy_simulation", "assumption", spec.name, "power", f"{spec.power_w:g}", "W", "asumsi"])
    return rows


def save_results_csv(exp1, exp2, exp3, path: Path = CSV_PATH) -> Path:
    """Menyimpan seluruh hasil eksperimen ke CSV dan mengembalikan path-nya."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["experiment", "case", "item", "metric", "value", "unit", "data_type"])
        writer.writerows(build_csv_rows(exp1, exp2, exp3))
    return path


def run_all(config: Optional[AppConfig] = None, csv_path: Path = CSV_PATH) -> str:
    """Menjalankan ketiga eksperimen, menyimpan CSV, dan mengembalikan laporan teks."""
    exp1, exp2, exp3 = run_experiment_1(), run_experiment_2(), run_experiment_3(config)
    saved = save_results_csv(exp1, exp2, exp3, csv_path)
    return "\n".join(["=== EXPERIMENT 1: Boolean Logic Validation ===", format_experiment_1(exp1),
                      "", "=== EXPERIMENT 2: Security Scenario Testing ===", format_experiment_2(exp2),
                      "", "=== EXPERIMENT 3: Energy Consumption Simulation ===", format_experiment_3(exp3),
                      "", f"Hasil disimpan ke: {saved}"])
