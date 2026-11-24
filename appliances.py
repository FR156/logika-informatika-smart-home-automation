"""Pengelolaan perangkat rumah (status, hitungan waktu simulasi).

Tujuan file:
    Menyimpan keadaan tiap perangkat (ON/OFF, menit pemakaian, jumlah aktivasi,
    menit tidak aktif) dan menyediakan operasi dasar. File ini TIDAK memutuskan
    boleh/tidaknya perangkat menyala; keputusan itu milik energy_manager.py
    (separation of concerns).
"""

from dataclasses import dataclass
from typing import List, Sequence

from config import DeviceSpec


@dataclass
class Appliance:
    """Keadaan satu perangkat.

    Attributes:
        spec: spesifikasi statis perangkat.
        is_on: perangkat sedang menyala.
        minutes_today: total menit ON pada hari simulasi ini.
        activations_today: berapa kali perangkat dinyalakan hari ini.
        idle_minutes: menit sejak aktivitas pengguna terakhir (hanya bertambah saat ON).
    """

    spec: DeviceSpec
    is_on: bool = False
    minutes_today: int = 0
    activations_today: int = 0
    idle_minutes: int = 0


class ApplianceManager:
    """Kumpulan perangkat dan operasi dasarnya."""

    def __init__(self, specs: Sequence[DeviceSpec]) -> None:
        """Membuat perangkat dari spesifikasi; semua awalnya OFF.

        Raises:
            ValueError: bila nama perangkat tidak unik.
        """
        names = [s.name.lower() for s in specs]
        if len(names) != len(set(names)):
            raise ValueError("Nama perangkat harus unik.")
        self.devices: List[Appliance] = [Appliance(spec) for spec in specs]

    def find(self, key: str) -> Appliance:
        """Mencari perangkat berdasarkan nomor urut (mulai 1) atau nama (tak peka huruf besar).

        Raises:
            ValueError: bila tidak ditemukan.
        """
        text = key.strip()
        if text.isdigit():
            index = int(text) - 1
            if 0 <= index < len(self.devices):
                return self.devices[index]
        for device in self.devices:
            if device.spec.name.lower() == text.lower():
                return device
        raise ValueError(f"Perangkat tidak ditemukan: {key!r}")

    def turn_on(self, key: str) -> bool:
        """Menyalakan perangkat (operasi mentah, tanpa cek kebijakan).

        Returns:
            True bila status berubah dari OFF ke ON. Penyalaan menambah
            activations_today dan mereset idle_minutes (dianggap aktivitas baru).
        """
        device = self.find(key)
        if device.is_on:
            return False
        device.is_on = True
        device.activations_today += 1
        device.idle_minutes = 0
        return True

    def turn_off(self, key: str) -> bool:
        """Mematikan perangkat (operasi mentah). Returns True bila status berubah."""
        device = self.find(key)
        if not device.is_on:
            return False
        device.is_on = False
        return True

    def touch(self, key: str) -> None:
        """Mencatat aktivitas pengguna pada perangkat (mereset idle_minutes)."""
        self.find(key).idle_minutes = 0

    def advance_minutes(self, minutes: int) -> None:
        """Memajukan waktu simulasi; perangkat ON menambah menit pakai dan menit tidak aktif.

        Raises:
            ValueError: bila minutes bukan bilangan bulat tidak negatif.
        """
        if isinstance(minutes, bool) or not isinstance(minutes, int) or minutes < 0:
            raise ValueError("Menit harus bilangan bulat tidak negatif.")
        for device in self.devices:
            if device.is_on:
                device.minutes_today += minutes
                device.idle_minutes += minutes

    def reset_day(self) -> None:
        """Memulai hari simulasi baru: semua penghitung harian di-nol-kan (status ON/OFF tetap)."""
        for device in self.devices:
            device.minutes_today = 0
            device.activations_today = 0
            device.idle_minutes = 0
