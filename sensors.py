"""Simulasi status sensor dan diagnostik sensor.

Tujuan file:
    Menyimpan keadaan sensor/kondisi rumah sebagai nilai Boolean yang diubah
    oleh pengguna (tanpa perangkat keras), serta menghitung tiga diagnostik
    memakai XOR, NOR, dan NAND.
"""

from dataclasses import dataclass
from typing import Optional

from boolean_operations import boolean_nand, boolean_nor, boolean_not, boolean_xor

TRUE_WORDS = {"1", "y", "yes", "ya", "on", "true", "t", "open", "detected", "dark", "gelap"}
FALSE_WORDS = {"0", "n", "no", "tidak", "off", "false", "f", "closed", "close", "none",
               "light", "terang"}


@dataclass
class SensorState:
    """Keadaan seluruh sensor dan kondisi rumah (semua bool).

    Attributes:
        security_mode: mode keamanan aktif.
        door_open: sensor pintu utama mendeteksi pintu terbuka.
        door_open_redundant: sensor pintu redundan (hanya untuk diagnostik XOR).
        motion_detected: sensor gerak mendeteksi gerakan.
        motion_sensor_online: sensor gerak merespons uji diagnostik.
        occupied: rumah/ruangan ditempati.
        dark: ruangan gelap.
        energy_saving_mode: mode hemat energi aktif.
    """

    security_mode: bool = False
    door_open: bool = False
    door_open_redundant: bool = False
    motion_detected: bool = False
    motion_sensor_online: bool = True
    occupied: bool = True
    dark: bool = False
    energy_saving_mode: bool = False


def parse_bool(text: str) -> Optional[bool]:
    """Mengubah teks pengguna menjadi bool.

    Returns:
        True/False bila dikenali, None bila tidak dikenali (pemanggil menampilkan
        pesan kesalahan). Tidak melempar exception agar CLI tidak berhenti.
    """
    word = text.strip().lower()
    if word in TRUE_WORDS:
        return True
    if word in FALSE_WORDS:
        return False
    return None


def door_mismatch(state: SensorState) -> bool:
    """XOR: TRUE bila sensor pintu utama dan redundan memberi hasil BERBEDA.

    Ketidaksesuaian hanya tanda untuk diperiksa; tidak membuktikan sensor tertentu rusak.
    """
    return boolean_xor(state.door_open, state.door_open_redundant)


def no_activity(state: SensorState) -> bool:
    """NOR: TRUE bila pintu tidak terbuka DAN tidak ada gerakan."""
    return boolean_nor(state.door_open, state.motion_detected)


def diagnostics_incomplete(state: SensorState) -> bool:
    """NAND: TRUE bila TIDAK SEMUA kondisi diagnostik terpenuhi.

    Kondisi diagnostik: kedua sensor pintu konsisten DAN sensor gerak online.
    """
    door_consistent = boolean_not(door_mismatch(state))
    return boolean_nand(door_consistent, state.motion_sensor_online)


def describe_state(state: SensorState) -> str:
    """Teks ringkas status sensor untuk ditampilkan di terminal."""
    def onoff(value: bool, yes: str, no: str) -> str:
        return yes if value else no

    return "\n".join([
        f"Mode keamanan        : {onoff(state.security_mode, 'ON', 'OFF')}",
        f"Sensor pintu utama   : {onoff(state.door_open, 'OPEN', 'CLOSED')}",
        f"Sensor pintu redundan: {onoff(state.door_open_redundant, 'OPEN', 'CLOSED')}",
        f"Sensor gerak         : {onoff(state.motion_detected, 'DETECTED', 'NOT DETECTED')}",
        f"Sensor gerak online  : {onoff(state.motion_sensor_online, 'YES', 'NO')}",
        f"Ruangan ditempati    : {onoff(state.occupied, 'YES', 'NO')}",
        f"Ruangan gelap        : {onoff(state.dark, 'YES', 'NO')}",
        f"Mode hemat energi    : {onoff(state.energy_saving_mode, 'ON', 'OFF')}",
    ])
