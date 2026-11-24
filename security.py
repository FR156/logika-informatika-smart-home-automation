"""Logika sistem keamanan.

Tujuan file:
    Menghitung status alarm dari mode keamanan, sensor pintu, dan sensor gerak,
    lalu menjelaskan alasannya dalam kalimat.

Rumus: alarm_active = security_mode AND (door_open OR motion_detected)
"""

from dataclasses import dataclass

from boolean_operations import boolean_and, boolean_or


@dataclass(frozen=True)
class SecurityResult:
    """Hasil evaluasi keamanan.

    Attributes:
        alarm_active: status alarm hasil rumus.
        activity_detected: hasil (door_open OR motion_detected).
        reason: penjelasan alasan alarm aktif/tidak aktif.
    """

    alarm_active: bool
    activity_detected: bool
    reason: str


def evaluate_security(security_mode: bool, door_open: bool, motion_detected: bool) -> SecurityResult:
    """Mengevaluasi alarm.

    Langkah: (1) OR sensor -> activity_detected; (2) AND dengan security_mode ->
    alarm_active. Urutan ini menjamin mode OFF selalu mematikan alarm.

    Returns:
        SecurityResult berisi status alarm dan alasan.
    """
    activity = boolean_or(door_open, motion_detected)
    alarm = boolean_and(security_mode, activity)

    triggers = []
    if door_open:
        triggers.append("pintu terbuka")
    if motion_detected:
        triggers.append("gerakan terdeteksi")
    trigger_text = " dan ".join(triggers)

    if not security_mode:
        extra = f" (walau {trigger_text})" if activity else ""
        reason = f"Alarm MATI: mode keamanan OFF{extra}, sehingga alarm tidak boleh aktif."
    elif activity:
        reason = f"Alarm AKTIF: mode keamanan ON dan {trigger_text}."
    else:
        reason = "Alarm MATI: mode keamanan ON tetapi pintu tertutup dan tidak ada gerakan."
    return SecurityResult(alarm, activity, reason)
