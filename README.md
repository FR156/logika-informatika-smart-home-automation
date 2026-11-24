# Smart Home Automation & Energy Management System (Python CLI MVP)

Simulasi keamanan dan hemat energi smart home memakai Aljabar Boolean. **Python 3 Standard Library only**, berjalan offline, tanpa perangkat keras.
Diuji pada Python 3.12.

## Instalasi
Tidak ada yang perlu diinstal. Pastikan `python --version` menunjukkan Python 3.9 atau lebih baru (diuji di 3.12).

## Menjalankan
```text
python main.py                                   # program CLI
python -m unittest discover -s tests -v          # seluruh unit test
python -c "import research; print(research.run_all())"   # mini research + tulis data/research_results.csv
python tools/generate_line_guide.py              # perbarui docs/LINE_BY_LINE_GUIDE.md setelah kode berubah
```

## Menu
1 Sensor, 2 Security (alarm + diagnostik XOR/NOR/NAND), 3 Lighting (AUTO/ON/OFF), 4 Appliances,
5 Energy (Strategy 1 & 2, majukan waktu simulasi, laporan kWh, ubah batas), 6 Boolean demo (6 operator + tabel kebenaran),
7 Mini Research (3 eksperimen + CSV), 8 Exit. Input salah tidak menghentikan program; kosongkan input untuk membatalkan.

## Konfigurasi
Daya dan batas penggunaan ada di `config.py` (default) dan `data/config.json` (menimpa default). Semua angka adalah **asumsi simulasi**.

## Dokumentasi (urutan belajar yang disarankan)
1. `docs/BOOLEAN_LOGIC.md` — dasar logika dan rumus.
2. `docs/SRS.md` — kebutuhan, variabel, persamaan, dan keputusan atas ambiguitas.
3. `docs/SOFTWARE_ARCHITECTURE.md` — struktur dan diagram.
4. `docs/LINE_BY_LINE_GUIDE.md` — penjelasan setiap baris kode (dibuat otomatis dari kode).
5. `docs/TESTING_REPORT.md`, `docs/RESEARCH_METHODOLOGY.md`, `docs/JOURNAL_NOTES.md`.

## Catatan
Hasil energi adalah simulasi, bukan pengukuran listrik nyata. Referensi akademik pada jurnal belum diisi (ditandai `[PERLU REFERENSI]`).
