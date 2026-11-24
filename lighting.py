"""Otomatisasi lampu dan manual override.

Tujuan file:
    Menentukan status lampu dari tiga keadaan kontrol (AUTO, ON, OFF).
    Kondisi otomatis memakai Boolean:  lamp_on = occupied AND dark
    AUTO/ON/OFF adalah TIGA keadaan kontrol (bukan Boolean); Boolean dipakai
    hanya untuk keputusan otomatis di dalam mode AUTO.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional

from boolean_operations import boolean_and


class LightingMode(Enum):
    """Mode pengendalian lampu."""

    AUTO = "AUTO"
    ON = "ON"
    OFF = "OFF"


@dataclass(frozen=True)
class LightingResult:
    """Hasil evaluasi lampu.

    Attributes:
        lamp_on: keputusan akhir lampu setelah mempertimbangkan override.
        auto_decision: hasil occupied AND dark (selalu dihitung, untuk perbandingan).
        reason: penjelasan keputusan.
    """

    lamp_on: bool
    auto_decision: bool
    reason: str


def parse_lighting_mode(text: str) -> Optional[LightingMode]:
    """Mengubah teks (AUTO/ON/OFF atau 1/2/3) menjadi LightingMode; None bila tidak valid."""
    word = text.strip().upper()
    aliases = {"1": LightingMode.AUTO, "2": LightingMode.ON, "3": LightingMode.OFF}
    if word in aliases:
        return aliases[word]
    try:
        return LightingMode(word)
    except ValueError:
        return None


def evaluate_lighting(mode: LightingMode, occupied: bool, dark: bool) -> LightingResult:
    """Menentukan status lampu.

    Manual override (ON/OFF) berprioritas atas keputusan otomatis.
    """
    auto = boolean_and(occupied, dark)
    if mode is LightingMode.ON:
        return LightingResult(True, auto, "Lampu ON: mode ON memaksa lampu menyala (override manual).")
    if mode is LightingMode.OFF:
        return LightingResult(False, auto, "Lampu OFF: mode OFF memaksa lampu mati (override manual).")
    if auto:
        return LightingResult(True, auto, "Lampu ON: mode AUTO, ruangan ditempati dan gelap.")
    if not occupied and not dark:
        why = "ruangan tidak ditempati dan tidak gelap"
    elif not occupied:
        why = "ruangan tidak ditempati"
    else:
        why = "ruangan tidak gelap"
    return LightingResult(False, auto, f"Lampu OFF: mode AUTO, {why}.")
