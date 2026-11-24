"""Konfigurasi sistem: kategori, daftar perangkat, daya, dan batas penggunaan.

Tujuan file:
    Memusatkan semua angka asumsi simulasi supaya mudah diubah tanpa menyentuh
    logika. Nilai default dapat ditimpa oleh data/config.json. Semua daya dan
    batas di sini adalah ASUMSI simulasi, bukan spesifikasi perangkat nyata.
"""

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional

BASE_DIR: Path = Path(__file__).resolve().parent
CONFIG_PATH: Path = BASE_DIR / "data" / "config.json"
CSV_PATH: Path = BASE_DIR / "data" / "research_results.csv"

CATEGORY_ESSENTIAL = "Essential"
CATEGORY_CONDITIONAL = "Conditional"
CATEGORY_NON_ESSENTIAL = "Non-essential"
VALID_CATEGORIES = (CATEGORY_ESSENTIAL, CATEGORY_CONDITIONAL, CATEGORY_NON_ESSENTIAL)
VALID_CONDITIONS = (None, "lamp", "occupied")


@dataclass(frozen=True)
class UsageLimits:
    """Batas penggunaan satu perangkat (None = tidak dibatasi).

    Attributes:
        max_daily_minutes: batas DURASI total menit ON per hari.
        max_daily_activations: batas FREKUENSI jumlah penyalaan per hari.
        inactivity_timeout_minutes: batas menit tanpa aktivitas pengguna saat ON.
    """

    max_daily_minutes: Optional[int] = None
    max_daily_activations: Optional[int] = None
    inactivity_timeout_minutes: Optional[int] = None


@dataclass(frozen=True)
class DeviceSpec:
    """Spesifikasi statis perangkat.

    Attributes:
        name: nama unik perangkat.
        category: salah satu VALID_CATEGORIES.
        power_w: daya asumsi dalam Watt (tidak negatif).
        condition: kondisi operasi untuk Conditional ("lamp", "occupied", atau None).
        limits: batas penggunaan (hanya dipakai kebijakan untuk Non-essential).
    """

    name: str
    category: str
    power_w: float
    condition: Optional[str] = None
    limits: UsageLimits = UsageLimits()


@dataclass
class AppConfig:
    """Konfigurasi aplikasi: daftar perangkat dan saklar dua strategi hemat energi."""

    devices: List[DeviceSpec]
    shutdown_enabled: bool = True
    limits_enabled: bool = True


DEFAULT_DEVICES: List[DeviceSpec] = [
    DeviceSpec("Refrigerator", CATEGORY_ESSENTIAL, 150.0),
    DeviceSpec("Main Lighting", CATEGORY_CONDITIONAL, 12.0, condition="lamp"),
    DeviceSpec("Fan", CATEGORY_CONDITIONAL, 45.0, condition="occupied"),
    DeviceSpec("Television", CATEGORY_NON_ESSENTIAL, 80.0,
               limits=UsageLimits(240, 6, 120)),
    DeviceSpec("Decorative Lighting", CATEGORY_NON_ESSENTIAL, 20.0,
               limits=UsageLimits(240, None, 60)),
]


def default_config() -> AppConfig:
    """Mengembalikan konfigurasi default (salinan baru setiap dipanggil)."""
    return AppConfig(devices=list(DEFAULT_DEVICES))


def validate_device_spec(spec: DeviceSpec) -> None:
    """Memeriksa satu spesifikasi perangkat.

    Raises:
        ValueError: nama kosong, kategori/kondisi tidak valid, daya negatif,
            atau batas penggunaan bukan bilangan bulat positif.
    """
    if not spec.name.strip():
        raise ValueError("Nama perangkat tidak boleh kosong.")
    if spec.category not in VALID_CATEGORIES:
        raise ValueError(f"Kategori tidak valid untuk {spec.name}: {spec.category!r}")
    if spec.condition not in VALID_CONDITIONS:
        raise ValueError(f"Kondisi tidak valid untuk {spec.name}: {spec.condition!r}")
    if spec.power_w < 0:
        raise ValueError(f"Daya {spec.name} tidak boleh negatif.")
    for label, value in (("max_daily_minutes", spec.limits.max_daily_minutes),
                         ("max_daily_activations", spec.limits.max_daily_activations),
                         ("inactivity_timeout_minutes", spec.limits.inactivity_timeout_minutes)):
        if value is not None and (isinstance(value, bool) or not isinstance(value, int) or value <= 0):
            raise ValueError(f"{label} untuk {spec.name} harus bilangan bulat positif atau null.")


def validate_config(config: AppConfig) -> None:
    """Memeriksa seluruh konfigurasi (spesifikasi valid dan nama perangkat unik)."""
    names = [d.name.strip().lower() for d in config.devices]
    if len(names) != len(set(names)):
        raise ValueError("Nama perangkat harus unik.")
    for spec in config.devices:
        validate_device_spec(spec)


def config_to_dict(config: AppConfig) -> Dict[str, Any]:
    """Mengubah AppConfig menjadi dict yang dapat disimpan sebagai JSON."""
    return {
        "shutdown_enabled": config.shutdown_enabled,
        "limits_enabled": config.limits_enabled,
        "devices": [
            {
                "name": d.name, "category": d.category, "power_w": d.power_w,
                "condition": d.condition,
                "limits": {
                    "max_daily_minutes": d.limits.max_daily_minutes,
                    "max_daily_activations": d.limits.max_daily_activations,
                    "inactivity_timeout_minutes": d.limits.inactivity_timeout_minutes,
                },
            }
            for d in config.devices
        ],
    }


def config_from_dict(data: Dict[str, Any]) -> AppConfig:
    """Membangun AppConfig dari dict JSON dan memvalidasinya.

    Raises:
        ValueError: struktur atau nilai konfigurasi tidak valid.
    """
    try:
        devices = [
            DeviceSpec(
                name=str(item["name"]), category=str(item["category"]),
                power_w=float(item["power_w"]), condition=item.get("condition"),
                limits=UsageLimits(**item.get("limits", {})),
            )
            for item in data["devices"]
        ]
        config = AppConfig(devices, bool(data.get("shutdown_enabled", True)),
                           bool(data.get("limits_enabled", True)))
    except (KeyError, TypeError) as error:
        raise ValueError(f"Struktur konfigurasi tidak valid: {error}") from error
    validate_config(config)
    return config


def load_config(path: Path = CONFIG_PATH) -> AppConfig:
    """Memuat konfigurasi dari JSON; jika file belum ada, memakai default.

    Raises:
        ValueError: file ada tetapi isinya bukan JSON/konfigurasi yang valid.
    """
    if not path.exists():
        return default_config()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError(f"File konfigurasi bukan JSON valid: {error}") from error
    return config_from_dict(data)


def save_config(config: AppConfig, path: Path = CONFIG_PATH) -> None:
    """Menyimpan konfigurasi ke JSON setelah divalidasi."""
    validate_config(config)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(config_to_dict(config), indent=2), encoding="utf-8")
