# Boolean Logic

## 1. Pengertian Aljabar Boolean

Aljabar Boolean adalah aljabar atas dua nilai, TRUE (1) dan FALSE (0), dengan operasi AND, OR, dan NOT.
Setiap ekspresi Boolean selalu menghasilkan salah satu dari dua nilai tersebut, sehingga cocok untuk
keputusan ya/tidak dalam sistem otomatis. Dalam proyek ini setiap kondisi sistem dimodelkan sebagai variabel bool.

Notasi yang dipakai: `A AND B`, `A OR B`, `NOT A`, `A XOR B`, `A NAND B`, `A NOR B`; 1 = TRUE, 0 = FALSE.

## 2. Variabel Boolean Proyek

Lihat tabel lengkap di `SRS.md` bagian 2. Ringkas: `security_mode`, `door_open`, `door_open_redundant`,
`motion_detected`, `motion_sensor_online`, `occupied`, `dark`, `energy_saving_mode`, serta keluaran
`alarm_active`, `lamp_on`, `nonessential_allowed`, dan tiga Boolean hasil konversi numerik
(`duration_limit_reached`, `frequency_limit_reached`, `inactivity_exceeded`).

## 3. Enam Operator dan Tabel Kebenaran

| A | B | AND | OR | XOR | NAND | NOR |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 | 1 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 | 0 | 0 |

| A | NOT A |
|:-:|:-:|
| 0 | 1 |
| 1 | 0 |

Definisi turunan: `A XOR B = (A AND NOT B) OR (NOT A AND B)`, `A NAND B = NOT (A AND B)`, `A NOR B = NOT (A OR B)`.

## 4. Pemetaan Operator ke Python (`boolean_operations.py`)

| Operator | Fungsi | Ekspresi Python |
|---|---|---|
| AND | `boolean_and(a, b)` | `bool(a and b)` |
| OR | `boolean_or(a, b)` | `bool(a or b)` |
| NOT | `boolean_not(a)` | `not a` |
| XOR | `boolean_xor(a, b)` | `bool(a) != bool(b)` |
| NAND | `boolean_nand(a, b)` | `not (a and b)` |
| NOR | `boolean_nor(a, b)` | `not (a or b)` |

## 5. Penerapan Operator dalam Proyek

| Operator | Penerapan nyata di kode |
|---|---|
| AND | `alarm_active` (security.py), `lamp_on` (lighting.py), `nonessential_allowed` (energy_manager.py) |
| OR | `door_open OR motion_detected` (security.py); gabungan tiga batas penggunaan (energy_manager.py) |
| NOT | `NOT energy_saving_mode` (energy_manager.py); `NOT door_mismatch` (sensors.py) |
| XOR | `door_mismatch`: dua sensor pintu redundan memberi hasil berbeda (sensors.py). Hanya penanda untuk diperiksa; tidak menyimpulkan sensor mana yang rusak. |
| NAND | `diagnostics_incomplete`: TRUE bila tidak semua kondisi diagnostik terpenuhi (sensors.py) |
| NOR | `no_activity`: pintu tertutup dan tidak ada gerakan (sensors.py) |

NAND dan NOR sengaja hanya dipakai pada diagnostik sensor, tidak dipaksakan ke modul lain.

## 6. Rumus per Modul

| Modul | Rumus |
|---|---|
| Security | `alarm_active = security_mode AND (door_open OR motion_detected)` |
| Lighting (AUTO) | `lamp_on = occupied AND dark` |
| Lighting (ON/OFF) | ON → `lamp_on = TRUE`; OFF → `lamp_on = FALSE` (override mengalahkan rumus AUTO) |
| Strategy 1 | `nonessential_allowed = occupied AND NOT energy_saving_mode` |
| Strategy 2 | `usage_blocked = duration_limit_reached OR frequency_limit_reached OR inactivity_exceeded` |
| Keputusan Non-essential | `boleh_ON = nonessential_allowed AND NOT usage_blocked` |
| Diagnostik | `door_mismatch = door_open XOR door_open_redundant`; `no_activity = door_open NOR motion_detected`; `diagnostics_incomplete = (NOT door_mismatch) NAND motion_sensor_online` |

AUTO, ON, dan OFF adalah **tiga keadaan kontrol** (enumerasi `LightingMode`), bukan nilai Boolean. Boolean hanya
dipakai pada keputusan otomatis di dalam mode AUTO.

Konversi numerik → Boolean (contoh): `duration_limit_reached = (minutes_today >= max_daily_minutes)`.

Kesetaraan Strategy 1 (De Morgan): `NOT nonessential_allowed = NOT occupied OR energy_saving_mode`, yaitu non-esensial
dimatikan jika rumah tidak ditempati ATAU mode hemat aktif.

## 7. Contoh Evaluasi Skenario

**Contoh 1 (alarm).** `security_mode=1, door_open=0, motion_detected=1`
→ `door_open OR motion_detected = 0 OR 1 = 1` → `alarm_active = 1 AND 1 = 1` → alarm AKTIF.

**Contoh 2 (mode mati).** `security_mode=0, door_open=1, motion_detected=1`
→ `OR = 1` → `alarm_active = 0 AND 1 = 0` → alarm MATI walau ada aktivitas.

**Contoh 3 (lampu AUTO).** `occupied=1, dark=0` → `lamp_on = 1 AND 0 = 0` → lampu OFF.
Jika mode diganti ON → lampu ON (override), walau hasil AUTO tetap 0.

**Contoh 4 (Strategy 1).** `occupied=1, energy_saving_mode=1`
→ `NOT energy_saving_mode = 0` → `nonessential_allowed = 1 AND 0 = 0` → TV dan lampu dekorasi dimatikan; kulkas tetap ON.

**Contoh 5 (Strategy 2).** TV sudah ON 240 menit dengan batas 240 → `duration_limit_reached = TRUE`
→ `usage_blocked = TRUE` → `boleh_ON = 1 AND NOT 1 = 0` → TV dimatikan dan tidak dapat dinyalakan lagi sampai hari baru.

**Contoh 6 (XOR).** `door_open=1, door_open_redundant=0` → `door_mismatch = 1 XOR 0 = 1`
→ sistem menandai "periksa sensor" tanpa menyimpulkan sensor mana yang bermasalah.
