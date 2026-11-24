# Research Methodology

## 1. Jenis Penelitian
Simulasi komputasional deterministik. Tidak ada pengukuran listrik, sensor fisik, atau responden. Hasil menunjukkan
perilaku logika program pada asumsi tertentu, bukan klaim tentang rumah nyata.

## 2. Klasifikasi Data

| Jenis | Isi | Lokasi |
|---|---|---|
| **Data asumsi** | daya perangkat (150/12/45/80/20 W), batas penggunaan (TV 240 mnt/6 aktivasi/timeout 120; dekorasi 240 mnt/timeout 60) | `config.py`, `data/config.json` |
| **Input simulasi** | profil jam hunian (kosong 08-17), gelap (18-05), jam mode hemat (00-05), kebiasaan pengguna per jam, interaksi TV tiap 30 menit | konstanta di `research.py` |
| **Hasil pengujian aktual** | keluaran program saat dijalankan | terminal, `data/research_results.csv`, `TESTING_REPORT.md` |

Kolom `data_type` pada CSV: `asumsi`, `asumsi_ekspektasi`, `hasil_pengujian`, `hasil_simulasi`.

## 3. Experiment 1 — Validasi Boolean
- **Tujuan:** memastikan fungsi sesuai tabel kebenaran.
- **Metode:** setiap kombinasi masukan dijalankan; hasil dibandingkan dengan referensi aritmetika 0/1 yang independen dari operator Python (`AND=a*b`, `OR=min(1,a+b)`, `XOR=(a+b) mod 2`, `NAND=1-a*b`, `NOR=1-min(1,a+b)`, `NOT=1-a`).
- **Metrik:** `Accuracy = (Correct / Total) x 100%`, target 100%.

## 4. Experiment 2 — Skenario Keamanan
- 2 x 2 x 2 = 8 kombinasi (`security_mode`, `door_open`, `motion_detected`).
- Ekspektasi ditulis manual sebagai tabel konstan (`EXPECTED_ALARM`), bukan dihitung ulang dengan rumus yang sama.
- Metrik: jumlah skenario yang aktual = ekspektasi.

## 5. Experiment 3 — Simulasi Konsumsi Energi
- **Satuan waktu:** 1 menit, 1440 langkah (1 hari). Energi: `kWh = W x (menit/60) / 1000`.
- **Skenario A (tanpa otomatisasi):** perangkat ON persis pada jam kebiasaan pengguna, tanpa kebijakan.
- **Skenario B (otomatisasi):** lampu = `occupied AND dark`; kipas hanya saat `occupied`; Strategy 1 aktif (non-esensial hanya saat rumah ditempati).
- **Skenario C:** B + mode hemat energi pada jam 00-05 + Strategy 2 (durasi, frekuensi, inactivity).
- **Perilaku pengguna tersimulasi:** pengguna menekan tombol non-esensial di awal setiap jam yang diinginkan jika perangkat OFF; menyentuh TV tiap 30 menit; tidak menyentuh lampu dekorasi setelah menyala.
- Logika keputusan memakai `request_turn_on` dan `enforce_policy` yang sama dengan CLI.
- **Keluaran:** menit ON, kWh per perangkat, total, selisih, persentase penghematan, persentase perubahan.
- **Pengaman:** `compute_savings` melempar `ValueError` jika skenario otomatis lebih boros dari baseline.

## 6. Replikasi
```text
python -c "import research; print(research.run_all())"
```
Program deterministik: dua kali eksekusi menghasilkan angka identik (diuji di `test_experiment_3_is_deterministic`).

## 7. Ancaman Validitas
- Profil harian satu hari, satu rumah, dibuat peneliti; hasil sangat bergantung pada asumsi ini.
- Baseline A sengaja berupa kebiasaan "perangkat dibiarkan menyala"; persentase penghematan akan lebih kecil pada pengguna yang sudah hemat.
- Daya konstan; tidak memodelkan standby, siklus kompresor kulkas, atau variasi beban.
- Persentase penghematan tidak boleh digeneralisasi ke rumah nyata.
