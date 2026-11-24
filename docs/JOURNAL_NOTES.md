# Journal Notes — Bahan Penyusunan Jurnal (Bab I–IV)

Konvensi penandaan:
- **[FAKTA IMPLEMENTASI]** = benar-benar ada di kode.
- **[ASUMSI]** = asumsi simulasi.
- **[INTERPRETASI]** = tafsiran terhadap hasil; perlu dipertimbangkan kelompok.
- **[PERLU REFERENSI]** = klaim umum yang membutuhkan sumber akademik; **belum ada sitasi, sengaja tidak dikarang**. Kelompok perlu mencari dan memverifikasi sumbernya sendiri.

---

## BAB I — PENDAHULUAN

### 1.1 Latar Belakang
Rumah pintar (smart home) mengotomatisasi keamanan, pencahayaan, dan pemakaian listrik berdasarkan kondisi sensor. [PERLU REFERENSI: tren smart home dan konsumsi energi rumah tangga]. Keputusan otomatis pada sistem tersebut pada dasarnya berupa keputusan ya/tidak (alarm menyala atau tidak, lampu menyala atau tidak, perangkat diizinkan atau tidak) sehingga dapat dimodelkan dengan Aljabar Boolean. Proyek ini membuat prototipe CLI Python yang mensimulasikan tiga fungsi (keamanan, pencahayaan, manajemen energi) dengan enam operator Boolean, tanpa perangkat keras.

### 1.2 Rumusan Masalah
1. Bagaimana memodelkan logika alarm keamanan dengan Aljabar Boolean?
2. Bagaimana memodelkan otomatisasi lampu beserta manual override?
3. Bagaimana memodelkan kebijakan hemat energi yang membedakan perangkat esensial, kondisional, dan non-esensial?
4. Bagaimana kebenaran logika divalidasi dan dampak simulasi pada konsumsi energi diperkirakan?

### 1.3 Tujuan
Merancang dan mengimplementasikan model logika Boolean untuk ketiga fungsi di atas; memvalidasinya terhadap tabel kebenaran; dan membandingkan konsumsi energi simulasi pada tiga skenario.

### 1.4 Manfaat
Bagi kelompok: pemahaman Aljabar Boolean dan Python. Bagi pembaca: contoh penerapan Boolean yang dapat diuji ulang. [Manfaat praktis lain: kelompok menambahkan sendiri.]

### 1.5 Batasan Masalah
Simulasi CLI tanpa sensor/IoT nyata; hanya Standard Library Python; dua sensor keamanan (pintu dan gerak) ditambah satu sensor pintu redundan untuk diagnostik; lima perangkat; satu hari simulasi; daya dan batas penggunaan adalah asumsi; tanpa pengukuran listrik nyata.

---

## BAB II — PEMBAHASAN DAN LANDASAN TEORI

Setiap subbagian berikut perlu diisi dari sumber akademik. Poin yang tersedia dari implementasi:

| Subbagian | Poin dari proyek | Status referensi |
|---|---|---|
| Aljabar Boolean | dua nilai, operasi AND/OR/NOT, hukum De Morgan dipakai pada Strategy 1 (lihat `BOOLEAN_LOGIC.md`) | [PERLU REFERENSI] |
| Operator Boolean | AND, OR, NOT, XOR, NAND, NOR beserta tabel kebenaran | [PERLU REFERENSI] |
| Smart home | definisi, komponen sensor-pengendali-aktuator | [PERLU REFERENSI] |
| Sistem keamanan otomatis | pola sensor pintu/gerak + mode aktif | [PERLU REFERENSI] |
| Otomatisasi pencahayaan | kontrol berbasis hunian dan cahaya, override manual | [PERLU REFERENSI] |
| Manajemen energi | `E (kWh) = P (W) x t (jam) / 1000` (rumus fisika dasar yang dipakai langsung); strategi pembatasan beban | [PERLU REFERENSI untuk strategi] |
| Python dan Boolean | `and`, `or`, `not`, tipe `bool`, `unittest`, `dataclasses` | dokumentasi resmi Python [PERLU DISITASI dengan versi] |
| Penelitian terdahulu | belum ada | [PERLU REFERENSI: cari 3-5 penelitian smart home / logika Boolean] |

---

## BAB III — REKAYASA IDE

### 3.1 Identifikasi Masalah
Alarm tidak boleh berbunyi saat mode keamanan mati; lampu tidak boleh menyala sia-sia; perangkat vital (kulkas) tidak boleh ikut dimatikan oleh penghematan; pembatasan harus dapat dikonfigurasi dan dapat diuji tanpa menunggu waktu nyata.

### 3.2 Ide Solusi
Memodelkan semua kondisi sebagai variabel bool, memakai rumus Boolean untuk keputusan, dan mengonversi data numerik (menit, jumlah aktivasi) menjadi Boolean sebelum dipakai keputusan.

### 3.3 Perancangan Sistem dan Persamaan Boolean [FAKTA IMPLEMENTASI]
Lihat `SRS.md` (variabel dan persamaan E1-E8) dan `BOOLEAN_LOGIC.md`.

| Fungsi | Persamaan |
|---|---|
| Alarm | `alarm_active = security_mode AND (door_open OR motion_detected)` |
| Lampu AUTO | `lamp_on = occupied AND dark` |
| Strategy 1 | `nonessential_allowed = occupied AND NOT energy_saving_mode` |
| Strategy 2 | `usage_blocked = duration OR frequency OR inactivity` |
| Diagnostik | XOR (pintu redundan), NOR (tanpa aktivitas), NAND (diagnostik tidak lengkap) |

### 3.4 Arsitektur dan Flowchart
Diagram Mermaid tersedia di `SOFTWARE_ARCHITECTURE.md` (arsitektur modul, alur eksekusi, flowchart keputusan perangkat). Ekspor gambar dari Mermaid untuk dimasukkan ke jurnal.

### 3.5 Rancangan Implementasi
Sembilan modul Python, 53 unit test, CLI delapan menu. Desain memisahkan perhitungan logika (`security.py`, `lighting.py`, `energy_manager.py`) dari antarmuka (`main.py`).

### 3.6 Keputusan Desain yang Perlu Dinyatakan di Jurnal
Keputusan A1-A10 pada `SRS.md` bagian 7 (mis. sensor pintu redundan hanya untuk diagnostik; Strategy 2 hanya untuk Non-essential; batas frekuensi hanya menahan aktivasi baru).

---

## BAB IV — MINI RESEARCH

### 4.1 Metodologi
Lihat `RESEARCH_METHODOLOGY.md`. Tiga eksperimen: validasi Boolean, skenario keamanan, simulasi energi sehari.

### 4.2 Skenario Pengujian
Experiment 1: 22 pengujian. Experiment 2: 8 kombinasi. Experiment 3: skenario A, B, C dengan profil hunian dan kebiasaan pada `research.py` [ASUMSI].

### 4.3 Hasil Pengujian [HASIL EKSEKUSI AKTUAL]
- Experiment 1: 22/22 benar, akurasi 100.0%.
- Experiment 2: 8/8 skenario sesuai ekspektasi.
- Experiment 3 (simulasi):

| Skenario | Total (kWh) | Penghematan vs A |
|---|---:|---:|
| A. Tanpa otomatisasi | 5.570 | – |
| B. Otomatisasi | 4.674 | 0.896 kWh (16.09%) |
| C. Otomatisasi + hemat + batas | 4.394 | 1.176 kWh (21.11%) |

Rincian per perangkat: `TESTING_REPORT.md` bagian 4 dan `data/research_results.csv`.

### 4.4 Analisis
- [FAKTA] Kulkas (Essential) tetap 1440 menit pada ketiga skenario (3.600 kWh) dan menjadi porsi terbesar total.
- [FAKTA] Dari A ke B, penurunan terbesar berasal dari televisi (0.480 kWh) dan kipas (0.360 kWh); lampu utama 0.036 kWh; lampu dekorasi 0.020 kWh.
- [FAKTA] Dari B ke C, penurunan berasal dari televisi (0.160 kWh, batas 240 menit) dan lampu dekorasi (0.120 kWh).
- [INTERPRETASI] Penghematan terutama muncul karena perangkat tidak lagi menyala saat rumah kosong (jam 08-17), yang merupakan konsekuensi dari profil asumsi, bukan temuan umum.
- [FAKTA] Pada skenario C, lampu dekorasi menyala 180 menit: karena tidak ada interaksi, timeout 60 menit mematikannya, lalu simulasi pengguna menyalakannya kembali di awal jam berikutnya. Pola nyala-mati bergantian ini adalah artefak model perilaku pengguna.

### 4.5 Pembahasan
Logika Boolean terbukti konsisten dengan tabel kebenaran pada seluruh kombinasi yang diuji. Besaran penghematan adalah hasil simulasi pada asumsi tertentu. Penghematan 16.09% dan 21.11% tidak boleh dikutip sebagai penghematan rumah nyata. Frekuensi penggunaan rendah tidak otomatis menandakan pemborosan; karena itu batas frekuensi hanya menahan aktivasi baru, bukan memvonis pemborosan.

### 4.6 Keterbatasan Penelitian
Satu hari, satu profil, daya konstan, tanpa standby/siklus kompresor, perilaku pengguna sederhana, tanpa data nyata, `main.py` tanpa unit test otomatis, dan belum ada tinjauan pustaka. Penelitian lanjutan: variasi profil, analisis sensitivitas terhadap batas, dan validasi dengan data pengukuran.
