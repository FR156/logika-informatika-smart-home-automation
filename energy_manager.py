"""Kebijakan hemat energi dan perhitungan konsumsi.

Tujuan file:
    Menentukan apakah suatu perangkat boleh beroperasi (dengan alasan), serta
    menghitung energi (kWh). Mengimplementasikan dua strategi:

    Strategy 1 (Non-essential Shutdown):
        nonessential_allowed = occupied AND NOT energy_saving_mode
    Strategy 2 (Usage-based Restriction), semua hasil numerik dikonversi ke Boolean:
        duration_limit_reached  = minutes_today >= max_daily_minutes
        frequency_limit_reached = activations_today >= max_daily_activations
        inactivity_exceeded     = idle_minutes >= inactivity_timeout_minutes
        usage_blocked = duration OR frequency OR inactivity
    Non-essential boleh ON = nonessential_allowed AND NOT usage_blocked
    Essential tidak pernah dibatasi; Conditional mengikuti kondisinya sendiri.

    Energi: kWh = Daya (W) x Waktu (jam) / 1000
"""

from dataclasses import dataclass
from typing import List, Optional, Tuple

from appliances import Appliance, ApplianceManager
from boolean_operations import boolean_and, boolean_not, boolean_or
from config import CATEGORY_CONDITIONAL, CATEGORY_ESSENTIAL


@dataclass(frozen=True)
class Context:
    """Kondisi rumah saat keputusan dibuat (semua bool)."""

    occupied: bool
    energy_saving_mode: bool
    lamp_on: bool


@dataclass(frozen=True)
class Decision:
    """Keputusan kebijakan: allowed + alasan dalam kalimat."""

    allowed: bool
    reason: str


@dataclass
class EnergyPolicy:
    """Saklar strategi: shutdown_enabled (Strategy 1), limits_enabled (Strategy 2)."""

    shutdown_enabled: bool = True
    limits_enabled: bool = True


def nonessential_allowed(context: Context, policy: EnergyPolicy) -> bool:
    """Strategy 1: occupied AND NOT energy_saving_mode (selalu TRUE bila strategi dimatikan)."""
    if not policy.shutdown_enabled:
        return True
    return boolean_and(context.occupied, boolean_not(context.energy_saving_mode))


def condition_met(condition: Optional[str], context: Context) -> bool:
    """Memeriksa kondisi operasi perangkat Conditional ("lamp", "occupied", atau None).

    Raises:
        ValueError: kondisi tidak dikenal.
    """
    if condition is None:
        return True
    if condition == "lamp":
        return context.lamp_on
    if condition == "occupied":
        return context.occupied
    raise ValueError(f"Kondisi tidak dikenal: {condition!r}")


def usage_flags(device: Appliance, activation: bool) -> Tuple[bool, bool, bool]:
    """Mengubah data numerik pemakaian menjadi tiga Boolean (durasi, frekuensi, inaktivitas).

    Args:
        device: perangkat yang dievaluasi.
        activation: TRUE bila evaluasi untuk PERMINTAAN menyalakan, FALSE bila perangkat sedang ON.
            Frekuensi hanya memblokir permintaan aktivasi baru; inaktivitas hanya relevan saat ON.
    """
    limits = device.spec.limits
    duration = (limits.max_daily_minutes is not None
                and device.minutes_today >= limits.max_daily_minutes)
    frequency = (activation and limits.max_daily_activations is not None
                 and device.activations_today >= limits.max_daily_activations)
    inactivity = ((not activation) and limits.inactivity_timeout_minutes is not None
                  and device.idle_minutes >= limits.inactivity_timeout_minutes)
    return duration, frequency, inactivity


def evaluate_device(device: Appliance, context: Context, policy: EnergyPolicy,
                    activation: bool) -> Decision:
    """Memutuskan apakah perangkat boleh beroperasi, beserta alasannya."""
    category = device.spec.category
    if category == CATEGORY_ESSENTIAL:
        return Decision(True, "Diizinkan: perangkat esensial dikecualikan dari kebijakan hemat energi.")
    if category == CATEGORY_CONDITIONAL:
        if condition_met(device.spec.condition, context):
            return Decision(True, f"Diizinkan: kondisi '{device.spec.condition}' terpenuhi.")
        return Decision(False, f"Tidak diizinkan: kondisi '{device.spec.condition}' tidak terpenuhi.")
    if not nonessential_allowed(context, policy):
        return Decision(False, "Tidak diizinkan (Strategy 1): "
                        f"occupied={context.occupied}, energy_saving_mode={context.energy_saving_mode}.")
    if policy.limits_enabled:
        duration, frequency, inactivity = usage_flags(device, activation)
        if boolean_or(boolean_or(duration, frequency), inactivity):
            parts = []
            if duration:
                parts.append("batas durasi harian tercapai")
            if frequency:
                parts.append("batas frekuensi aktivasi tercapai")
            if inactivity:
                parts.append("inactivity timeout terlampaui")
            return Decision(False, "Tidak diizinkan (Strategy 2): " + ", ".join(parts) + ".")
    return Decision(True, "Diizinkan: lolos Strategy 1 dan Strategy 2.")


def enforce_policy(manager: ApplianceManager, context: Context, policy: EnergyPolicy) -> List[str]:
    """Mematikan perangkat ON yang tidak lagi diizinkan.

    Returns:
        Daftar pesan untuk setiap perangkat yang dimatikan (Essential tidak pernah termasuk).
    """
    messages: List[str] = []
    for device in manager.devices:
        if device.is_on:
            decision = evaluate_device(device, context, policy, activation=False)
            if not decision.allowed:
                manager.turn_off(device.spec.name)
                messages.append(f"{device.spec.name} dimatikan. {decision.reason}")
    return messages


def request_turn_on(manager: ApplianceManager, key: str, context: Context,
                    policy: EnergyPolicy) -> Decision:
    """Meminta menyalakan perangkat; hanya menyala bila kebijakan mengizinkan."""
    device = manager.find(key)
    if device.is_on:
        return Decision(True, "Perangkat sudah menyala.")
    decision = evaluate_device(device, context, policy, activation=True)
    if decision.allowed:
        manager.turn_on(device.spec.name)
    return decision


def energy_kwh(power_w: float, hours: float) -> float:
    """Energi (kWh) = Daya (W) x Waktu (jam) / 1000.

    Raises:
        ValueError: daya atau jam negatif.
    """
    if power_w < 0 or hours < 0:
        raise ValueError("Daya dan waktu tidak boleh negatif.")
    return power_w * hours / 1000.0


def device_energy_kwh(device: Appliance) -> float:
    """Energi hari simulasi satu perangkat; perangkat yang tidak pernah ON bernilai 0."""
    return energy_kwh(device.spec.power_w, device.minutes_today / 60.0)


def total_energy_kwh(manager: ApplianceManager) -> float:
    """Total energi seluruh perangkat, termasuk perangkat esensial."""
    return sum(device_energy_kwh(d) for d in manager.devices)


def compute_savings(baseline_kwh: float, scenario_kwh: float) -> Tuple[float, float]:
    """Penghematan (kWh) dan persentasenya terhadap baseline.

    Raises:
        ValueError: bila skenario memakai energi LEBIH BESAR dari baseline (indikasi logika salah),
            atau nilai negatif.
    """
    if baseline_kwh < 0 or scenario_kwh < 0:
        raise ValueError("Energi tidak boleh negatif.")
    if scenario_kwh > baseline_kwh + 1e-9:
        raise ValueError("Skenario otomatis memakai energi lebih besar dari baseline.")
    saving = baseline_kwh - scenario_kwh
    percent = 0.0 if baseline_kwh == 0 else saving / baseline_kwh * 100.0
    return saving, percent


def percent_change(baseline_kwh: float, scenario_kwh: float) -> float:
    """Persentase perubahan konsumsi: (skenario - baseline) / baseline x 100 (negatif = lebih hemat)."""
    if baseline_kwh == 0:
        return 0.0
    return (scenario_kwh - baseline_kwh) / baseline_kwh * 100.0
