# Software Requirements Specification (SRS)
## Sistem Otomatisasi Keamanan dan Hemat Energi pada Smart Home Menggunakan Aljabar Boolean

Dokumen ini dibuat pada **Phase 1 — Requirement Analysis**, sebelum kode ditulis, lalu disesuaikan dengan implementasi final.

---

## 1. Ruang Lingkup

Program CLI Python (Standard Library only) yang mensimulasikan:
1. Sistem keamanan (sensor pintu + sensor gerak).
2. Otomatisasi lampu (AUTO / ON / OFF).
3. Pengelolaan perangkat rumah berkategori (Essential / Conditional / Non-essential).
4. Dua strategi hemat energi (Non-essential Shutdown dan Usage-based Restriction).
5. Enam operator Boolean (AND, OR, NOT, XOR, NAND, NOR) beserta demonstrasinya.
6. Mini research (3 eksperimen) dengan keluaran CSV.

Di luar lingkup: perangkat keras/IoT nyata, internet/API, database server, framework web, dependency eksternal.

---

## 2. Variabel Boolean

| Variabel | Modul | Arti TRUE |
|---|---|---|
| `security_mode` | Security | Mode keamanan aktif |
| `door_open` | Security | Sensor pintu utama mendeteksi pintu terbuka |
| `door_open_redundant` | Diagnostik | Sensor pintu redundan mendeteksi pintu terbuka |
| `motion_detected` | Security | Sensor gerak mendeteksi gerakan |
| `motion_sensor_online` | Diagnostik | Sensor gerak merespons uji diagnostik |
| `alarm_active` | Security | Alarm menyala (keluaran) |
| `occupied` | Lighting / Energy | Rumah/ruangan ditempati |
| `dark` | Lighting | Ruangan gelap |
| `lamp_on` | Lighting | Lampu menyala (keluaran) |
| `energy_saving_mode` | Energy | Mode hemat energi aktif |
| `nonessential_allowed` | Energy | Perangkat non-esensial boleh beroperasi (keluaran) |
| `duration_limit_reached` | Energy | Batas durasi harian tercapai (hasil konversi numerik → Boolean) |
| `frequency_limit_reached` | Energy | Batas jumlah aktivasi harian tercapai |
| `inactivity_exceeded` | Energy | Waktu tidak aktif ≥ batas timeout |

## 3. Persamaan Boolean

| # | Persamaan | Modul |
|---|---|---|
| E1 | `alarm_active = security_mode AND (door_open OR motion_detected)` | security.py |
| E2 | `lamp_on = occupied AND dark` (hanya pada mode AUTO; ON/OFF override) | lighting.py |
| E3 | `nonessential_allowed = occupied AND NOT energy_saving_mode` | energy_manager.py |
| E4 | `usage_blocked = duration_limit_reached OR frequency_limit_reached OR inactivity_exceeded` | energy_manager.py |
| E5 | `non-essential boleh ON = nonessential_allowed AND NOT usage_blocked` | energy_manager.py |
| E6 | `door_mismatch = door_open XOR door_open_redundant` | sensors.py |
| E7 | `no_activity = door_open NOR motion_detected` | sensors.py |
| E8 | `diagnostics_incomplete = (NOT door_mismatch) NAND motion_sensor_online` | sensors.py |

**Konsistensi E3 dengan teks "Strategy 1":** teks meminta non-esensial dimatikan ketika *rumah tidak ditempati ATAU mode hemat aktif*. Negasi dari E3 adalah `NOT occupied OR energy_saving_mode` (hukum De Morgan), sehingga keduanya konsisten.

## 4. Kebutuhan Fungsional

| ID | Kebutuhan |
|---|---|
| FR-01 | Pengguna dapat mengubah status setiap sensor dan mode keamanan secara interaktif. |
| FR-02 | Alarm dihitung dengan E1 dan alasan aktif/tidaknya ditampilkan. |
| FR-03 | Lampu mendukung mode AUTO, ON, OFF; ON/OFF mengalahkan keputusan otomatis; perubahan mode terlihat di terminal. |
| FR-04 | Sistem menyimpan daftar perangkat (nama, kategori, daya, kondisi, batas penggunaan). |
| FR-05 | Pengguna dapat melihat daftar perangkat, kategori, daya, dan mengubah statusnya (simulasi), beserta alasan diizinkan/tidak. |
| FR-06 | Perangkat Essential tidak pernah dimatikan oleh kebijakan energi. |
| FR-07 | Strategy 1: non-esensial dimatikan jika `NOT nonessential_allowed`. |
| FR-08 | Strategy 2: batas durasi harian, batas frekuensi aktivasi, dan inactivity timeout, semua dapat dikonfigurasi. |
| FR-09 | Hasil numerik (menit, jumlah aktivasi) dikonversi menjadi Boolean sebelum dipakai keputusan. |
| FR-10 | Waktu simulasi dapat dimajukan (menit) tanpa menunggu waktu nyata. |
| FR-11 | Enam operator Boolean tersedia sebagai fungsi terpisah dan dapat didemokan dengan input pengguna + tabel kebenaran. |
| FR-12 | XOR didemokan sebagai deteksi ketidaksesuaian dua sensor pintu redundan (tanpa menyimpulkan sensor rusak). |
| FR-13 | Energi (kWh) = Daya (W) × Waktu (jam) / 1000; tersedia per perangkat, total, perbandingan skenario, penghematan, dan persentase. |
| FR-14 | Mini research: Eksperimen 1 (validasi Boolean), 2 (8 skenario keamanan), 3 (simulasi energi 3 skenario); hasil disimpan ke CSV. |
| FR-15 | Seluruh input CLI divalidasi; input salah tidak menghentikan program. |

## 5. Kebutuhan Non-Fungsional

| ID | Kebutuhan |
|---|---|
| NFR-01 | Python 3 (diuji pada 3.12), Standard Library only, berjalan offline. |
| NFR-02 | Arsitektur modular; tiap file punya satu tanggung jawab. |
| NFR-03 | Type hints dan docstring pada setiap modul, class, dan fungsi. |
| NFR-04 | Unit test `unittest`, deterministik, tidak bergantung waktu nyata. |
| NFR-05 | Semua hasil energi berlabel *simulasi*, bukan pengukuran nyata. |
| NFR-06 | Dokumentasi (termasuk line-by-line guide) sinkron dengan kode final. |

## 6. Kategori dan Aturan Perangkat

| Perangkat | Kategori | Daya (asumsi) | Kondisi operasi | Batas penggunaan (konfigurabel) |
|---|---|---:|---|---|
| Refrigerator | Essential | 150 W | selalu diizinkan | tidak berlaku |
| Main Lighting | Conditional | 12 W | diizinkan jika `lamp_on` TRUE | tidak berlaku |
| Fan | Conditional | 45 W | diizinkan jika `occupied` TRUE | tidak berlaku |
| Television | Non-essential | 80 W | E3 AND NOT E4 | maks 240 menit/hari, maks 6 aktivasi/hari, timeout 120 menit |
| Decorative Lighting | Non-essential | 20 W | E3 AND NOT E4 | maks 240 menit/hari, timeout 60 menit |

Semua angka merupakan **asumsi simulasi**, bukan spesifikasi perangkat nyata.

## 7. Analisis Konsistensi dan Keputusan atas Ambiguitas (Aturan 13)

Tidak ditemukan konflik yang menghalangi implementasi. Ambiguitas berikut diputuskan dengan asumsi dan **dicatat di sini agar dapat dikoreksi kelompok**:

| # | Ambiguitas | Keputusan |
|---|---|---|
| A1 | Aturan operasi Fan dan Main Lighting (Conditional) tidak dirinci. | Main Lighting mengikuti `lamp_on` (E2). Fan hanya boleh beroperasi saat `occupied` TRUE. |
| A2 | Strategy 2 berlaku untuk kategori mana? | Hanya Non-essential. Essential dikecualikan (sesuai spesifikasi); Conditional diatur oleh kondisinya sendiri. |
| A3 | Arti "frekuensi" vs "durasi" vs "inactivity". | Frekuensi = jumlah aktivasi per hari; durasi = total menit ON per hari; inactivity = menit sejak aktivitas pengguna terakhir saat perangkat ON. Ketiganya dipisah. |
| A4 | Kapan batas frekuensi memblokir? | Hanya saat permintaan aktivasi baru (perangkat yang sedang ON tidak dimatikan karena aktivasi terakhirnya sah). |
| A5 | Sensor pintu redundan padahal keamanan "hanya dua jenis sensor". | Sensor redundan adalah sensor *pintu* kedua yang dipakai **hanya untuk diagnostik XOR**; tidak masuk rumus alarm E1. |
| A6 | Definisi diagnostik NAND tidak rinci. | `diagnostics_incomplete = NAND(door_consistent, motion_sensor_online)`: TRUE bila tidak semua kondisi diagnostik terpenuhi. |
| A7 | Apakah pengguna boleh mematikan perangkat Essential manual? | Tidak: simulasi mengunci Refrigerator tetap ON ("harus tetap aktif"). |
| A8 | Mode ON/OFF lampu memengaruhi Main Lighting perangkat. | Ya; keputusan akhir lampu (`lamp_on` setelah override) dipakai sebagai kondisi Main Lighting. |
| A9 | Inactivity pada perangkat OFF. | Hanya dievaluasi pada perangkat ON; menyalakan ulang dianggap aktivitas baru yang mereset timer, tetapi batas durasi/frekuensi tetap menghalangi. |
| A10 | Penghematan tidak boleh negatif. | `compute_savings` melempar `ValueError` bila skenario otomatis memakai energi lebih besar dari baseline (indikasi kesalahan logika), bukan memotong angkanya menjadi 0. |

## 8. Skenario Mini Research

| Eksperimen | Tujuan | Keluaran |
|---|---|---|
| 1 | Validasi enam operator terhadap tabel kebenaran (referensi aritmetika 0/1) | jumlah benar/salah, akurasi |
| 2 | Delapan kombinasi security_mode × door × motion | tabel aktual vs ekspektasi |
| 3 | Simulasi sehari (1440 menit): tanpa otomatisasi, otomatisasi, otomatisasi + hemat + batas | menit ON, kWh, selisih, % penghematan |

Pembedaan data: **asumsi** (daya, profil jam, batas), **input simulasi** (profil hunian/gelap/keinginan pengguna), **hasil pengujian aktual** (keluaran program saat dijalankan; tercatat di `TESTING_REPORT.md` dan `data/research_results.csv`).
