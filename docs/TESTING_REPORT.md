# Testing Report

Seluruh angka di bawah diambil dari eksekusi nyata pada Python 3.12.3 (Linux), offline, tanpa package eksternal.

## 1. Cara Menjalankan

```text
python -m unittest discover -s tests -v
```

## 2. Hasil Unit Test (hasil eksekusi aktual)

```text
Ran 53 tests in 0.111s
OK
```

| File test | Jumlah test | Cakupan |
|---|---:|---|
| test_boolean_operations.py | 7 | enam operator vs tabel manual, referensi aritmetika, arity, format tabel |
| test_security.py | 6 | 8 kombinasi alarm, alasan, XOR/NOR/NAND diagnostik, validasi `parse_bool` |
| test_lighting.py | 6 | AUTO/ON/OFF, prioritas override, alasan, validasi `parse_lighting_mode` |
| test_appliances.py | 10 | klasifikasi, daya, pencarian, ON/OFF, waktu simulasi, reset, validasi konfigurasi, JSON rusak |
| test_energy_manager.py | 24 | Strategy 1, pengecualian Essential, Conditional, durasi, frekuensi, inactivity, kWh, penghematan, Experiment 1-3, CSV |
| **Total** | **53** | **0 gagal, 0 error** |

Pemenuhan ketentuan Bagian 10 spesifikasi:

| Ketentuan | Status |
|---|---|
| Enam operator Boolean | diuji |
| Seluruh kombinasi alarm | 8 dari 8 diuji |
| Tiga mode pencahayaan | diuji |
| Klasifikasi perangkat | diuji |
| Pengecualian Essential | diuji (shutdown, batas penggunaan) |
| Shutdown non-esensial | diuji |
| Batas durasi | diuji (239 → boleh, 240 → diblokir, blokir re-aktivasi, reset hari) |
| Inactivity timeout | diuji (59 → boleh, 60 → diblokir, `touch` mereset) |
| Perhitungan konsumsi energi | diuji |
| Validasi input penting | diuji (`parse_bool`, `parse_lighting_mode`, `advance_minutes`, konfigurasi, JSON rusak) |
| Tidak bergantung waktu nyata | tidak ada `time`/`datetime` pada kode maupun test; waktu = argumen menit |
| Tanpa dependency eksternal | diaudit via AST: seluruh import adalah Standard Library atau modul proyek |

## 3. Uji Integrasi CLI (manual, dijalankan dengan input terjadwal)

| Skenario | Hasil |
|---|---|
| Input menu tidak valid (`abc`, `9`) | pesan kesalahan, menu diulang, program tidak berhenti |
| Nilai bool tidak valid (`x`) | pesan "Masukan tidak dikenali", diminta ulang |
| Input berakhir mendadak (EOF) | program keluar bersih, kode keluar 0, tanpa traceback |
| Ganti mode lampu AUTO → ON | pesan "Mode lampu berubah: AUTO -> ON", status lampu ON |
| Nyalakan perangkat saat diizinkan | "Berhasil dinyalakan" + alasan |
| Mode hemat energi ON lalu minta TV | ditolak dengan alasan Strategy 1 |
| Menu 7 (Research) | tiga eksperimen berjalan, CSV tertulis |

Uji ini dijalankan lewat pipe input pada sesi pengembangan; bukan test otomatis di folder `tests/`.

## 4. Hasil Mini Research (eksekusi aktual `research.run_all()`)

**Experiment 1** — 22 pengujian (AND 4, OR 4, NOT 2, XOR 4, NAND 4, NOR 4): benar 22, salah 0, akurasi **100.0%**.

**Experiment 2** — 8 kombinasi: lulus 8/8. Alarm aktif hanya pada (mode=1,door=0,motion=1), (1,1,0), (1,1,1).

**Experiment 3** (SIMULASI, bukan pengukuran listrik nyata):

| Perangkat | A menit | A kWh | B menit | B kWh | C menit | C kWh |
|---|---:|---:|---:|---:|---:|---:|
| Refrigerator | 1440 | 3.600 | 1440 | 3.600 | 1440 | 3.600 |
| Main Lighting | 900 | 0.180 | 720 | 0.144 | 720 | 0.144 |
| Fan | 840 | 0.630 | 360 | 0.270 | 360 | 0.270 |
| Television | 720 | 0.960 | 360 | 0.480 | 240 | 0.320 |
| Decorative Lighting | 600 | 0.200 | 540 | 0.180 | 180 | 0.060 |
| **Total** | | **5.570** | | **4.674** | | **4.394** |
| Penghematan vs A | | – | | 0.896 kWh (16.09%) | | 1.176 kWh (21.11%) |

A = tanpa otomatisasi, B = otomatisasi, C = otomatisasi + mode hemat + batas penggunaan.

## 5. Temuan Selama Pengembangan

- Pembuatan folder awal memakai brace expansion yang tidak didukung `sh`, sehingga folder `tests/` tidak terbentuk dan percobaan test pertama gagal dengan `ImportError: Start directory is not importable`. Folder dibuat ulang dan test dijalankan kembali; hasil di atas berasal dari eksekusi setelah perbaikan.
- Generator line-by-line pertama menandai baris `def boolean_and(...)` sebagai ekspresi Boolean (positif palsu). Diperbaiki, dihasilkan ulang, dan nomor baris divalidasi otomatis terhadap source (2.210 baris diperiksa, 0 ketidakcocokan; angka ini bertambah jika kode ditambah).

## 6. Keterbatasan Pengujian

- `main.py` (lapisan CLI) tidak memiliki unit test otomatis; hanya diuji manual seperti pada Bagian 3.
- Tidak dilakukan pengukuran cakupan kode (coverage) karena tidak ada alat di Standard Library untuk itu.
- Pengujian hanya pada satu lingkungan (Linux, Python 3.12).
