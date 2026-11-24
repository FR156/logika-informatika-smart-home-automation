# Line-by-Line Guide

Panduan ini dibuat OTOMATIS oleh `tools/generate_line_guide.py` dari source code final, sehingga
nomor baris selalu cocok. **Jalankan ulang generator setiap kali source code berubah.**

Cara membaca: setiap entri berisi nomor baris, kode asli, dan penjelasan. Penjelasan disusun dari
struktur program (AST): jenis pernyataan, nama variabel/fungsi, parameter, ekspresi, serta tujuan
fungsi yang diambil dari docstring-nya. Setelah setiap fungsi/class ada paragraf *Hubungan antarbaris*.

Perintah: `python tools/generate_line_guide.py`

## boolean_operations.py

~~~~text
File: boolean_operations.py

Line 1:
Kode: """Modul operator Boolean.
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 2:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 3:
Kode: Tujuan file:
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 4:
Kode:     Menyediakan enam operator Boolean (AND, OR, NOT, XOR, NAND, NOR) sebagai
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 5:
Kode:     fungsi terpisah, ditambah utilitas tabel kebenaran dan nilai referensi
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 6:
Kode:     aritmetika 0/1 yang dipakai untuk validasi pada mini research.
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 7:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 8:
Kode: Semua modul lain WAJIB memakai fungsi di sini untuk keputusan logika sistem,
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 9:
Kode: sehingga seluruh logika Boolean proyek berada di satu tempat.
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 10:
Kode: """
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 11:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 12:
Kode: from itertools import product
Penjelasan: Mengimpor product dari modul `itertools`.

Line 13:
Kode: from typing import Callable, Dict, List, Tuple
Penjelasan: Mengimpor Callable, Dict, List, Tuple dari modul `typing`.

Line 14:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 15:
Kode: OPERATOR_NAMES: Tuple[str, ...] = ("AND", "OR", "NOT", "XOR", "NAND", "NOR")
Penjelasan: Mendeklarasikan variabel `OPERATOR_NAMES` bertipe `Tuple[str, ...]` dengan nilai awal `("AND", "OR", "NOT", "XOR", "NAND", "NOR")`.

Line 16:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 17:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 18:
Kode: def boolean_and(a: bool, b: bool) -> bool:
Penjelasan: Mendefinisikan fungsi `boolean_and` dengan parameter: a: bool, b: bool dan tipe kembalian `bool`. Tujuan: AND: TRUE hanya jika kedua masukan TRUE.

Line 19:
Kode:     """AND: TRUE hanya jika kedua masukan TRUE.
Penjelasan: Bagian docstring `boolean_and`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 20:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 21:
Kode:     Rumus: A AND B. Dipakai pada syarat alarm dan lampu otomatis.
Penjelasan: Bagian docstring `boolean_and`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 22:
Kode:     """
Penjelasan: Bagian docstring `boolean_and`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 23:
Kode:     return bool(a and b)
Penjelasan: Mengembalikan hasil ekspresi `bool(a and b)` kepada pemanggil fungsi. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Hubungan antarbaris (fungsi `boolean_and`, baris 18-23): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: AND: TRUE hanya jika kedua masukan TRUE.

Line 24:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 25:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 26:
Kode: def boolean_or(a: bool, b: bool) -> bool:
Penjelasan: Mendefinisikan fungsi `boolean_or` dengan parameter: a: bool, b: bool dan tipe kembalian `bool`. Tujuan: OR: TRUE jika minimal satu masukan TRUE.

Line 27:
Kode:     """OR: TRUE jika minimal satu masukan TRUE.
Penjelasan: Bagian docstring `boolean_or`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 28:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 29:
Kode:     Rumus: A OR B. Dipakai untuk mendeteksi aktivitas pintu ATAU gerak.
Penjelasan: Bagian docstring `boolean_or`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 30:
Kode:     """
Penjelasan: Bagian docstring `boolean_or`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 31:
Kode:     return bool(a or b)
Penjelasan: Mengembalikan hasil ekspresi `bool(a or b)` kepada pemanggil fungsi. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Hubungan antarbaris (fungsi `boolean_or`, baris 26-31): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: OR: TRUE jika minimal satu masukan TRUE.

Line 32:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 33:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 34:
Kode: def boolean_not(a: bool) -> bool:
Penjelasan: Mendefinisikan fungsi `boolean_not` dengan parameter: a: bool dan tipe kembalian `bool`. Tujuan: NOT: membalik nilai masukan (TRUE menjadi FALSE dan sebaliknya).

Line 35:
Kode:     """NOT: membalik nilai masukan (TRUE menjadi FALSE dan sebaliknya)."""
Penjelasan: Bagian docstring `boolean_not`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 36:
Kode:     return not a
Penjelasan: Mengembalikan hasil ekspresi `not a` kepada pemanggil fungsi. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Hubungan antarbaris (fungsi `boolean_not`, baris 34-36): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: NOT: membalik nilai masukan (TRUE menjadi FALSE dan sebaliknya).

Line 37:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 38:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 39:
Kode: def boolean_xor(a: bool, b: bool) -> bool:
Penjelasan: Mendefinisikan fungsi `boolean_xor` dengan parameter: a: bool, b: bool dan tipe kembalian `bool`. Tujuan: XOR: TRUE jika kedua masukan BERBEDA.

Line 40:
Kode:     """XOR: TRUE jika kedua masukan BERBEDA.
Penjelasan: Bagian docstring `boolean_xor`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 41:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 42:
Kode:     Definisi: (A AND NOT B) OR (NOT A AND B), yang setara dengan A != B untuk bool.
Penjelasan: Bagian docstring `boolean_xor`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 43:
Kode:     Dipakai membandingkan dua sensor pintu redundan.
Penjelasan: Bagian docstring `boolean_xor`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 44:
Kode:     """
Penjelasan: Bagian docstring `boolean_xor`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 45:
Kode:     return bool(a) != bool(b)
Penjelasan: Mengembalikan hasil ekspresi `bool(a) != bool(b)` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `boolean_xor`, baris 39-45): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: XOR: TRUE jika kedua masukan BERBEDA.

Line 46:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 47:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 48:
Kode: def boolean_nand(a: bool, b: bool) -> bool:
Penjelasan: Mendefinisikan fungsi `boolean_nand` dengan parameter: a: bool, b: bool dan tipe kembalian `bool`. Tujuan: NAND: kebalikan AND; FALSE hanya jika kedua masukan TRUE.

Line 49:
Kode:     """NAND: kebalikan AND; FALSE hanya jika kedua masukan TRUE."""
Penjelasan: Bagian docstring `boolean_nand`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 50:
Kode:     return not (a and b)
Penjelasan: Mengembalikan hasil ekspresi `not (a and b)` kepada pemanggil fungsi. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Hubungan antarbaris (fungsi `boolean_nand`, baris 48-50): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: NAND: kebalikan AND; FALSE hanya jika kedua masukan TRUE.

Line 51:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 52:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 53:
Kode: def boolean_nor(a: bool, b: bool) -> bool:
Penjelasan: Mendefinisikan fungsi `boolean_nor` dengan parameter: a: bool, b: bool dan tipe kembalian `bool`. Tujuan: NOR: kebalikan OR; TRUE hanya jika kedua masukan FALSE.

Line 54:
Kode:     """NOR: kebalikan OR; TRUE hanya jika kedua masukan FALSE."""
Penjelasan: Bagian docstring `boolean_nor`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 55:
Kode:     return not (a or b)
Penjelasan: Mengembalikan hasil ekspresi `not (a or b)` kepada pemanggil fungsi. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Hubungan antarbaris (fungsi `boolean_nor`, baris 53-55): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: NOR: kebalikan OR; TRUE hanya jika kedua masukan FALSE.

Line 56:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 57:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 58:
Kode: BINARY_OPERATORS: Dict[str, Callable[[bool, bool], bool]] = {
Penjelasan: Mendeklarasikan variabel `BINARY_OPERATORS` bertipe `Dict[str, Callable[[bool, bool], bool]]` dengan nilai awal `{ "AND": boolean_and, "OR": boolean_or, "XOR": boolean_xor, "NAND": boolean_nand, "NOR": boolean_nor, }`.

Line 59:
Kode:     "AND": boolean_and,
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 58 (`BINARY_OPERATORS: Dict[str, Callable[[bool, bool], bool]]...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 60:
Kode:     "OR": boolean_or,
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 58 (`BINARY_OPERATORS: Dict[str, Callable[[bool, bool], bool]]...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 61:
Kode:     "XOR": boolean_xor,
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 58 (`BINARY_OPERATORS: Dict[str, Callable[[bool, bool], bool]]...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 62:
Kode:     "NAND": boolean_nand,
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 58 (`BINARY_OPERATORS: Dict[str, Callable[[bool, bool], bool]]...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 63:
Kode:     "NOR": boolean_nor,
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 58 (`BINARY_OPERATORS: Dict[str, Callable[[bool, bool], bool]]...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 64:
Kode: }
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 58 (`BINARY_OPERATORS: Dict[str, Callable[[bool, bool], bool]]...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 65:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 66:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 67:
Kode: def operator_arity(name: str) -> int:
Penjelasan: Mendefinisikan fungsi `operator_arity` dengan parameter: name: str dan tipe kembalian `int`. Tujuan: Mengembalikan jumlah masukan operator (1 untuk NOT, 2 untuk lainnya).

Line 68:
Kode:     """Mengembalikan jumlah masukan operator (1 untuk NOT, 2 untuk lainnya).
Penjelasan: Bagian docstring `operator_arity`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 69:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 70:
Kode:     Raises:
Penjelasan: Bagian docstring `operator_arity`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 71:
Kode:         ValueError: jika nama operator tidak dikenal.
Penjelasan: Bagian docstring `operator_arity`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 72:
Kode:     """
Penjelasan: Bagian docstring `operator_arity`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 73:
Kode:     key = name.strip().upper()
Penjelasan: Menetapkan variabel `key` dengan nilai `name.strip().upper()`.

Line 74:
Kode:     if key == "NOT":
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `key == "NOT"` bernilai True.

Line 75:
Kode:         return 1
Penjelasan: Mengembalikan hasil ekspresi `1` kepada pemanggil fungsi.

Line 76:
Kode:     if key in BINARY_OPERATORS:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `key in BINARY_OPERATORS` bernilai True.

Line 77:
Kode:         return 2
Penjelasan: Mengembalikan hasil ekspresi `2` kepada pemanggil fungsi.

Line 78:
Kode:     raise ValueError(f"Operator tidak dikenal: {name!r}")
Penjelasan: Melempar exception `ValueError(f"Operator tidak dikenal: {name!r}")` untuk melaporkan kondisi tidak valid. Exception handling: menangani atau melaporkan kesalahan agar program tidak berhenti mendadak.

Hubungan antarbaris (fungsi `operator_arity`, baris 67-78): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Mengembalikan jumlah masukan operator (1 untuk NOT, 2 untuk lainnya).

Line 79:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 80:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 81:
Kode: def evaluate_operator(name: str, *inputs: bool) -> bool:
Penjelasan: Mendefinisikan fungsi `evaluate_operator` dengan parameter: name: str, *inputs: bool dan tipe kembalian `bool`. Tujuan: Menjalankan operator berdasarkan nama.

Line 82:
Kode:     """Menjalankan operator berdasarkan nama.
Penjelasan: Bagian docstring `evaluate_operator`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 83:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 84:
Kode:     Args:
Penjelasan: Bagian docstring `evaluate_operator`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 85:
Kode:         name: nama operator (AND, OR, NOT, XOR, NAND, NOR).
Penjelasan: Bagian docstring `evaluate_operator`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 86:
Kode:         *inputs: nilai bool; jumlahnya harus sesuai arity operator.
Penjelasan: Bagian docstring `evaluate_operator`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 87:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 88:
Kode:     Raises:
Penjelasan: Bagian docstring `evaluate_operator`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 89:
Kode:         ValueError: nama tidak dikenal atau jumlah masukan salah.
Penjelasan: Bagian docstring `evaluate_operator`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 90:
Kode:     """
Penjelasan: Bagian docstring `evaluate_operator`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 91:
Kode:     key = name.strip().upper()
Penjelasan: Menetapkan variabel `key` dengan nilai `name.strip().upper()`.

Line 92:
Kode:     if len(inputs) != operator_arity(key):
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `len(inputs) != operator_arity(key)` bernilai True.

Line 93:
Kode:         raise ValueError(f"Operator {key} membutuhkan {operator_arity(key)} masukan.")
Penjelasan: Melempar exception `ValueError(f"Operator {key} membutuhkan {operator_arity(key)} masukan.")` untuk melaporkan kondisi tidak valid. Exception handling: menangani atau melaporkan kesalahan agar program tidak berhenti mendadak.

Line 94:
Kode:     if key == "NOT":
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `key == "NOT"` bernilai True.

Line 95:
Kode:         return boolean_not(inputs[0])
Penjelasan: Mengembalikan hasil ekspresi `boolean_not(inputs[0])` kepada pemanggil fungsi. Ekspresi Boolean: memakai operator NOT dari boolean_operations.py.

Line 96:
Kode:     return BINARY_OPERATORS[key](inputs[0], inputs[1])
Penjelasan: Mengembalikan hasil ekspresi `BINARY_OPERATORS[key](inputs[0], inputs[1])` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `evaluate_operator`, baris 81-96): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Menjalankan operator berdasarkan nama.

Line 97:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 98:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 99:
Kode: def reference_result(name: str, inputs: Tuple[bool, ...]) -> bool:
Penjelasan: Mendefinisikan fungsi `reference_result` dengan parameter: name: str, inputs: Tuple[bool, ...] dan tipe kembalian `bool`. Tujuan: Nilai referensi independen memakai aritmetika bilangan bulat 0/1.

Line 100:
Kode:     """Nilai referensi independen memakai aritmetika bilangan bulat 0/1.
Penjelasan: Bagian docstring `reference_result`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 101:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 102:
Kode:     Dipakai sebagai 'jawaban benar' pada validasi, sengaja TIDAK memakai
Penjelasan: Bagian docstring `reference_result`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 103:
Kode:     operator Python and/or/not agar validasi tidak membandingkan kode dengan dirinya sendiri.
Penjelasan: Bagian docstring `reference_result`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 104:
Kode:     """
Penjelasan: Bagian docstring `reference_result`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 105:
Kode:     key = name.strip().upper()
Penjelasan: Menetapkan variabel `key` dengan nilai `name.strip().upper()`.

Line 106:
Kode:     bits = [int(x) for x in inputs]
Penjelasan: Menetapkan variabel `bits` dengan nilai `[int(x) for x in inputs]`.

Line 107:
Kode:     if key == "NOT":
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `key == "NOT"` bernilai True.

Line 108:
Kode:         return (1 - bits[0]) == 1
Penjelasan: Mengembalikan hasil ekspresi `(1 - bits[0]) == 1` kepada pemanggil fungsi.

Line 109:
Kode:     a, b = bits
Penjelasan: Menetapkan variabel `(a, b)` dengan nilai `bits`.

Line 110:
Kode:     table = {
Penjelasan: Menetapkan variabel `table` dengan nilai `{ "AND": a * b, "OR": min(1, a + b), "XOR": (a + b) % 2, "NAND": 1 - a * b, "NOR": 1 - min(1, a + b), }`.

Line 111:
Kode:         "AND": a * b,
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 110 (`table = {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 112:
Kode:         "OR": min(1, a + b),
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 110 (`table = {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 113:
Kode:         "XOR": (a + b) % 2,
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 110 (`table = {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 114:
Kode:         "NAND": 1 - a * b,
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 110 (`table = {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 115:
Kode:         "NOR": 1 - min(1, a + b),
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 110 (`table = {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 116:
Kode:     }
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 110 (`table = {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 117:
Kode:     return table[key] == 1
Penjelasan: Mengembalikan hasil ekspresi `table[key] == 1` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `reference_result`, baris 99-117): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Nilai referensi independen memakai aritmetika bilangan bulat 0/1.

Line 118:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 119:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 120:
Kode: def input_combinations(name: str) -> List[Tuple[bool, ...]]:
Penjelasan: Mendefinisikan fungsi `input_combinations` dengan parameter: name: str dan tipe kembalian `List[Tuple[bool, ...]]`. Tujuan: Seluruh kombinasi masukan operator, urut dari (False, ...) ke (True, ...).

Line 121:
Kode:     """Seluruh kombinasi masukan operator, urut dari (False, ...) ke (True, ...)."""
Penjelasan: Bagian docstring `input_combinations`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 122:
Kode:     return list(product([False, True], repeat=operator_arity(name)))
Penjelasan: Mengembalikan hasil ekspresi `list(product([False, True], repeat=operator_arity(name)))` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `input_combinations`, baris 120-122): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Seluruh kombinasi masukan operator, urut dari (False, ...) ke (True, ...).

Line 123:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 124:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 125:
Kode: def truth_table(name: str) -> List[Tuple[Tuple[bool, ...], bool]]:
Penjelasan: Mendefinisikan fungsi `truth_table` dengan parameter: name: str dan tipe kembalian `List[Tuple[Tuple[bool, ...], bool]]`. Tujuan: Tabel kebenaran operator: daftar pasangan (masukan, keluaran).

Line 126:
Kode:     """Tabel kebenaran operator: daftar pasangan (masukan, keluaran)."""
Penjelasan: Bagian docstring `truth_table`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 127:
Kode:     return [(inputs, evaluate_operator(name, *inputs)) for inputs in input_combinations(name)]
Penjelasan: Mengembalikan hasil ekspresi `[(inputs, evaluate_operator(name, *inputs)) for inputs in input_combinations(name)]` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `truth_table`, baris 125-127): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Tabel kebenaran operator: daftar pasangan (masukan, keluaran).

Line 128:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 129:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 130:
Kode: def format_truth_table(name: str) -> str:
Penjelasan: Mendefinisikan fungsi `format_truth_table` dengan parameter: name: str dan tipe kembalian `str`. Tujuan: Membuat teks tabel kebenaran (1 = TRUE, 0 = FALSE) untuk dicetak di terminal.

Line 131:
Kode:     """Membuat teks tabel kebenaran (1 = TRUE, 0 = FALSE) untuk dicetak di terminal."""
Penjelasan: Bagian docstring `format_truth_table`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 132:
Kode:     key = name.strip().upper()
Penjelasan: Menetapkan variabel `key` dengan nilai `name.strip().upper()`.

Line 133:
Kode:     heads = ["A"] if operator_arity(key) == 1 else ["A", "B"]
Penjelasan: Menetapkan variabel `heads` dengan nilai `["A"] if operator_arity(key) == 1 else ["A", "B"]`.

Line 134:
Kode:     lines = [" ".join(heads) + f" | {key}", "-" * (2 * len(heads) + 3 + len(key))]
Penjelasan: Menetapkan variabel `lines` dengan nilai `[" ".join(heads) + f" | {key}", "-" * (2 * len(heads) + 3 + len(key))]`.

Line 135:
Kode:     for inputs, output in truth_table(key):
Penjelasan: Perulangan for: variabel `(inputs, output)` mengambil tiap elemen dari `truth_table(key)`, dan blok di bawahnya diulang untuk tiap elemen.

Line 136:
Kode:         lines.append(" ".join(str(int(x)) for x in inputs) + f" | {int(output)}")
Penjelasan: Memanggil `lines.append(" ".join(str(int(x)) for x in inputs) + f" | {int(output)}")` (hasilnya tidak disimpan; yang penting efeknya).

Line 137:
Kode:     return "\n".join(lines)
Penjelasan: Mengembalikan hasil ekspresi `"\n".join(lines)` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `format_truth_table`, baris 130-137): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Membuat teks tabel kebenaran (1 = TRUE, 0 = FALSE) untuk dicetak di terminal.

~~~~

## config.py

~~~~text
File: config.py

Line 1:
Kode: """Konfigurasi sistem: kategori, daftar perangkat, daya, dan batas penggunaan.
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 2:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 3:
Kode: Tujuan file:
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 4:
Kode:     Memusatkan semua angka asumsi simulasi supaya mudah diubah tanpa menyentuh
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 5:
Kode:     logika. Nilai default dapat ditimpa oleh data/config.json. Semua daya dan
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 6:
Kode:     batas di sini adalah ASUMSI simulasi, bukan spesifikasi perangkat nyata.
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 7:
Kode: """
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 8:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 9:
Kode: import json
Penjelasan: Mengimpor modul: json.

Line 10:
Kode: from dataclasses import dataclass
Penjelasan: Mengimpor dataclass dari modul `dataclasses`.

Line 11:
Kode: from pathlib import Path
Penjelasan: Mengimpor Path dari modul `pathlib`.

Line 12:
Kode: from typing import Any, Dict, List, Optional
Penjelasan: Mengimpor Any, Dict, List, Optional dari modul `typing`.

Line 13:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 14:
Kode: BASE_DIR: Path = Path(__file__).resolve().parent
Penjelasan: Mendeklarasikan variabel `BASE_DIR` bertipe `Path` dengan nilai awal `Path(__file__).resolve().parent`.

Line 15:
Kode: CONFIG_PATH: Path = BASE_DIR / "data" / "config.json"
Penjelasan: Mendeklarasikan variabel `CONFIG_PATH` bertipe `Path` dengan nilai awal `BASE_DIR / "data" / "config.json"`.

Line 16:
Kode: CSV_PATH: Path = BASE_DIR / "data" / "research_results.csv"
Penjelasan: Mendeklarasikan variabel `CSV_PATH` bertipe `Path` dengan nilai awal `BASE_DIR / "data" / "research_results.csv"`.

Line 17:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 18:
Kode: CATEGORY_ESSENTIAL = "Essential"
Penjelasan: Menetapkan konstanta/variabel modul `CATEGORY_ESSENTIAL` dengan nilai `"Essential"`.

Line 19:
Kode: CATEGORY_CONDITIONAL = "Conditional"
Penjelasan: Menetapkan konstanta/variabel modul `CATEGORY_CONDITIONAL` dengan nilai `"Conditional"`.

Line 20:
Kode: CATEGORY_NON_ESSENTIAL = "Non-essential"
Penjelasan: Menetapkan konstanta/variabel modul `CATEGORY_NON_ESSENTIAL` dengan nilai `"Non-essential"`.

Line 21:
Kode: VALID_CATEGORIES = (CATEGORY_ESSENTIAL, CATEGORY_CONDITIONAL, CATEGORY_NON_ESSENTIAL)
Penjelasan: Menetapkan konstanta/variabel modul `VALID_CATEGORIES` dengan nilai `(CATEGORY_ESSENTIAL, CATEGORY_CONDITIONAL, CATEGORY_NON_ESSENTIAL)`.

Line 22:
Kode: VALID_CONDITIONS = (None, "lamp", "occupied")
Penjelasan: Menetapkan konstanta/variabel modul `VALID_CONDITIONS` dengan nilai `(None, "lamp", "occupied")`.

Line 23:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 24:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 25:
Kode: @dataclass(frozen=True)
Penjelasan: Dekorator `@dataclass(frozen=True)`: memodifikasi class/fungsi di bawahnya (mis. membuat dataclass).

Line 26:
Kode: class UsageLimits:
Penjelasan: Mendefinisikan class `UsageLimits` dengan dekorator @dataclass(frozen=True). Tujuan: Batas penggunaan satu perangkat (None = tidak dibatasi).

Line 27:
Kode:     """Batas penggunaan satu perangkat (None = tidak dibatasi).
Penjelasan: Bagian docstring `UsageLimits`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 28:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 29:
Kode:     Attributes:
Penjelasan: Bagian docstring `UsageLimits`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 30:
Kode:         max_daily_minutes: batas DURASI total menit ON per hari.
Penjelasan: Bagian docstring `UsageLimits`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 31:
Kode:         max_daily_activations: batas FREKUENSI jumlah penyalaan per hari.
Penjelasan: Bagian docstring `UsageLimits`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 32:
Kode:         inactivity_timeout_minutes: batas menit tanpa aktivitas pengguna saat ON.
Penjelasan: Bagian docstring `UsageLimits`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 33:
Kode:     """
Penjelasan: Bagian docstring `UsageLimits`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 34:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 35:
Kode:     max_daily_minutes: Optional[int] = None
Penjelasan: Mendeklarasikan atribut class `max_daily_minutes` bertipe `Optional[int]` dengan nilai awal `None`.

Line 36:
Kode:     max_daily_activations: Optional[int] = None
Penjelasan: Mendeklarasikan atribut class `max_daily_activations` bertipe `Optional[int]` dengan nilai awal `None`.

Line 37:
Kode:     inactivity_timeout_minutes: Optional[int] = None
Penjelasan: Mendeklarasikan atribut class `inactivity_timeout_minutes` bertipe `Optional[int]` dengan nilai awal `None`.

Hubungan antarbaris (class `UsageLimits`, baris 26-37): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Batas penggunaan satu perangkat (None = tidak dibatasi).

Line 38:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 39:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 40:
Kode: @dataclass(frozen=True)
Penjelasan: Dekorator `@dataclass(frozen=True)`: memodifikasi class/fungsi di bawahnya (mis. membuat dataclass).

Line 41:
Kode: class DeviceSpec:
Penjelasan: Mendefinisikan class `DeviceSpec` dengan dekorator @dataclass(frozen=True). Tujuan: Spesifikasi statis perangkat.

Line 42:
Kode:     """Spesifikasi statis perangkat.
Penjelasan: Bagian docstring `DeviceSpec`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 43:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 44:
Kode:     Attributes:
Penjelasan: Bagian docstring `DeviceSpec`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 45:
Kode:         name: nama unik perangkat.
Penjelasan: Bagian docstring `DeviceSpec`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 46:
Kode:         category: salah satu VALID_CATEGORIES.
Penjelasan: Bagian docstring `DeviceSpec`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 47:
Kode:         power_w: daya asumsi dalam Watt (tidak negatif).
Penjelasan: Bagian docstring `DeviceSpec`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 48:
Kode:         condition: kondisi operasi untuk Conditional ("lamp", "occupied", atau None).
Penjelasan: Bagian docstring `DeviceSpec`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 49:
Kode:         limits: batas penggunaan (hanya dipakai kebijakan untuk Non-essential).
Penjelasan: Bagian docstring `DeviceSpec`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 50:
Kode:     """
Penjelasan: Bagian docstring `DeviceSpec`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 51:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 52:
Kode:     name: str
Penjelasan: Mendeklarasikan atribut class `name` bertipe `str`.

Line 53:
Kode:     category: str
Penjelasan: Mendeklarasikan atribut class `category` bertipe `str`.

Line 54:
Kode:     power_w: float
Penjelasan: Mendeklarasikan atribut class `power_w` bertipe `float`.

Line 55:
Kode:     condition: Optional[str] = None
Penjelasan: Mendeklarasikan atribut class `condition` bertipe `Optional[str]` dengan nilai awal `None`.

Line 56:
Kode:     limits: UsageLimits = UsageLimits()
Penjelasan: Mendeklarasikan atribut class `limits` bertipe `UsageLimits` dengan nilai awal `UsageLimits()`.

Hubungan antarbaris (class `DeviceSpec`, baris 41-56): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Spesifikasi statis perangkat.

Line 57:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 58:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 59:
Kode: @dataclass
Penjelasan: Dekorator `@dataclass`: memodifikasi class/fungsi di bawahnya (mis. membuat dataclass).

Line 60:
Kode: class AppConfig:
Penjelasan: Mendefinisikan class `AppConfig` dengan dekorator @dataclass. Tujuan: Konfigurasi aplikasi: daftar perangkat dan saklar dua strategi hemat energi.

Line 61:
Kode:     """Konfigurasi aplikasi: daftar perangkat dan saklar dua strategi hemat energi."""
Penjelasan: Bagian docstring `AppConfig`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 62:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 63:
Kode:     devices: List[DeviceSpec]
Penjelasan: Mendeklarasikan atribut class `devices` bertipe `List[DeviceSpec]`.

Line 64:
Kode:     shutdown_enabled: bool = True
Penjelasan: Mendeklarasikan atribut class `shutdown_enabled` bertipe `bool` dengan nilai awal `True`.

Line 65:
Kode:     limits_enabled: bool = True
Penjelasan: Mendeklarasikan atribut class `limits_enabled` bertipe `bool` dengan nilai awal `True`.

Hubungan antarbaris (class `AppConfig`, baris 60-65): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Konfigurasi aplikasi: daftar perangkat dan saklar dua strategi hemat energi.

Line 66:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 67:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 68:
Kode: DEFAULT_DEVICES: List[DeviceSpec] = [
Penjelasan: Mendeklarasikan variabel `DEFAULT_DEVICES` bertipe `List[DeviceSpec]` dengan nilai awal `[ DeviceSpec("Refrigerator", CATEGORY_ESSENTIAL, 150.0), DeviceSpec("Main Lighting", CATEGORY_CONDITIONAL, ...`.

Line 69:
Kode:     DeviceSpec("Refrigerator", CATEGORY_ESSENTIAL, 150.0),
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 68 (`DEFAULT_DEVICES: List[DeviceSpec] = [`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 70:
Kode:     DeviceSpec("Main Lighting", CATEGORY_CONDITIONAL, 12.0, condition="lamp"),
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 68 (`DEFAULT_DEVICES: List[DeviceSpec] = [`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 71:
Kode:     DeviceSpec("Fan", CATEGORY_CONDITIONAL, 45.0, condition="occupied"),
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 68 (`DEFAULT_DEVICES: List[DeviceSpec] = [`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 72:
Kode:     DeviceSpec("Television", CATEGORY_NON_ESSENTIAL, 80.0,
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 68 (`DEFAULT_DEVICES: List[DeviceSpec] = [`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 73:
Kode:                limits=UsageLimits(240, 6, 120)),
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 68 (`DEFAULT_DEVICES: List[DeviceSpec] = [`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 74:
Kode:     DeviceSpec("Decorative Lighting", CATEGORY_NON_ESSENTIAL, 20.0,
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 68 (`DEFAULT_DEVICES: List[DeviceSpec] = [`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 75:
Kode:                limits=UsageLimits(240, None, 60)),
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 68 (`DEFAULT_DEVICES: List[DeviceSpec] = [`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 76:
Kode: ]
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 68 (`DEFAULT_DEVICES: List[DeviceSpec] = [`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 77:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 78:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 79:
Kode: def default_config() -> AppConfig:
Penjelasan: Mendefinisikan fungsi `default_config` dengan parameter: (tanpa parameter) dan tipe kembalian `AppConfig`. Tujuan: Mengembalikan konfigurasi default (salinan baru setiap dipanggil).

Line 80:
Kode:     """Mengembalikan konfigurasi default (salinan baru setiap dipanggil)."""
Penjelasan: Bagian docstring `default_config`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 81:
Kode:     return AppConfig(devices=list(DEFAULT_DEVICES))
Penjelasan: Mengembalikan hasil ekspresi `AppConfig(devices=list(DEFAULT_DEVICES))` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `default_config`, baris 79-81): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Mengembalikan konfigurasi default (salinan baru setiap dipanggil).

Line 82:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 83:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 84:
Kode: def validate_device_spec(spec: DeviceSpec) -> None:
Penjelasan: Mendefinisikan fungsi `validate_device_spec` dengan parameter: spec: DeviceSpec dan tipe kembalian `None`. Tujuan: Memeriksa satu spesifikasi perangkat.

Line 85:
Kode:     """Memeriksa satu spesifikasi perangkat.
Penjelasan: Bagian docstring `validate_device_spec`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 86:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 87:
Kode:     Raises:
Penjelasan: Bagian docstring `validate_device_spec`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 88:
Kode:         ValueError: nama kosong, kategori/kondisi tidak valid, daya negatif,
Penjelasan: Bagian docstring `validate_device_spec`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 89:
Kode:             atau batas penggunaan bukan bilangan bulat positif.
Penjelasan: Bagian docstring `validate_device_spec`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 90:
Kode:     """
Penjelasan: Bagian docstring `validate_device_spec`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 91:
Kode:     if not spec.name.strip():
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `not spec.name.strip()` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 92:
Kode:         raise ValueError("Nama perangkat tidak boleh kosong.")
Penjelasan: Melempar exception `ValueError("Nama perangkat tidak boleh kosong.")` untuk melaporkan kondisi tidak valid. Exception handling: menangani atau melaporkan kesalahan agar program tidak berhenti mendadak.

Line 93:
Kode:     if spec.category not in VALID_CATEGORIES:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `spec.category not in VALID_CATEGORIES` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 94:
Kode:         raise ValueError(f"Kategori tidak valid untuk {spec.name}: {spec.category!r}")
Penjelasan: Melempar exception `ValueError(f"Kategori tidak valid untuk {spec.name}: {spec.category!r}")` untuk melaporkan kondisi tidak valid. Exception handling: menangani atau melaporkan kesalahan agar program tidak berhenti mendadak.

Line 95:
Kode:     if spec.condition not in VALID_CONDITIONS:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `spec.condition not in VALID_CONDITIONS` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 96:
Kode:         raise ValueError(f"Kondisi tidak valid untuk {spec.name}: {spec.condition!r}")
Penjelasan: Melempar exception `ValueError(f"Kondisi tidak valid untuk {spec.name}: {spec.condition!r}")` untuk melaporkan kondisi tidak valid. Exception handling: menangani atau melaporkan kesalahan agar program tidak berhenti mendadak.

Line 97:
Kode:     if spec.power_w < 0:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `spec.power_w < 0` bernilai True.

Line 98:
Kode:         raise ValueError(f"Daya {spec.name} tidak boleh negatif.")
Penjelasan: Melempar exception `ValueError(f"Daya {spec.name} tidak boleh negatif.")` untuk melaporkan kondisi tidak valid. Exception handling: menangani atau melaporkan kesalahan agar program tidak berhenti mendadak.

Line 99:
Kode:     for label, value in (("max_daily_minutes", spec.limits.max_daily_minutes),
Penjelasan: Perulangan for: variabel `(label, value)` mengambil tiap elemen dari `(("max_daily_minutes", spec.limits.max_daily_minutes), ("max_daily_activations", spec.limits.max_daily_acti...`, dan blok di bawahnya diulang untuk tiap elemen.

Line 100:
Kode:                          ("max_daily_activations", spec.limits.max_daily_activations),
Penjelasan: Lanjutan header yang dimulai pada baris 99: bagian parameter/kondisi yang ditulis lebih dari satu baris.

Line 101:
Kode:                          ("inactivity_timeout_minutes", spec.limits.inactivity_timeout_minutes)):
Penjelasan: Lanjutan header yang dimulai pada baris 99: bagian parameter/kondisi yang ditulis lebih dari satu baris.

Line 102:
Kode:         if value is not None and (isinstance(value, bool) or not isinstance(value, int) or value <= 0):
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `value is not None and (isinstance(value, bool) or not isinstance(value, int) or value <= 0)` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 103:
Kode:             raise ValueError(f"{label} untuk {spec.name} harus bilangan bulat positif atau null.")
Penjelasan: Melempar exception `ValueError(f"{label} untuk {spec.name} harus bilangan bulat positif atau null.")` untuk melaporkan kondisi tidak valid. Exception handling: menangani atau melaporkan kesalahan agar program tidak berhenti mendadak.

Hubungan antarbaris (fungsi `validate_device_spec`, baris 84-103): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Memeriksa satu spesifikasi perangkat.

Line 104:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 105:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 106:
Kode: def validate_config(config: AppConfig) -> None:
Penjelasan: Mendefinisikan fungsi `validate_config` dengan parameter: config: AppConfig dan tipe kembalian `None`. Tujuan: Memeriksa seluruh konfigurasi (spesifikasi valid dan nama perangkat unik).

Line 107:
Kode:     """Memeriksa seluruh konfigurasi (spesifikasi valid dan nama perangkat unik)."""
Penjelasan: Bagian docstring `validate_config`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 108:
Kode:     names = [d.name.strip().lower() for d in config.devices]
Penjelasan: Menetapkan variabel `names` dengan nilai `[d.name.strip().lower() for d in config.devices]`.

Line 109:
Kode:     if len(names) != len(set(names)):
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `len(names) != len(set(names))` bernilai True.

Line 110:
Kode:         raise ValueError("Nama perangkat harus unik.")
Penjelasan: Melempar exception `ValueError("Nama perangkat harus unik.")` untuk melaporkan kondisi tidak valid. Exception handling: menangani atau melaporkan kesalahan agar program tidak berhenti mendadak.

Line 111:
Kode:     for spec in config.devices:
Penjelasan: Perulangan for: variabel `spec` mengambil tiap elemen dari `config.devices`, dan blok di bawahnya diulang untuk tiap elemen.

Line 112:
Kode:         validate_device_spec(spec)
Penjelasan: Memanggil `validate_device_spec(spec)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `validate_config`, baris 106-112): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Memeriksa seluruh konfigurasi (spesifikasi valid dan nama perangkat unik).

Line 113:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 114:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 115:
Kode: def config_to_dict(config: AppConfig) -> Dict[str, Any]:
Penjelasan: Mendefinisikan fungsi `config_to_dict` dengan parameter: config: AppConfig dan tipe kembalian `Dict[str, Any]`. Tujuan: Mengubah AppConfig menjadi dict yang dapat disimpan sebagai JSON.

Line 116:
Kode:     """Mengubah AppConfig menjadi dict yang dapat disimpan sebagai JSON."""
Penjelasan: Bagian docstring `config_to_dict`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 117:
Kode:     return {
Penjelasan: Mengembalikan hasil ekspresi `{ "shutdown_enabled": config.shutdown_enabled, "limits_enabled": config.limits_enabled, "devices": [ { "nam...` kepada pemanggil fungsi.

Line 118:
Kode:         "shutdown_enabled": config.shutdown_enabled,
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 117 (`return {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 119:
Kode:         "limits_enabled": config.limits_enabled,
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 117 (`return {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 120:
Kode:         "devices": [
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 117 (`return {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 121:
Kode:             {
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 117 (`return {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 122:
Kode:                 "name": d.name, "category": d.category, "power_w": d.power_w,
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 117 (`return {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 123:
Kode:                 "condition": d.condition,
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 117 (`return {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 124:
Kode:                 "limits": {
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 117 (`return {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 125:
Kode:                     "max_daily_minutes": d.limits.max_daily_minutes,
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 117 (`return {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 126:
Kode:                     "max_daily_activations": d.limits.max_daily_activations,
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 117 (`return {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 127:
Kode:                     "inactivity_timeout_minutes": d.limits.inactivity_timeout_minutes,
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 117 (`return {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 128:
Kode:                 },
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 117 (`return {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 129:
Kode:             }
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 117 (`return {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 130:
Kode:             for d in config.devices
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 117 (`return {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 131:
Kode:         ],
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 117 (`return {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 132:
Kode:     }
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 117 (`return {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Hubungan antarbaris (fungsi `config_to_dict`, baris 115-132): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Mengubah AppConfig menjadi dict yang dapat disimpan sebagai JSON.

Line 133:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 134:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 135:
Kode: def config_from_dict(data: Dict[str, Any]) -> AppConfig:
Penjelasan: Mendefinisikan fungsi `config_from_dict` dengan parameter: data: Dict[str, Any] dan tipe kembalian `AppConfig`. Tujuan: Membangun AppConfig dari dict JSON dan memvalidasinya.

Line 136:
Kode:     """Membangun AppConfig dari dict JSON dan memvalidasinya.
Penjelasan: Bagian docstring `config_from_dict`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 137:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 138:
Kode:     Raises:
Penjelasan: Bagian docstring `config_from_dict`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 139:
Kode:         ValueError: struktur atau nilai konfigurasi tidak valid.
Penjelasan: Bagian docstring `config_from_dict`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 140:
Kode:     """
Penjelasan: Bagian docstring `config_from_dict`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 141:
Kode:     try:
Penjelasan: Awal blok try: kode di bawahnya dijalankan dan kesalahan yang mungkin muncul ditangkap oleh blok except. Exception handling: menangani atau melaporkan kesalahan agar program tidak berhenti mendadak.

Line 142:
Kode:         devices = [
Penjelasan: Menetapkan variabel `devices` dengan nilai `[ DeviceSpec( name=str(item["name"]), category=str(item["category"]), power_w=float(item["power_w"]), condi...`.

Line 143:
Kode:             DeviceSpec(
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 142 (`devices = [`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 144:
Kode:                 name=str(item["name"]), category=str(item["category"]),
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 142 (`devices = [`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 145:
Kode:                 power_w=float(item["power_w"]), condition=item.get("condition"),
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 142 (`devices = [`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 146:
Kode:                 limits=UsageLimits(**item.get("limits", {})),
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 142 (`devices = [`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 147:
Kode:             )
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 142 (`devices = [`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 148:
Kode:             for item in data["devices"]
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 142 (`devices = [`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 149:
Kode:         ]
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 142 (`devices = [`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 150:
Kode:         config = AppConfig(devices, bool(data.get("shutdown_enabled", True)),
Penjelasan: Menetapkan variabel `config` dengan nilai `AppConfig(devices, bool(data.get("shutdown_enabled", True)), bool(data.get("limits_enabled", True)))`.

Line 151:
Kode:                            bool(data.get("limits_enabled", True)))
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 150 (`config = AppConfig(devices, bool(data.get("shutdown_enabl...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 152:
Kode:     except (KeyError, TypeError) as error:
Penjelasan: Penangkap kesalahan `except (KeyError, TypeError) as error:`: dijalankan bila blok try melempar exception yang sesuai, sehingga program tidak berhenti mendadak.

Line 153:
Kode:         raise ValueError(f"Struktur konfigurasi tidak valid: {error}") from error
Penjelasan: Melempar exception `ValueError(f"Struktur konfigurasi tidak valid: {error}")` untuk melaporkan kondisi tidak valid. Exception handling: menangani atau melaporkan kesalahan agar program tidak berhenti mendadak.

Line 154:
Kode:     validate_config(config)
Penjelasan: Memanggil `validate_config(config)` (hasilnya tidak disimpan; yang penting efeknya).

Line 155:
Kode:     return config
Penjelasan: Mengembalikan hasil ekspresi `config` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `config_from_dict`, baris 135-155): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Membangun AppConfig dari dict JSON dan memvalidasinya.

Line 156:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 157:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 158:
Kode: def load_config(path: Path = CONFIG_PATH) -> AppConfig:
Penjelasan: Mendefinisikan fungsi `load_config` dengan parameter: path: Path=CONFIG_PATH dan tipe kembalian `AppConfig`. Tujuan: Memuat konfigurasi dari JSON; jika file belum ada, memakai default.

Line 159:
Kode:     """Memuat konfigurasi dari JSON; jika file belum ada, memakai default.
Penjelasan: Bagian docstring `load_config`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 160:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 161:
Kode:     Raises:
Penjelasan: Bagian docstring `load_config`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 162:
Kode:         ValueError: file ada tetapi isinya bukan JSON/konfigurasi yang valid.
Penjelasan: Bagian docstring `load_config`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 163:
Kode:     """
Penjelasan: Bagian docstring `load_config`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 164:
Kode:     if not path.exists():
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `not path.exists()` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 165:
Kode:         return default_config()
Penjelasan: Mengembalikan hasil ekspresi `default_config()` kepada pemanggil fungsi.

Line 166:
Kode:     try:
Penjelasan: Awal blok try: kode di bawahnya dijalankan dan kesalahan yang mungkin muncul ditangkap oleh blok except. Exception handling: menangani atau melaporkan kesalahan agar program tidak berhenti mendadak.

Line 167:
Kode:         data = json.loads(path.read_text(encoding="utf-8"))
Penjelasan: Menetapkan variabel `data` dengan nilai `json.loads(path.read_text(encoding="utf-8"))`. File handling: membaca/menulis/menyiapkan file data (JSON atau CSV).

Line 168:
Kode:     except json.JSONDecodeError as error:
Penjelasan: Penangkap kesalahan `except json.JSONDecodeError as error:`: dijalankan bila blok try melempar exception yang sesuai, sehingga program tidak berhenti mendadak.

Line 169:
Kode:         raise ValueError(f"File konfigurasi bukan JSON valid: {error}") from error
Penjelasan: Melempar exception `ValueError(f"File konfigurasi bukan JSON valid: {error}")` untuk melaporkan kondisi tidak valid. Exception handling: menangani atau melaporkan kesalahan agar program tidak berhenti mendadak.

Line 170:
Kode:     return config_from_dict(data)
Penjelasan: Mengembalikan hasil ekspresi `config_from_dict(data)` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `load_config`, baris 158-170): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Memuat konfigurasi dari JSON; jika file belum ada, memakai default.

Line 171:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 172:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 173:
Kode: def save_config(config: AppConfig, path: Path = CONFIG_PATH) -> None:
Penjelasan: Mendefinisikan fungsi `save_config` dengan parameter: config: AppConfig, path: Path=CONFIG_PATH dan tipe kembalian `None`. Tujuan: Menyimpan konfigurasi ke JSON setelah divalidasi.

Line 174:
Kode:     """Menyimpan konfigurasi ke JSON setelah divalidasi."""
Penjelasan: Bagian docstring `save_config`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 175:
Kode:     validate_config(config)
Penjelasan: Memanggil `validate_config(config)` (hasilnya tidak disimpan; yang penting efeknya).

Line 176:
Kode:     path.parent.mkdir(parents=True, exist_ok=True)
Penjelasan: Memanggil `path.parent.mkdir(parents=True, exist_ok=True)` (hasilnya tidak disimpan; yang penting efeknya). File handling: membaca/menulis/menyiapkan file data (JSON atau CSV).

Line 177:
Kode:     path.write_text(json.dumps(config_to_dict(config), indent=2), encoding="utf-8")
Penjelasan: Memanggil `path.write_text(json.dumps(config_to_dict(config), indent=2), encoding="utf-8")` (hasilnya tidak disimpan; yang penting efeknya). File handling: membaca/menulis/menyiapkan file data (JSON atau CSV).

Hubungan antarbaris (fungsi `save_config`, baris 173-177): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Menyimpan konfigurasi ke JSON setelah divalidasi.

~~~~

## sensors.py

~~~~text
File: sensors.py

Line 1:
Kode: """Simulasi status sensor dan diagnostik sensor.
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 2:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 3:
Kode: Tujuan file:
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 4:
Kode:     Menyimpan keadaan sensor/kondisi rumah sebagai nilai Boolean yang diubah
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 5:
Kode:     oleh pengguna (tanpa perangkat keras), serta menghitung tiga diagnostik
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 6:
Kode:     memakai XOR, NOR, dan NAND.
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 7:
Kode: """
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 8:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 9:
Kode: from dataclasses import dataclass
Penjelasan: Mengimpor dataclass dari modul `dataclasses`.

Line 10:
Kode: from typing import Optional
Penjelasan: Mengimpor Optional dari modul `typing`.

Line 11:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 12:
Kode: from boolean_operations import boolean_nand, boolean_nor, boolean_not, boolean_xor
Penjelasan: Mengimpor boolean_nand, boolean_nor, boolean_not, boolean_xor dari modul `boolean_operations`.

Line 13:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 14:
Kode: TRUE_WORDS = {"1", "y", "yes", "ya", "on", "true", "t", "open", "detected", "dark", "gelap"}
Penjelasan: Menetapkan konstanta/variabel modul `TRUE_WORDS` dengan nilai `{"1", "y", "yes", "ya", "on", "true", "t", "open", "detected", "dark", "gelap"}`.

Line 15:
Kode: FALSE_WORDS = {"0", "n", "no", "tidak", "off", "false", "f", "closed", "close", "none",
Penjelasan: Menetapkan konstanta/variabel modul `FALSE_WORDS` dengan nilai `{"0", "n", "no", "tidak", "off", "false", "f", "closed", "close", "none", "light", "terang"}`.

Line 16:
Kode:                "light", "terang"}
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 15 (`FALSE_WORDS = {"0", "n", "no", "tidak", "off", "false", "...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 17:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 18:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 19:
Kode: @dataclass
Penjelasan: Dekorator `@dataclass`: memodifikasi class/fungsi di bawahnya (mis. membuat dataclass).

Line 20:
Kode: class SensorState:
Penjelasan: Mendefinisikan class `SensorState` dengan dekorator @dataclass. Tujuan: Keadaan seluruh sensor dan kondisi rumah (semua bool).

Line 21:
Kode:     """Keadaan seluruh sensor dan kondisi rumah (semua bool).
Penjelasan: Bagian docstring `SensorState`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 22:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 23:
Kode:     Attributes:
Penjelasan: Bagian docstring `SensorState`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 24:
Kode:         security_mode: mode keamanan aktif.
Penjelasan: Bagian docstring `SensorState`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 25:
Kode:         door_open: sensor pintu utama mendeteksi pintu terbuka.
Penjelasan: Bagian docstring `SensorState`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 26:
Kode:         door_open_redundant: sensor pintu redundan (hanya untuk diagnostik XOR).
Penjelasan: Bagian docstring `SensorState`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 27:
Kode:         motion_detected: sensor gerak mendeteksi gerakan.
Penjelasan: Bagian docstring `SensorState`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 28:
Kode:         motion_sensor_online: sensor gerak merespons uji diagnostik.
Penjelasan: Bagian docstring `SensorState`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 29:
Kode:         occupied: rumah/ruangan ditempati.
Penjelasan: Bagian docstring `SensorState`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 30:
Kode:         dark: ruangan gelap.
Penjelasan: Bagian docstring `SensorState`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 31:
Kode:         energy_saving_mode: mode hemat energi aktif.
Penjelasan: Bagian docstring `SensorState`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 32:
Kode:     """
Penjelasan: Bagian docstring `SensorState`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 33:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 34:
Kode:     security_mode: bool = False
Penjelasan: Mendeklarasikan atribut class `security_mode` bertipe `bool` dengan nilai awal `False`.

Line 35:
Kode:     door_open: bool = False
Penjelasan: Mendeklarasikan atribut class `door_open` bertipe `bool` dengan nilai awal `False`.

Line 36:
Kode:     door_open_redundant: bool = False
Penjelasan: Mendeklarasikan atribut class `door_open_redundant` bertipe `bool` dengan nilai awal `False`.

Line 37:
Kode:     motion_detected: bool = False
Penjelasan: Mendeklarasikan atribut class `motion_detected` bertipe `bool` dengan nilai awal `False`.

Line 38:
Kode:     motion_sensor_online: bool = True
Penjelasan: Mendeklarasikan atribut class `motion_sensor_online` bertipe `bool` dengan nilai awal `True`.

Line 39:
Kode:     occupied: bool = True
Penjelasan: Mendeklarasikan atribut class `occupied` bertipe `bool` dengan nilai awal `True`.

Line 40:
Kode:     dark: bool = False
Penjelasan: Mendeklarasikan atribut class `dark` bertipe `bool` dengan nilai awal `False`.

Line 41:
Kode:     energy_saving_mode: bool = False
Penjelasan: Mendeklarasikan atribut class `energy_saving_mode` bertipe `bool` dengan nilai awal `False`.

Hubungan antarbaris (class `SensorState`, baris 20-41): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Keadaan seluruh sensor dan kondisi rumah (semua bool).

Line 42:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 43:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 44:
Kode: def parse_bool(text: str) -> Optional[bool]:
Penjelasan: Mendefinisikan fungsi `parse_bool` dengan parameter: text: str dan tipe kembalian `Optional[bool]`. Tujuan: Mengubah teks pengguna menjadi bool.

Line 45:
Kode:     """Mengubah teks pengguna menjadi bool.
Penjelasan: Bagian docstring `parse_bool`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 46:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 47:
Kode:     Returns:
Penjelasan: Bagian docstring `parse_bool`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 48:
Kode:         True/False bila dikenali, None bila tidak dikenali (pemanggil menampilkan
Penjelasan: Bagian docstring `parse_bool`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 49:
Kode:         pesan kesalahan). Tidak melempar exception agar CLI tidak berhenti.
Penjelasan: Bagian docstring `parse_bool`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 50:
Kode:     """
Penjelasan: Bagian docstring `parse_bool`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 51:
Kode:     word = text.strip().lower()
Penjelasan: Menetapkan variabel `word` dengan nilai `text.strip().lower()`.

Line 52:
Kode:     if word in TRUE_WORDS:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `word in TRUE_WORDS` bernilai True.

Line 53:
Kode:         return True
Penjelasan: Mengembalikan hasil ekspresi `True` kepada pemanggil fungsi.

Line 54:
Kode:     if word in FALSE_WORDS:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `word in FALSE_WORDS` bernilai True.

Line 55:
Kode:         return False
Penjelasan: Mengembalikan hasil ekspresi `False` kepada pemanggil fungsi.

Line 56:
Kode:     return None
Penjelasan: Mengembalikan hasil ekspresi `None` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `parse_bool`, baris 44-56): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Mengubah teks pengguna menjadi bool.

Line 57:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 58:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 59:
Kode: def door_mismatch(state: SensorState) -> bool:
Penjelasan: Mendefinisikan fungsi `door_mismatch` dengan parameter: state: SensorState dan tipe kembalian `bool`. Tujuan: XOR: TRUE bila sensor pintu utama dan redundan memberi hasil BERBEDA.

Line 60:
Kode:     """XOR: TRUE bila sensor pintu utama dan redundan memberi hasil BERBEDA.
Penjelasan: Bagian docstring `door_mismatch`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 61:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 62:
Kode:     Ketidaksesuaian hanya tanda untuk diperiksa; tidak membuktikan sensor tertentu rusak.
Penjelasan: Bagian docstring `door_mismatch`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 63:
Kode:     """
Penjelasan: Bagian docstring `door_mismatch`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 64:
Kode:     return boolean_xor(state.door_open, state.door_open_redundant)
Penjelasan: Mengembalikan hasil ekspresi `boolean_xor(state.door_open, state.door_open_redundant)` kepada pemanggil fungsi. Ekspresi Boolean: memakai operator XOR dari boolean_operations.py.

Hubungan antarbaris (fungsi `door_mismatch`, baris 59-64): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: XOR: TRUE bila sensor pintu utama dan redundan memberi hasil BERBEDA.

Line 65:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 66:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 67:
Kode: def no_activity(state: SensorState) -> bool:
Penjelasan: Mendefinisikan fungsi `no_activity` dengan parameter: state: SensorState dan tipe kembalian `bool`. Tujuan: NOR: TRUE bila pintu tidak terbuka DAN tidak ada gerakan.

Line 68:
Kode:     """NOR: TRUE bila pintu tidak terbuka DAN tidak ada gerakan."""
Penjelasan: Bagian docstring `no_activity`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 69:
Kode:     return boolean_nor(state.door_open, state.motion_detected)
Penjelasan: Mengembalikan hasil ekspresi `boolean_nor(state.door_open, state.motion_detected)` kepada pemanggil fungsi. Ekspresi Boolean: memakai operator NOR dari boolean_operations.py.

Hubungan antarbaris (fungsi `no_activity`, baris 67-69): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: NOR: TRUE bila pintu tidak terbuka DAN tidak ada gerakan.

Line 70:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 71:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 72:
Kode: def diagnostics_incomplete(state: SensorState) -> bool:
Penjelasan: Mendefinisikan fungsi `diagnostics_incomplete` dengan parameter: state: SensorState dan tipe kembalian `bool`. Tujuan: NAND: TRUE bila TIDAK SEMUA kondisi diagnostik terpenuhi.

Line 73:
Kode:     """NAND: TRUE bila TIDAK SEMUA kondisi diagnostik terpenuhi.
Penjelasan: Bagian docstring `diagnostics_incomplete`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 74:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 75:
Kode:     Kondisi diagnostik: kedua sensor pintu konsisten DAN sensor gerak online.
Penjelasan: Bagian docstring `diagnostics_incomplete`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 76:
Kode:     """
Penjelasan: Bagian docstring `diagnostics_incomplete`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 77:
Kode:     door_consistent = boolean_not(door_mismatch(state))
Penjelasan: Menetapkan variabel `door_consistent` dengan nilai `boolean_not(door_mismatch(state))`. Ekspresi Boolean: memakai operator NOT dari boolean_operations.py.

Line 78:
Kode:     return boolean_nand(door_consistent, state.motion_sensor_online)
Penjelasan: Mengembalikan hasil ekspresi `boolean_nand(door_consistent, state.motion_sensor_online)` kepada pemanggil fungsi. Ekspresi Boolean: memakai operator NAND dari boolean_operations.py.

Hubungan antarbaris (fungsi `diagnostics_incomplete`, baris 72-78): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: NAND: TRUE bila TIDAK SEMUA kondisi diagnostik terpenuhi.

Line 79:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 80:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 81:
Kode: def describe_state(state: SensorState) -> str:
Penjelasan: Mendefinisikan fungsi `describe_state` dengan parameter: state: SensorState dan tipe kembalian `str`. Tujuan: Teks ringkas status sensor untuk ditampilkan di terminal.

Line 82:
Kode:     """Teks ringkas status sensor untuk ditampilkan di terminal."""
Penjelasan: Bagian docstring `describe_state`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 83:
Kode:     def onoff(value: bool, yes: str, no: str) -> str:
Penjelasan: Mendefinisikan fungsi `onoff` dengan parameter: value: bool, yes: str, no: str dan tipe kembalian `str`.

Line 84:
Kode:         return yes if value else no
Penjelasan: Mengembalikan hasil ekspresi `yes if value else no` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `onoff`, baris 83-84): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 85:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 86:
Kode:     return "\n".join([
Penjelasan: Mengembalikan hasil ekspresi `"\n".join([ f"Mode keamanan : {onoff(state.security_mode, 'ON', 'OFF')}", f"Sensor pintu utama : {onoff(sta...` kepada pemanggil fungsi.

Line 87:
Kode:         f"Mode keamanan        : {onoff(state.security_mode, 'ON', 'OFF')}",
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 86 (`return "\n".join([`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 88:
Kode:         f"Sensor pintu utama   : {onoff(state.door_open, 'OPEN', 'CLOSED')}",
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 86 (`return "\n".join([`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 89:
Kode:         f"Sensor pintu redundan: {onoff(state.door_open_redundant, 'OPEN', 'CLOSED')}",
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 86 (`return "\n".join([`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 90:
Kode:         f"Sensor gerak         : {onoff(state.motion_detected, 'DETECTED', 'NOT DETECTED')}",
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 86 (`return "\n".join([`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 91:
Kode:         f"Sensor gerak online  : {onoff(state.motion_sensor_online, 'YES', 'NO')}",
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 86 (`return "\n".join([`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 92:
Kode:         f"Ruangan ditempati    : {onoff(state.occupied, 'YES', 'NO')}",
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 86 (`return "\n".join([`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 93:
Kode:         f"Ruangan gelap        : {onoff(state.dark, 'YES', 'NO')}",
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 86 (`return "\n".join([`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 94:
Kode:         f"Mode hemat energi    : {onoff(state.energy_saving_mode, 'ON', 'OFF')}",
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 86 (`return "\n".join([`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 95:
Kode:     ])
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 86 (`return "\n".join([`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Hubungan antarbaris (fungsi `describe_state`, baris 81-95): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Teks ringkas status sensor untuk ditampilkan di terminal.

~~~~

## security.py

~~~~text
File: security.py

Line 1:
Kode: """Logika sistem keamanan.
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 2:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 3:
Kode: Tujuan file:
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 4:
Kode:     Menghitung status alarm dari mode keamanan, sensor pintu, dan sensor gerak,
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 5:
Kode:     lalu menjelaskan alasannya dalam kalimat.
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 6:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 7:
Kode: Rumus: alarm_active = security_mode AND (door_open OR motion_detected)
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 8:
Kode: """
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 9:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 10:
Kode: from dataclasses import dataclass
Penjelasan: Mengimpor dataclass dari modul `dataclasses`.

Line 11:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 12:
Kode: from boolean_operations import boolean_and, boolean_or
Penjelasan: Mengimpor boolean_and, boolean_or dari modul `boolean_operations`.

Line 13:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 14:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 15:
Kode: @dataclass(frozen=True)
Penjelasan: Dekorator `@dataclass(frozen=True)`: memodifikasi class/fungsi di bawahnya (mis. membuat dataclass).

Line 16:
Kode: class SecurityResult:
Penjelasan: Mendefinisikan class `SecurityResult` dengan dekorator @dataclass(frozen=True). Tujuan: Hasil evaluasi keamanan.

Line 17:
Kode:     """Hasil evaluasi keamanan.
Penjelasan: Bagian docstring `SecurityResult`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 18:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 19:
Kode:     Attributes:
Penjelasan: Bagian docstring `SecurityResult`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 20:
Kode:         alarm_active: status alarm hasil rumus.
Penjelasan: Bagian docstring `SecurityResult`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 21:
Kode:         activity_detected: hasil (door_open OR motion_detected).
Penjelasan: Bagian docstring `SecurityResult`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 22:
Kode:         reason: penjelasan alasan alarm aktif/tidak aktif.
Penjelasan: Bagian docstring `SecurityResult`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 23:
Kode:     """
Penjelasan: Bagian docstring `SecurityResult`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 24:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 25:
Kode:     alarm_active: bool
Penjelasan: Mendeklarasikan atribut class `alarm_active` bertipe `bool`.

Line 26:
Kode:     activity_detected: bool
Penjelasan: Mendeklarasikan atribut class `activity_detected` bertipe `bool`.

Line 27:
Kode:     reason: str
Penjelasan: Mendeklarasikan atribut class `reason` bertipe `str`.

Hubungan antarbaris (class `SecurityResult`, baris 16-27): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Hasil evaluasi keamanan.

Line 28:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 29:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 30:
Kode: def evaluate_security(security_mode: bool, door_open: bool, motion_detected: bool) -> SecurityResult:
Penjelasan: Mendefinisikan fungsi `evaluate_security` dengan parameter: security_mode: bool, door_open: bool, motion_detected: bool dan tipe kembalian `SecurityResult`. Tujuan: Mengevaluasi alarm.

Line 31:
Kode:     """Mengevaluasi alarm.
Penjelasan: Bagian docstring `evaluate_security`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 32:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 33:
Kode:     Langkah: (1) OR sensor -> activity_detected; (2) AND dengan security_mode ->
Penjelasan: Bagian docstring `evaluate_security`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 34:
Kode:     alarm_active. Urutan ini menjamin mode OFF selalu mematikan alarm.
Penjelasan: Bagian docstring `evaluate_security`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 35:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 36:
Kode:     Returns:
Penjelasan: Bagian docstring `evaluate_security`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 37:
Kode:         SecurityResult berisi status alarm dan alasan.
Penjelasan: Bagian docstring `evaluate_security`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 38:
Kode:     """
Penjelasan: Bagian docstring `evaluate_security`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 39:
Kode:     activity = boolean_or(door_open, motion_detected)
Penjelasan: Menetapkan variabel `activity` dengan nilai `boolean_or(door_open, motion_detected)`. Ekspresi Boolean: memakai operator OR dari boolean_operations.py.

Line 40:
Kode:     alarm = boolean_and(security_mode, activity)
Penjelasan: Menetapkan variabel `alarm` dengan nilai `boolean_and(security_mode, activity)`. Ekspresi Boolean: memakai operator AND dari boolean_operations.py.

Line 41:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 42:
Kode:     triggers = []
Penjelasan: Menetapkan variabel `triggers` dengan nilai `[]`.

Line 43:
Kode:     if door_open:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `door_open` bernilai True.

Line 44:
Kode:         triggers.append("pintu terbuka")
Penjelasan: Memanggil `triggers.append("pintu terbuka")` (hasilnya tidak disimpan; yang penting efeknya).

Line 45:
Kode:     if motion_detected:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `motion_detected` bernilai True.

Line 46:
Kode:         triggers.append("gerakan terdeteksi")
Penjelasan: Memanggil `triggers.append("gerakan terdeteksi")` (hasilnya tidak disimpan; yang penting efeknya).

Line 47:
Kode:     trigger_text = " dan ".join(triggers)
Penjelasan: Menetapkan variabel `trigger_text` dengan nilai `" dan ".join(triggers)`.

Line 48:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 49:
Kode:     if not security_mode:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `not security_mode` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 50:
Kode:         extra = f" (walau {trigger_text})" if activity else ""
Penjelasan: Menetapkan variabel `extra` dengan nilai `f" (walau {trigger_text})" if activity else ""`.

Line 51:
Kode:         reason = f"Alarm MATI: mode keamanan OFF{extra}, sehingga alarm tidak boleh aktif."
Penjelasan: Menetapkan variabel `reason` dengan nilai `f"Alarm MATI: mode keamanan OFF{extra}, sehingga alarm tidak boleh aktif."`.

Line 52:
Kode:     elif activity:
Penjelasan: Percabangan alternatif (elif): blok di bawahnya hanya dijalankan jika kondisi `activity` bernilai True.

Line 53:
Kode:         reason = f"Alarm AKTIF: mode keamanan ON dan {trigger_text}."
Penjelasan: Menetapkan variabel `reason` dengan nilai `f"Alarm AKTIF: mode keamanan ON dan {trigger_text}."`.

Line 54:
Kode:     else:
Penjelasan: Cabang else: dijalankan bila semua kondisi if/elif/for di atasnya tidak terpenuhi.

Line 55:
Kode:         reason = "Alarm MATI: mode keamanan ON tetapi pintu tertutup dan tidak ada gerakan."
Penjelasan: Menetapkan variabel `reason` dengan nilai `"Alarm MATI: mode keamanan ON tetapi pintu tertutup dan tidak ada gerakan."`.

Line 56:
Kode:     return SecurityResult(alarm, activity, reason)
Penjelasan: Mengembalikan hasil ekspresi `SecurityResult(alarm, activity, reason)` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `evaluate_security`, baris 30-56): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Mengevaluasi alarm.

~~~~

## lighting.py

~~~~text
File: lighting.py

Line 1:
Kode: """Otomatisasi lampu dan manual override.
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 2:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 3:
Kode: Tujuan file:
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 4:
Kode:     Menentukan status lampu dari tiga keadaan kontrol (AUTO, ON, OFF).
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 5:
Kode:     Kondisi otomatis memakai Boolean:  lamp_on = occupied AND dark
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 6:
Kode:     AUTO/ON/OFF adalah TIGA keadaan kontrol (bukan Boolean); Boolean dipakai
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 7:
Kode:     hanya untuk keputusan otomatis di dalam mode AUTO.
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 8:
Kode: """
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 9:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 10:
Kode: from dataclasses import dataclass
Penjelasan: Mengimpor dataclass dari modul `dataclasses`.

Line 11:
Kode: from enum import Enum
Penjelasan: Mengimpor Enum dari modul `enum`.

Line 12:
Kode: from typing import Optional
Penjelasan: Mengimpor Optional dari modul `typing`.

Line 13:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 14:
Kode: from boolean_operations import boolean_and
Penjelasan: Mengimpor boolean_and dari modul `boolean_operations`.

Line 15:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 16:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 17:
Kode: class LightingMode(Enum):
Penjelasan: Mendefinisikan class `LightingMode` turunan Enum. Tujuan: Mode pengendalian lampu.

Line 18:
Kode:     """Mode pengendalian lampu."""
Penjelasan: Bagian docstring `LightingMode`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 19:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 20:
Kode:     AUTO = "AUTO"
Penjelasan: Menetapkan variabel `AUTO` dengan nilai `"AUTO"`.

Line 21:
Kode:     ON = "ON"
Penjelasan: Menetapkan variabel `ON` dengan nilai `"ON"`.

Line 22:
Kode:     OFF = "OFF"
Penjelasan: Menetapkan variabel `OFF` dengan nilai `"OFF"`.

Hubungan antarbaris (class `LightingMode`, baris 17-22): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Mode pengendalian lampu.

Line 23:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 24:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 25:
Kode: @dataclass(frozen=True)
Penjelasan: Dekorator `@dataclass(frozen=True)`: memodifikasi class/fungsi di bawahnya (mis. membuat dataclass).

Line 26:
Kode: class LightingResult:
Penjelasan: Mendefinisikan class `LightingResult` dengan dekorator @dataclass(frozen=True). Tujuan: Hasil evaluasi lampu.

Line 27:
Kode:     """Hasil evaluasi lampu.
Penjelasan: Bagian docstring `LightingResult`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 28:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 29:
Kode:     Attributes:
Penjelasan: Bagian docstring `LightingResult`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 30:
Kode:         lamp_on: keputusan akhir lampu setelah mempertimbangkan override.
Penjelasan: Bagian docstring `LightingResult`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 31:
Kode:         auto_decision: hasil occupied AND dark (selalu dihitung, untuk perbandingan).
Penjelasan: Bagian docstring `LightingResult`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 32:
Kode:         reason: penjelasan keputusan.
Penjelasan: Bagian docstring `LightingResult`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 33:
Kode:     """
Penjelasan: Bagian docstring `LightingResult`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 34:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 35:
Kode:     lamp_on: bool
Penjelasan: Mendeklarasikan atribut class `lamp_on` bertipe `bool`.

Line 36:
Kode:     auto_decision: bool
Penjelasan: Mendeklarasikan atribut class `auto_decision` bertipe `bool`.

Line 37:
Kode:     reason: str
Penjelasan: Mendeklarasikan atribut class `reason` bertipe `str`.

Hubungan antarbaris (class `LightingResult`, baris 26-37): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Hasil evaluasi lampu.

Line 38:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 39:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 40:
Kode: def parse_lighting_mode(text: str) -> Optional[LightingMode]:
Penjelasan: Mendefinisikan fungsi `parse_lighting_mode` dengan parameter: text: str dan tipe kembalian `Optional[LightingMode]`. Tujuan: Mengubah teks (AUTO/ON/OFF atau 1/2/3) menjadi LightingMode; None bila tidak valid.

Line 41:
Kode:     """Mengubah teks (AUTO/ON/OFF atau 1/2/3) menjadi LightingMode; None bila tidak valid."""
Penjelasan: Bagian docstring `parse_lighting_mode`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 42:
Kode:     word = text.strip().upper()
Penjelasan: Menetapkan variabel `word` dengan nilai `text.strip().upper()`.

Line 43:
Kode:     aliases = {"1": LightingMode.AUTO, "2": LightingMode.ON, "3": LightingMode.OFF}
Penjelasan: Menetapkan variabel `aliases` dengan nilai `{"1": LightingMode.AUTO, "2": LightingMode.ON, "3": LightingMode.OFF}`.

Line 44:
Kode:     if word in aliases:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `word in aliases` bernilai True.

Line 45:
Kode:         return aliases[word]
Penjelasan: Mengembalikan hasil ekspresi `aliases[word]` kepada pemanggil fungsi.

Line 46:
Kode:     try:
Penjelasan: Awal blok try: kode di bawahnya dijalankan dan kesalahan yang mungkin muncul ditangkap oleh blok except. Exception handling: menangani atau melaporkan kesalahan agar program tidak berhenti mendadak.

Line 47:
Kode:         return LightingMode(word)
Penjelasan: Mengembalikan hasil ekspresi `LightingMode(word)` kepada pemanggil fungsi.

Line 48:
Kode:     except ValueError:
Penjelasan: Penangkap kesalahan `except ValueError:`: dijalankan bila blok try melempar exception yang sesuai, sehingga program tidak berhenti mendadak.

Line 49:
Kode:         return None
Penjelasan: Mengembalikan hasil ekspresi `None` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `parse_lighting_mode`, baris 40-49): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Mengubah teks (AUTO/ON/OFF atau 1/2/3) menjadi LightingMode; None bila tidak valid.

Line 50:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 51:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 52:
Kode: def evaluate_lighting(mode: LightingMode, occupied: bool, dark: bool) -> LightingResult:
Penjelasan: Mendefinisikan fungsi `evaluate_lighting` dengan parameter: mode: LightingMode, occupied: bool, dark: bool dan tipe kembalian `LightingResult`. Tujuan: Menentukan status lampu.

Line 53:
Kode:     """Menentukan status lampu.
Penjelasan: Bagian docstring `evaluate_lighting`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 54:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 55:
Kode:     Manual override (ON/OFF) berprioritas atas keputusan otomatis.
Penjelasan: Bagian docstring `evaluate_lighting`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 56:
Kode:     """
Penjelasan: Bagian docstring `evaluate_lighting`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 57:
Kode:     auto = boolean_and(occupied, dark)
Penjelasan: Menetapkan variabel `auto` dengan nilai `boolean_and(occupied, dark)`. Ekspresi Boolean: memakai operator AND dari boolean_operations.py.

Line 58:
Kode:     if mode is LightingMode.ON:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `mode is LightingMode.ON` bernilai True.

Line 59:
Kode:         return LightingResult(True, auto, "Lampu ON: mode ON memaksa lampu menyala (override manual).")
Penjelasan: Mengembalikan hasil ekspresi `LightingResult(True, auto, "Lampu ON: mode ON memaksa lampu menyala (override manual).")` kepada pemanggil fungsi.

Line 60:
Kode:     if mode is LightingMode.OFF:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `mode is LightingMode.OFF` bernilai True.

Line 61:
Kode:         return LightingResult(False, auto, "Lampu OFF: mode OFF memaksa lampu mati (override manual).")
Penjelasan: Mengembalikan hasil ekspresi `LightingResult(False, auto, "Lampu OFF: mode OFF memaksa lampu mati (override manual).")` kepada pemanggil fungsi.

Line 62:
Kode:     if auto:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `auto` bernilai True.

Line 63:
Kode:         return LightingResult(True, auto, "Lampu ON: mode AUTO, ruangan ditempati dan gelap.")
Penjelasan: Mengembalikan hasil ekspresi `LightingResult(True, auto, "Lampu ON: mode AUTO, ruangan ditempati dan gelap.")` kepada pemanggil fungsi.

Line 64:
Kode:     if not occupied and not dark:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `not occupied and not dark` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 65:
Kode:         why = "ruangan tidak ditempati dan tidak gelap"
Penjelasan: Menetapkan variabel `why` dengan nilai `"ruangan tidak ditempati dan tidak gelap"`.

Line 66:
Kode:     elif not occupied:
Penjelasan: Percabangan alternatif (elif): blok di bawahnya hanya dijalankan jika kondisi `not occupied` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 67:
Kode:         why = "ruangan tidak ditempati"
Penjelasan: Menetapkan variabel `why` dengan nilai `"ruangan tidak ditempati"`.

Line 68:
Kode:     else:
Penjelasan: Cabang else: dijalankan bila semua kondisi if/elif/for di atasnya tidak terpenuhi.

Line 69:
Kode:         why = "ruangan tidak gelap"
Penjelasan: Menetapkan variabel `why` dengan nilai `"ruangan tidak gelap"`.

Line 70:
Kode:     return LightingResult(False, auto, f"Lampu OFF: mode AUTO, {why}.")
Penjelasan: Mengembalikan hasil ekspresi `LightingResult(False, auto, f"Lampu OFF: mode AUTO, {why}.")` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `evaluate_lighting`, baris 52-70): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Menentukan status lampu.

~~~~

## appliances.py

~~~~text
File: appliances.py

Line 1:
Kode: """Pengelolaan perangkat rumah (status, hitungan waktu simulasi).
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 2:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 3:
Kode: Tujuan file:
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 4:
Kode:     Menyimpan keadaan tiap perangkat (ON/OFF, menit pemakaian, jumlah aktivasi,
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 5:
Kode:     menit tidak aktif) dan menyediakan operasi dasar. File ini TIDAK memutuskan
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 6:
Kode:     boleh/tidaknya perangkat menyala; keputusan itu milik energy_manager.py
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 7:
Kode:     (separation of concerns).
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 8:
Kode: """
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 9:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 10:
Kode: from dataclasses import dataclass
Penjelasan: Mengimpor dataclass dari modul `dataclasses`.

Line 11:
Kode: from typing import List, Sequence
Penjelasan: Mengimpor List, Sequence dari modul `typing`.

Line 12:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 13:
Kode: from config import DeviceSpec
Penjelasan: Mengimpor DeviceSpec dari modul `config`.

Line 14:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 15:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 16:
Kode: @dataclass
Penjelasan: Dekorator `@dataclass`: memodifikasi class/fungsi di bawahnya (mis. membuat dataclass).

Line 17:
Kode: class Appliance:
Penjelasan: Mendefinisikan class `Appliance` dengan dekorator @dataclass. Tujuan: Keadaan satu perangkat.

Line 18:
Kode:     """Keadaan satu perangkat.
Penjelasan: Bagian docstring `Appliance`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 19:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 20:
Kode:     Attributes:
Penjelasan: Bagian docstring `Appliance`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 21:
Kode:         spec: spesifikasi statis perangkat.
Penjelasan: Bagian docstring `Appliance`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 22:
Kode:         is_on: perangkat sedang menyala.
Penjelasan: Bagian docstring `Appliance`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 23:
Kode:         minutes_today: total menit ON pada hari simulasi ini.
Penjelasan: Bagian docstring `Appliance`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 24:
Kode:         activations_today: berapa kali perangkat dinyalakan hari ini.
Penjelasan: Bagian docstring `Appliance`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 25:
Kode:         idle_minutes: menit sejak aktivitas pengguna terakhir (hanya bertambah saat ON).
Penjelasan: Bagian docstring `Appliance`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 26:
Kode:     """
Penjelasan: Bagian docstring `Appliance`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 27:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 28:
Kode:     spec: DeviceSpec
Penjelasan: Mendeklarasikan atribut class `spec` bertipe `DeviceSpec`.

Line 29:
Kode:     is_on: bool = False
Penjelasan: Mendeklarasikan atribut class `is_on` bertipe `bool` dengan nilai awal `False`.

Line 30:
Kode:     minutes_today: int = 0
Penjelasan: Mendeklarasikan atribut class `minutes_today` bertipe `int` dengan nilai awal `0`.

Line 31:
Kode:     activations_today: int = 0
Penjelasan: Mendeklarasikan atribut class `activations_today` bertipe `int` dengan nilai awal `0`.

Line 32:
Kode:     idle_minutes: int = 0
Penjelasan: Mendeklarasikan atribut class `idle_minutes` bertipe `int` dengan nilai awal `0`.

Hubungan antarbaris (class `Appliance`, baris 17-32): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Keadaan satu perangkat.

Line 33:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 34:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 35:
Kode: class ApplianceManager:
Penjelasan: Mendefinisikan class `ApplianceManager`. Tujuan: Kumpulan perangkat dan operasi dasarnya.

Line 36:
Kode:     """Kumpulan perangkat dan operasi dasarnya."""
Penjelasan: Bagian docstring `ApplianceManager`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 37:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 38:
Kode:     def __init__(self, specs: Sequence[DeviceSpec]) -> None:
Penjelasan: Mendefinisikan fungsi `__init__` dengan parameter: self, specs: Sequence[DeviceSpec] dan tipe kembalian `None`. Tujuan: Membuat perangkat dari spesifikasi; semua awalnya OFF.

Line 39:
Kode:         """Membuat perangkat dari spesifikasi; semua awalnya OFF.
Penjelasan: Bagian docstring `__init__`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 40:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 41:
Kode:         Raises:
Penjelasan: Bagian docstring `__init__`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 42:
Kode:             ValueError: bila nama perangkat tidak unik.
Penjelasan: Bagian docstring `__init__`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 43:
Kode:         """
Penjelasan: Bagian docstring `__init__`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 44:
Kode:         names = [s.name.lower() for s in specs]
Penjelasan: Menetapkan variabel `names` dengan nilai `[s.name.lower() for s in specs]`.

Line 45:
Kode:         if len(names) != len(set(names)):
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `len(names) != len(set(names))` bernilai True.

Line 46:
Kode:             raise ValueError("Nama perangkat harus unik.")
Penjelasan: Melempar exception `ValueError("Nama perangkat harus unik.")` untuk melaporkan kondisi tidak valid. Exception handling: menangani atau melaporkan kesalahan agar program tidak berhenti mendadak.

Line 47:
Kode:         self.devices: List[Appliance] = [Appliance(spec) for spec in specs]
Penjelasan: Mendeklarasikan variabel `self.devices` bertipe `List[Appliance]` dengan nilai awal `[Appliance(spec) for spec in specs]`.

Hubungan antarbaris (fungsi `__init__`, baris 38-47): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Membuat perangkat dari spesifikasi; semua awalnya OFF.

Line 48:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 49:
Kode:     def find(self, key: str) -> Appliance:
Penjelasan: Mendefinisikan fungsi `find` dengan parameter: self, key: str dan tipe kembalian `Appliance`. Tujuan: Mencari perangkat berdasarkan nomor urut (mulai 1) atau nama (tak peka huruf besar).

Line 50:
Kode:         """Mencari perangkat berdasarkan nomor urut (mulai 1) atau nama (tak peka huruf besar).
Penjelasan: Bagian docstring `find`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 51:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 52:
Kode:         Raises:
Penjelasan: Bagian docstring `find`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 53:
Kode:             ValueError: bila tidak ditemukan.
Penjelasan: Bagian docstring `find`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 54:
Kode:         """
Penjelasan: Bagian docstring `find`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 55:
Kode:         text = key.strip()
Penjelasan: Menetapkan variabel `text` dengan nilai `key.strip()`.

Line 56:
Kode:         if text.isdigit():
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `text.isdigit()` bernilai True.

Line 57:
Kode:             index = int(text) - 1
Penjelasan: Menetapkan variabel `index` dengan nilai `int(text) - 1`.

Line 58:
Kode:             if 0 <= index < len(self.devices):
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `0 <= index < len(self.devices)` bernilai True.

Line 59:
Kode:                 return self.devices[index]
Penjelasan: Mengembalikan hasil ekspresi `self.devices[index]` kepada pemanggil fungsi.

Line 60:
Kode:         for device in self.devices:
Penjelasan: Perulangan for: variabel `device` mengambil tiap elemen dari `self.devices`, dan blok di bawahnya diulang untuk tiap elemen.

Line 61:
Kode:             if device.spec.name.lower() == text.lower():
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `device.spec.name.lower() == text.lower()` bernilai True.

Line 62:
Kode:                 return device
Penjelasan: Mengembalikan hasil ekspresi `device` kepada pemanggil fungsi.

Line 63:
Kode:         raise ValueError(f"Perangkat tidak ditemukan: {key!r}")
Penjelasan: Melempar exception `ValueError(f"Perangkat tidak ditemukan: {key!r}")` untuk melaporkan kondisi tidak valid. Exception handling: menangani atau melaporkan kesalahan agar program tidak berhenti mendadak.

Hubungan antarbaris (fungsi `find`, baris 49-63): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Mencari perangkat berdasarkan nomor urut (mulai 1) atau nama (tak peka huruf besar).

Line 64:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 65:
Kode:     def turn_on(self, key: str) -> bool:
Penjelasan: Mendefinisikan fungsi `turn_on` dengan parameter: self, key: str dan tipe kembalian `bool`. Tujuan: Menyalakan perangkat (operasi mentah, tanpa cek kebijakan).

Line 66:
Kode:         """Menyalakan perangkat (operasi mentah, tanpa cek kebijakan).
Penjelasan: Bagian docstring `turn_on`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 67:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 68:
Kode:         Returns:
Penjelasan: Bagian docstring `turn_on`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 69:
Kode:             True bila status berubah dari OFF ke ON. Penyalaan menambah
Penjelasan: Bagian docstring `turn_on`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 70:
Kode:             activations_today dan mereset idle_minutes (dianggap aktivitas baru).
Penjelasan: Bagian docstring `turn_on`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 71:
Kode:         """
Penjelasan: Bagian docstring `turn_on`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 72:
Kode:         device = self.find(key)
Penjelasan: Menetapkan variabel `device` dengan nilai `self.find(key)`.

Line 73:
Kode:         if device.is_on:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `device.is_on` bernilai True.

Line 74:
Kode:             return False
Penjelasan: Mengembalikan hasil ekspresi `False` kepada pemanggil fungsi.

Line 75:
Kode:         device.is_on = True
Penjelasan: Menetapkan variabel `device.is_on` dengan nilai `True`.

Line 76:
Kode:         device.activations_today += 1
Penjelasan: Memperbarui `device.activations_today` dengan operasi `Add` terhadap `1`.

Line 77:
Kode:         device.idle_minutes = 0
Penjelasan: Menetapkan variabel `device.idle_minutes` dengan nilai `0`.

Line 78:
Kode:         return True
Penjelasan: Mengembalikan hasil ekspresi `True` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `turn_on`, baris 65-78): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Menyalakan perangkat (operasi mentah, tanpa cek kebijakan).

Line 79:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 80:
Kode:     def turn_off(self, key: str) -> bool:
Penjelasan: Mendefinisikan fungsi `turn_off` dengan parameter: self, key: str dan tipe kembalian `bool`. Tujuan: Mematikan perangkat (operasi mentah). Returns True bila status berubah.

Line 81:
Kode:         """Mematikan perangkat (operasi mentah). Returns True bila status berubah."""
Penjelasan: Bagian docstring `turn_off`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 82:
Kode:         device = self.find(key)
Penjelasan: Menetapkan variabel `device` dengan nilai `self.find(key)`.

Line 83:
Kode:         if not device.is_on:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `not device.is_on` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 84:
Kode:             return False
Penjelasan: Mengembalikan hasil ekspresi `False` kepada pemanggil fungsi.

Line 85:
Kode:         device.is_on = False
Penjelasan: Menetapkan variabel `device.is_on` dengan nilai `False`.

Line 86:
Kode:         return True
Penjelasan: Mengembalikan hasil ekspresi `True` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `turn_off`, baris 80-86): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Mematikan perangkat (operasi mentah). Returns True bila status berubah.

Line 87:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 88:
Kode:     def touch(self, key: str) -> None:
Penjelasan: Mendefinisikan fungsi `touch` dengan parameter: self, key: str dan tipe kembalian `None`. Tujuan: Mencatat aktivitas pengguna pada perangkat (mereset idle_minutes).

Line 89:
Kode:         """Mencatat aktivitas pengguna pada perangkat (mereset idle_minutes)."""
Penjelasan: Bagian docstring `touch`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 90:
Kode:         self.find(key).idle_minutes = 0
Penjelasan: Menetapkan variabel `self.find(key).idle_minutes` dengan nilai `0`.

Hubungan antarbaris (fungsi `touch`, baris 88-90): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Mencatat aktivitas pengguna pada perangkat (mereset idle_minutes).

Line 91:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 92:
Kode:     def advance_minutes(self, minutes: int) -> None:
Penjelasan: Mendefinisikan fungsi `advance_minutes` dengan parameter: self, minutes: int dan tipe kembalian `None`. Tujuan: Memajukan waktu simulasi; perangkat ON menambah menit pakai dan menit tidak aktif.

Line 93:
Kode:         """Memajukan waktu simulasi; perangkat ON menambah menit pakai dan menit tidak aktif.
Penjelasan: Bagian docstring `advance_minutes`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 94:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 95:
Kode:         Raises:
Penjelasan: Bagian docstring `advance_minutes`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 96:
Kode:             ValueError: bila minutes bukan bilangan bulat tidak negatif.
Penjelasan: Bagian docstring `advance_minutes`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 97:
Kode:         """
Penjelasan: Bagian docstring `advance_minutes`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 98:
Kode:         if isinstance(minutes, bool) or not isinstance(minutes, int) or minutes < 0:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `isinstance(minutes, bool) or not isinstance(minutes, int) or minutes < 0` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 99:
Kode:             raise ValueError("Menit harus bilangan bulat tidak negatif.")
Penjelasan: Melempar exception `ValueError("Menit harus bilangan bulat tidak negatif.")` untuk melaporkan kondisi tidak valid. Exception handling: menangani atau melaporkan kesalahan agar program tidak berhenti mendadak.

Line 100:
Kode:         for device in self.devices:
Penjelasan: Perulangan for: variabel `device` mengambil tiap elemen dari `self.devices`, dan blok di bawahnya diulang untuk tiap elemen.

Line 101:
Kode:             if device.is_on:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `device.is_on` bernilai True.

Line 102:
Kode:                 device.minutes_today += minutes
Penjelasan: Memperbarui `device.minutes_today` dengan operasi `Add` terhadap `minutes`.

Line 103:
Kode:                 device.idle_minutes += minutes
Penjelasan: Memperbarui `device.idle_minutes` dengan operasi `Add` terhadap `minutes`.

Hubungan antarbaris (fungsi `advance_minutes`, baris 92-103): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Memajukan waktu simulasi; perangkat ON menambah menit pakai dan menit tidak aktif.

Line 104:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 105:
Kode:     def reset_day(self) -> None:
Penjelasan: Mendefinisikan fungsi `reset_day` dengan parameter: self dan tipe kembalian `None`. Tujuan: Memulai hari simulasi baru: semua penghitung harian di-nol-kan (status ON/OFF tetap).

Line 106:
Kode:         """Memulai hari simulasi baru: semua penghitung harian di-nol-kan (status ON/OFF tetap)."""
Penjelasan: Bagian docstring `reset_day`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 107:
Kode:         for device in self.devices:
Penjelasan: Perulangan for: variabel `device` mengambil tiap elemen dari `self.devices`, dan blok di bawahnya diulang untuk tiap elemen.

Line 108:
Kode:             device.minutes_today = 0
Penjelasan: Menetapkan variabel `device.minutes_today` dengan nilai `0`.

Line 109:
Kode:             device.activations_today = 0
Penjelasan: Menetapkan variabel `device.activations_today` dengan nilai `0`.

Line 110:
Kode:             device.idle_minutes = 0
Penjelasan: Menetapkan variabel `device.idle_minutes` dengan nilai `0`.

Hubungan antarbaris (fungsi `reset_day`, baris 105-110): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Memulai hari simulasi baru: semua penghitung harian di-nol-kan (status ON/OFF tetap).

~~~~

## energy_manager.py

~~~~text
File: energy_manager.py

Line 1:
Kode: """Kebijakan hemat energi dan perhitungan konsumsi.
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 2:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 3:
Kode: Tujuan file:
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 4:
Kode:     Menentukan apakah suatu perangkat boleh beroperasi (dengan alasan), serta
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 5:
Kode:     menghitung energi (kWh). Mengimplementasikan dua strategi:
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 6:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 7:
Kode:     Strategy 1 (Non-essential Shutdown):
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 8:
Kode:         nonessential_allowed = occupied AND NOT energy_saving_mode
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 9:
Kode:     Strategy 2 (Usage-based Restriction), semua hasil numerik dikonversi ke Boolean:
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 10:
Kode:         duration_limit_reached  = minutes_today >= max_daily_minutes
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 11:
Kode:         frequency_limit_reached = activations_today >= max_daily_activations
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 12:
Kode:         inactivity_exceeded     = idle_minutes >= inactivity_timeout_minutes
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 13:
Kode:         usage_blocked = duration OR frequency OR inactivity
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 14:
Kode:     Non-essential boleh ON = nonessential_allowed AND NOT usage_blocked
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 15:
Kode:     Essential tidak pernah dibatasi; Conditional mengikuti kondisinya sendiri.
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 16:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 17:
Kode:     Energi: kWh = Daya (W) x Waktu (jam) / 1000
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 18:
Kode: """
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 19:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 20:
Kode: from dataclasses import dataclass
Penjelasan: Mengimpor dataclass dari modul `dataclasses`.

Line 21:
Kode: from typing import List, Optional, Tuple
Penjelasan: Mengimpor List, Optional, Tuple dari modul `typing`.

Line 22:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 23:
Kode: from appliances import Appliance, ApplianceManager
Penjelasan: Mengimpor Appliance, ApplianceManager dari modul `appliances`.

Line 24:
Kode: from boolean_operations import boolean_and, boolean_not, boolean_or
Penjelasan: Mengimpor boolean_and, boolean_not, boolean_or dari modul `boolean_operations`.

Line 25:
Kode: from config import CATEGORY_CONDITIONAL, CATEGORY_ESSENTIAL
Penjelasan: Mengimpor CATEGORY_CONDITIONAL, CATEGORY_ESSENTIAL dari modul `config`.

Line 26:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 27:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 28:
Kode: @dataclass(frozen=True)
Penjelasan: Dekorator `@dataclass(frozen=True)`: memodifikasi class/fungsi di bawahnya (mis. membuat dataclass).

Line 29:
Kode: class Context:
Penjelasan: Mendefinisikan class `Context` dengan dekorator @dataclass(frozen=True). Tujuan: Kondisi rumah saat keputusan dibuat (semua bool).

Line 30:
Kode:     """Kondisi rumah saat keputusan dibuat (semua bool)."""
Penjelasan: Bagian docstring `Context`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 31:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 32:
Kode:     occupied: bool
Penjelasan: Mendeklarasikan atribut class `occupied` bertipe `bool`.

Line 33:
Kode:     energy_saving_mode: bool
Penjelasan: Mendeklarasikan atribut class `energy_saving_mode` bertipe `bool`.

Line 34:
Kode:     lamp_on: bool
Penjelasan: Mendeklarasikan atribut class `lamp_on` bertipe `bool`.

Hubungan antarbaris (class `Context`, baris 29-34): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Kondisi rumah saat keputusan dibuat (semua bool).

Line 35:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 36:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 37:
Kode: @dataclass(frozen=True)
Penjelasan: Dekorator `@dataclass(frozen=True)`: memodifikasi class/fungsi di bawahnya (mis. membuat dataclass).

Line 38:
Kode: class Decision:
Penjelasan: Mendefinisikan class `Decision` dengan dekorator @dataclass(frozen=True). Tujuan: Keputusan kebijakan: allowed + alasan dalam kalimat.

Line 39:
Kode:     """Keputusan kebijakan: allowed + alasan dalam kalimat."""
Penjelasan: Bagian docstring `Decision`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 40:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 41:
Kode:     allowed: bool
Penjelasan: Mendeklarasikan atribut class `allowed` bertipe `bool`.

Line 42:
Kode:     reason: str
Penjelasan: Mendeklarasikan atribut class `reason` bertipe `str`.

Hubungan antarbaris (class `Decision`, baris 38-42): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Keputusan kebijakan: allowed + alasan dalam kalimat.

Line 43:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 44:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 45:
Kode: @dataclass
Penjelasan: Dekorator `@dataclass`: memodifikasi class/fungsi di bawahnya (mis. membuat dataclass).

Line 46:
Kode: class EnergyPolicy:
Penjelasan: Mendefinisikan class `EnergyPolicy` dengan dekorator @dataclass. Tujuan: Saklar strategi: shutdown_enabled (Strategy 1), limits_enabled (Strategy 2).

Line 47:
Kode:     """Saklar strategi: shutdown_enabled (Strategy 1), limits_enabled (Strategy 2)."""
Penjelasan: Bagian docstring `EnergyPolicy`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 48:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 49:
Kode:     shutdown_enabled: bool = True
Penjelasan: Mendeklarasikan atribut class `shutdown_enabled` bertipe `bool` dengan nilai awal `True`.

Line 50:
Kode:     limits_enabled: bool = True
Penjelasan: Mendeklarasikan atribut class `limits_enabled` bertipe `bool` dengan nilai awal `True`.

Hubungan antarbaris (class `EnergyPolicy`, baris 46-50): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Saklar strategi: shutdown_enabled (Strategy 1), limits_enabled (Strategy 2).

Line 51:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 52:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 53:
Kode: def nonessential_allowed(context: Context, policy: EnergyPolicy) -> bool:
Penjelasan: Mendefinisikan fungsi `nonessential_allowed` dengan parameter: context: Context, policy: EnergyPolicy dan tipe kembalian `bool`. Tujuan: Strategy 1: occupied AND NOT energy_saving_mode (selalu TRUE bila strategi dimatikan).

Line 54:
Kode:     """Strategy 1: occupied AND NOT energy_saving_mode (selalu TRUE bila strategi dimatikan)."""
Penjelasan: Bagian docstring `nonessential_allowed`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 55:
Kode:     if not policy.shutdown_enabled:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `not policy.shutdown_enabled` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 56:
Kode:         return True
Penjelasan: Mengembalikan hasil ekspresi `True` kepada pemanggil fungsi.

Line 57:
Kode:     return boolean_and(context.occupied, boolean_not(context.energy_saving_mode))
Penjelasan: Mengembalikan hasil ekspresi `boolean_and(context.occupied, boolean_not(context.energy_saving_mode))` kepada pemanggil fungsi. Ekspresi Boolean: memakai operator AND, NOT dari boolean_operations.py.

Hubungan antarbaris (fungsi `nonessential_allowed`, baris 53-57): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Strategy 1: occupied AND NOT energy_saving_mode (selalu TRUE bila strategi dimatikan).

Line 58:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 59:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 60:
Kode: def condition_met(condition: Optional[str], context: Context) -> bool:
Penjelasan: Mendefinisikan fungsi `condition_met` dengan parameter: condition: Optional[str], context: Context dan tipe kembalian `bool`. Tujuan: Memeriksa kondisi operasi perangkat Conditional ("lamp", "occupied", atau None).

Line 61:
Kode:     """Memeriksa kondisi operasi perangkat Conditional ("lamp", "occupied", atau None).
Penjelasan: Bagian docstring `condition_met`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 62:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 63:
Kode:     Raises:
Penjelasan: Bagian docstring `condition_met`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 64:
Kode:         ValueError: kondisi tidak dikenal.
Penjelasan: Bagian docstring `condition_met`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 65:
Kode:     """
Penjelasan: Bagian docstring `condition_met`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 66:
Kode:     if condition is None:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `condition is None` bernilai True.

Line 67:
Kode:         return True
Penjelasan: Mengembalikan hasil ekspresi `True` kepada pemanggil fungsi.

Line 68:
Kode:     if condition == "lamp":
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `condition == "lamp"` bernilai True.

Line 69:
Kode:         return context.lamp_on
Penjelasan: Mengembalikan hasil ekspresi `context.lamp_on` kepada pemanggil fungsi.

Line 70:
Kode:     if condition == "occupied":
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `condition == "occupied"` bernilai True.

Line 71:
Kode:         return context.occupied
Penjelasan: Mengembalikan hasil ekspresi `context.occupied` kepada pemanggil fungsi.

Line 72:
Kode:     raise ValueError(f"Kondisi tidak dikenal: {condition!r}")
Penjelasan: Melempar exception `ValueError(f"Kondisi tidak dikenal: {condition!r}")` untuk melaporkan kondisi tidak valid. Exception handling: menangani atau melaporkan kesalahan agar program tidak berhenti mendadak.

Hubungan antarbaris (fungsi `condition_met`, baris 60-72): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Memeriksa kondisi operasi perangkat Conditional ("lamp", "occupied", atau None).

Line 73:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 74:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 75:
Kode: def usage_flags(device: Appliance, activation: bool) -> Tuple[bool, bool, bool]:
Penjelasan: Mendefinisikan fungsi `usage_flags` dengan parameter: device: Appliance, activation: bool dan tipe kembalian `Tuple[bool, bool, bool]`. Tujuan: Mengubah data numerik pemakaian menjadi tiga Boolean (durasi, frekuensi, inaktivitas).

Line 76:
Kode:     """Mengubah data numerik pemakaian menjadi tiga Boolean (durasi, frekuensi, inaktivitas).
Penjelasan: Bagian docstring `usage_flags`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 77:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 78:
Kode:     Args:
Penjelasan: Bagian docstring `usage_flags`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 79:
Kode:         device: perangkat yang dievaluasi.
Penjelasan: Bagian docstring `usage_flags`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 80:
Kode:         activation: TRUE bila evaluasi untuk PERMINTAAN menyalakan, FALSE bila perangkat sedang ON.
Penjelasan: Bagian docstring `usage_flags`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 81:
Kode:             Frekuensi hanya memblokir permintaan aktivasi baru; inaktivitas hanya relevan saat ON.
Penjelasan: Bagian docstring `usage_flags`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 82:
Kode:     """
Penjelasan: Bagian docstring `usage_flags`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 83:
Kode:     limits = device.spec.limits
Penjelasan: Menetapkan variabel `limits` dengan nilai `device.spec.limits`.

Line 84:
Kode:     duration = (limits.max_daily_minutes is not None
Penjelasan: Menetapkan variabel `duration` dengan nilai `limits.max_daily_minutes is not None and device.minutes_today >= limits.max_daily_minutes`. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 85:
Kode:                 and device.minutes_today >= limits.max_daily_minutes)
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 84 (`duration = (limits.max_daily_minutes is not None`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 86:
Kode:     frequency = (activation and limits.max_daily_activations is not None
Penjelasan: Menetapkan variabel `frequency` dengan nilai `activation and limits.max_daily_activations is not None and device.activations_today >= limits.max_daily_ac...`. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 87:
Kode:                  and device.activations_today >= limits.max_daily_activations)
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 86 (`frequency = (activation and limits.max_daily_activations ...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 88:
Kode:     inactivity = ((not activation) and limits.inactivity_timeout_minutes is not None
Penjelasan: Menetapkan variabel `inactivity` dengan nilai `(not activation) and limits.inactivity_timeout_minutes is not None and device.idle_minutes >= limits.inacti...`. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 89:
Kode:                   and device.idle_minutes >= limits.inactivity_timeout_minutes)
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 88 (`inactivity = ((not activation) and limits.inactivity_time...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 90:
Kode:     return duration, frequency, inactivity
Penjelasan: Mengembalikan hasil ekspresi `duration, frequency, inactivity` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `usage_flags`, baris 75-90): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Mengubah data numerik pemakaian menjadi tiga Boolean (durasi, frekuensi, inaktivitas).

Line 91:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 92:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 93:
Kode: def evaluate_device(device: Appliance, context: Context, policy: EnergyPolicy,
Penjelasan: Mendefinisikan fungsi `evaluate_device` dengan parameter: device: Appliance, context: Context, policy: EnergyPolicy, activation: bool dan tipe kembalian `Decision`. Tujuan: Memutuskan apakah perangkat boleh beroperasi, beserta alasannya.

Line 94:
Kode:                     activation: bool) -> Decision:
Penjelasan: Lanjutan header yang dimulai pada baris 93: bagian parameter/kondisi yang ditulis lebih dari satu baris.

Line 95:
Kode:     """Memutuskan apakah perangkat boleh beroperasi, beserta alasannya."""
Penjelasan: Bagian docstring `evaluate_device`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 96:
Kode:     category = device.spec.category
Penjelasan: Menetapkan variabel `category` dengan nilai `device.spec.category`.

Line 97:
Kode:     if category == CATEGORY_ESSENTIAL:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `category == CATEGORY_ESSENTIAL` bernilai True.

Line 98:
Kode:         return Decision(True, "Diizinkan: perangkat esensial dikecualikan dari kebijakan hemat energi.")
Penjelasan: Mengembalikan hasil ekspresi `Decision(True, "Diizinkan: perangkat esensial dikecualikan dari kebijakan hemat energi.")` kepada pemanggil fungsi.

Line 99:
Kode:     if category == CATEGORY_CONDITIONAL:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `category == CATEGORY_CONDITIONAL` bernilai True.

Line 100:
Kode:         if condition_met(device.spec.condition, context):
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `condition_met(device.spec.condition, context)` bernilai True.

Line 101:
Kode:             return Decision(True, f"Diizinkan: kondisi '{device.spec.condition}' terpenuhi.")
Penjelasan: Mengembalikan hasil ekspresi `Decision(True, f"Diizinkan: kondisi '{device.spec.condition}' terpenuhi.")` kepada pemanggil fungsi.

Line 102:
Kode:         return Decision(False, f"Tidak diizinkan: kondisi '{device.spec.condition}' tidak terpenuhi.")
Penjelasan: Mengembalikan hasil ekspresi `Decision(False, f"Tidak diizinkan: kondisi '{device.spec.condition}' tidak terpenuhi.")` kepada pemanggil fungsi.

Line 103:
Kode:     if not nonessential_allowed(context, policy):
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `not nonessential_allowed(context, policy)` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 104:
Kode:         return Decision(False, "Tidak diizinkan (Strategy 1): "
Penjelasan: Mengembalikan hasil ekspresi `Decision(False, "Tidak diizinkan (Strategy 1): " f"occupied={context.occupied}, energy_saving_mode={context...` kepada pemanggil fungsi.

Line 105:
Kode:                         f"occupied={context.occupied}, energy_saving_mode={context.energy_saving_mode}.")
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 104 (`return Decision(False, "Tidak diizinkan (Strategy 1): "`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 106:
Kode:     if policy.limits_enabled:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `policy.limits_enabled` bernilai True.

Line 107:
Kode:         duration, frequency, inactivity = usage_flags(device, activation)
Penjelasan: Menetapkan variabel `(duration, frequency, inactivity)` dengan nilai `usage_flags(device, activation)`.

Line 108:
Kode:         if boolean_or(boolean_or(duration, frequency), inactivity):
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `boolean_or(boolean_or(duration, frequency), inactivity)` bernilai True. Ekspresi Boolean: memakai operator OR dari boolean_operations.py.

Line 109:
Kode:             parts = []
Penjelasan: Menetapkan variabel `parts` dengan nilai `[]`.

Line 110:
Kode:             if duration:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `duration` bernilai True.

Line 111:
Kode:                 parts.append("batas durasi harian tercapai")
Penjelasan: Memanggil `parts.append("batas durasi harian tercapai")` (hasilnya tidak disimpan; yang penting efeknya).

Line 112:
Kode:             if frequency:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `frequency` bernilai True.

Line 113:
Kode:                 parts.append("batas frekuensi aktivasi tercapai")
Penjelasan: Memanggil `parts.append("batas frekuensi aktivasi tercapai")` (hasilnya tidak disimpan; yang penting efeknya).

Line 114:
Kode:             if inactivity:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `inactivity` bernilai True.

Line 115:
Kode:                 parts.append("inactivity timeout terlampaui")
Penjelasan: Memanggil `parts.append("inactivity timeout terlampaui")` (hasilnya tidak disimpan; yang penting efeknya).

Line 116:
Kode:             return Decision(False, "Tidak diizinkan (Strategy 2): " + ", ".join(parts) + ".")
Penjelasan: Mengembalikan hasil ekspresi `Decision(False, "Tidak diizinkan (Strategy 2): " + ", ".join(parts) + ".")` kepada pemanggil fungsi.

Line 117:
Kode:     return Decision(True, "Diizinkan: lolos Strategy 1 dan Strategy 2.")
Penjelasan: Mengembalikan hasil ekspresi `Decision(True, "Diizinkan: lolos Strategy 1 dan Strategy 2.")` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `evaluate_device`, baris 93-117): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Memutuskan apakah perangkat boleh beroperasi, beserta alasannya.

Line 118:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 119:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 120:
Kode: def enforce_policy(manager: ApplianceManager, context: Context, policy: EnergyPolicy) -> List[str]:
Penjelasan: Mendefinisikan fungsi `enforce_policy` dengan parameter: manager: ApplianceManager, context: Context, policy: EnergyPolicy dan tipe kembalian `List[str]`. Tujuan: Mematikan perangkat ON yang tidak lagi diizinkan.

Line 121:
Kode:     """Mematikan perangkat ON yang tidak lagi diizinkan.
Penjelasan: Bagian docstring `enforce_policy`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 122:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 123:
Kode:     Returns:
Penjelasan: Bagian docstring `enforce_policy`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 124:
Kode:         Daftar pesan untuk setiap perangkat yang dimatikan (Essential tidak pernah termasuk).
Penjelasan: Bagian docstring `enforce_policy`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 125:
Kode:     """
Penjelasan: Bagian docstring `enforce_policy`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 126:
Kode:     messages: List[str] = []
Penjelasan: Mendeklarasikan variabel `messages` bertipe `List[str]` dengan nilai awal `[]`.

Line 127:
Kode:     for device in manager.devices:
Penjelasan: Perulangan for: variabel `device` mengambil tiap elemen dari `manager.devices`, dan blok di bawahnya diulang untuk tiap elemen.

Line 128:
Kode:         if device.is_on:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `device.is_on` bernilai True.

Line 129:
Kode:             decision = evaluate_device(device, context, policy, activation=False)
Penjelasan: Menetapkan variabel `decision` dengan nilai `evaluate_device(device, context, policy, activation=False)`.

Line 130:
Kode:             if not decision.allowed:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `not decision.allowed` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 131:
Kode:                 manager.turn_off(device.spec.name)
Penjelasan: Memanggil `manager.turn_off(device.spec.name)` (hasilnya tidak disimpan; yang penting efeknya).

Line 132:
Kode:                 messages.append(f"{device.spec.name} dimatikan. {decision.reason}")
Penjelasan: Memanggil `messages.append(f"{device.spec.name} dimatikan. {decision.reason}")` (hasilnya tidak disimpan; yang penting efeknya).

Line 133:
Kode:     return messages
Penjelasan: Mengembalikan hasil ekspresi `messages` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `enforce_policy`, baris 120-133): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Mematikan perangkat ON yang tidak lagi diizinkan.

Line 134:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 135:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 136:
Kode: def request_turn_on(manager: ApplianceManager, key: str, context: Context,
Penjelasan: Mendefinisikan fungsi `request_turn_on` dengan parameter: manager: ApplianceManager, key: str, context: Context, policy: EnergyPolicy dan tipe kembalian `Decision`. Tujuan: Meminta menyalakan perangkat; hanya menyala bila kebijakan mengizinkan.

Line 137:
Kode:                     policy: EnergyPolicy) -> Decision:
Penjelasan: Lanjutan header yang dimulai pada baris 136: bagian parameter/kondisi yang ditulis lebih dari satu baris.

Line 138:
Kode:     """Meminta menyalakan perangkat; hanya menyala bila kebijakan mengizinkan."""
Penjelasan: Bagian docstring `request_turn_on`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 139:
Kode:     device = manager.find(key)
Penjelasan: Menetapkan variabel `device` dengan nilai `manager.find(key)`.

Line 140:
Kode:     if device.is_on:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `device.is_on` bernilai True.

Line 141:
Kode:         return Decision(True, "Perangkat sudah menyala.")
Penjelasan: Mengembalikan hasil ekspresi `Decision(True, "Perangkat sudah menyala.")` kepada pemanggil fungsi.

Line 142:
Kode:     decision = evaluate_device(device, context, policy, activation=True)
Penjelasan: Menetapkan variabel `decision` dengan nilai `evaluate_device(device, context, policy, activation=True)`.

Line 143:
Kode:     if decision.allowed:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `decision.allowed` bernilai True.

Line 144:
Kode:         manager.turn_on(device.spec.name)
Penjelasan: Memanggil `manager.turn_on(device.spec.name)` (hasilnya tidak disimpan; yang penting efeknya).

Line 145:
Kode:     return decision
Penjelasan: Mengembalikan hasil ekspresi `decision` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `request_turn_on`, baris 136-145): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Meminta menyalakan perangkat; hanya menyala bila kebijakan mengizinkan.

Line 146:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 147:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 148:
Kode: def energy_kwh(power_w: float, hours: float) -> float:
Penjelasan: Mendefinisikan fungsi `energy_kwh` dengan parameter: power_w: float, hours: float dan tipe kembalian `float`. Tujuan: Energi (kWh) = Daya (W) x Waktu (jam) / 1000.

Line 149:
Kode:     """Energi (kWh) = Daya (W) x Waktu (jam) / 1000.
Penjelasan: Bagian docstring `energy_kwh`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 150:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 151:
Kode:     Raises:
Penjelasan: Bagian docstring `energy_kwh`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 152:
Kode:         ValueError: daya atau jam negatif.
Penjelasan: Bagian docstring `energy_kwh`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 153:
Kode:     """
Penjelasan: Bagian docstring `energy_kwh`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 154:
Kode:     if power_w < 0 or hours < 0:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `power_w < 0 or hours < 0` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 155:
Kode:         raise ValueError("Daya dan waktu tidak boleh negatif.")
Penjelasan: Melempar exception `ValueError("Daya dan waktu tidak boleh negatif.")` untuk melaporkan kondisi tidak valid. Exception handling: menangani atau melaporkan kesalahan agar program tidak berhenti mendadak.

Line 156:
Kode:     return power_w * hours / 1000.0
Penjelasan: Mengembalikan hasil ekspresi `power_w * hours / 1000.0` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `energy_kwh`, baris 148-156): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Energi (kWh) = Daya (W) x Waktu (jam) / 1000.

Line 157:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 158:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 159:
Kode: def device_energy_kwh(device: Appliance) -> float:
Penjelasan: Mendefinisikan fungsi `device_energy_kwh` dengan parameter: device: Appliance dan tipe kembalian `float`. Tujuan: Energi hari simulasi satu perangkat; perangkat yang tidak pernah ON bernilai 0.

Line 160:
Kode:     """Energi hari simulasi satu perangkat; perangkat yang tidak pernah ON bernilai 0."""
Penjelasan: Bagian docstring `device_energy_kwh`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 161:
Kode:     return energy_kwh(device.spec.power_w, device.minutes_today / 60.0)
Penjelasan: Mengembalikan hasil ekspresi `energy_kwh(device.spec.power_w, device.minutes_today / 60.0)` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `device_energy_kwh`, baris 159-161): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Energi hari simulasi satu perangkat; perangkat yang tidak pernah ON bernilai 0.

Line 162:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 163:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 164:
Kode: def total_energy_kwh(manager: ApplianceManager) -> float:
Penjelasan: Mendefinisikan fungsi `total_energy_kwh` dengan parameter: manager: ApplianceManager dan tipe kembalian `float`. Tujuan: Total energi seluruh perangkat, termasuk perangkat esensial.

Line 165:
Kode:     """Total energi seluruh perangkat, termasuk perangkat esensial."""
Penjelasan: Bagian docstring `total_energy_kwh`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 166:
Kode:     return sum(device_energy_kwh(d) for d in manager.devices)
Penjelasan: Mengembalikan hasil ekspresi `sum(device_energy_kwh(d) for d in manager.devices)` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `total_energy_kwh`, baris 164-166): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Total energi seluruh perangkat, termasuk perangkat esensial.

Line 167:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 168:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 169:
Kode: def compute_savings(baseline_kwh: float, scenario_kwh: float) -> Tuple[float, float]:
Penjelasan: Mendefinisikan fungsi `compute_savings` dengan parameter: baseline_kwh: float, scenario_kwh: float dan tipe kembalian `Tuple[float, float]`. Tujuan: Penghematan (kWh) dan persentasenya terhadap baseline.

Line 170:
Kode:     """Penghematan (kWh) dan persentasenya terhadap baseline.
Penjelasan: Bagian docstring `compute_savings`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 171:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 172:
Kode:     Raises:
Penjelasan: Bagian docstring `compute_savings`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 173:
Kode:         ValueError: bila skenario memakai energi LEBIH BESAR dari baseline (indikasi logika salah),
Penjelasan: Bagian docstring `compute_savings`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 174:
Kode:             atau nilai negatif.
Penjelasan: Bagian docstring `compute_savings`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 175:
Kode:     """
Penjelasan: Bagian docstring `compute_savings`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 176:
Kode:     if baseline_kwh < 0 or scenario_kwh < 0:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `baseline_kwh < 0 or scenario_kwh < 0` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 177:
Kode:         raise ValueError("Energi tidak boleh negatif.")
Penjelasan: Melempar exception `ValueError("Energi tidak boleh negatif.")` untuk melaporkan kondisi tidak valid. Exception handling: menangani atau melaporkan kesalahan agar program tidak berhenti mendadak.

Line 178:
Kode:     if scenario_kwh > baseline_kwh + 1e-9:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `scenario_kwh > baseline_kwh + 1e-9` bernilai True.

Line 179:
Kode:         raise ValueError("Skenario otomatis memakai energi lebih besar dari baseline.")
Penjelasan: Melempar exception `ValueError("Skenario otomatis memakai energi lebih besar dari baseline.")` untuk melaporkan kondisi tidak valid. Exception handling: menangani atau melaporkan kesalahan agar program tidak berhenti mendadak.

Line 180:
Kode:     saving = baseline_kwh - scenario_kwh
Penjelasan: Menetapkan variabel `saving` dengan nilai `baseline_kwh - scenario_kwh`.

Line 181:
Kode:     percent = 0.0 if baseline_kwh == 0 else saving / baseline_kwh * 100.0
Penjelasan: Menetapkan variabel `percent` dengan nilai `0.0 if baseline_kwh == 0 else saving / baseline_kwh * 100.0`.

Line 182:
Kode:     return saving, percent
Penjelasan: Mengembalikan hasil ekspresi `saving, percent` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `compute_savings`, baris 169-182): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Penghematan (kWh) dan persentasenya terhadap baseline.

Line 183:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 184:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 185:
Kode: def percent_change(baseline_kwh: float, scenario_kwh: float) -> float:
Penjelasan: Mendefinisikan fungsi `percent_change` dengan parameter: baseline_kwh: float, scenario_kwh: float dan tipe kembalian `float`. Tujuan: Persentase perubahan konsumsi: (skenario - baseline) / baseline x 100 (negatif = lebih hemat).

Line 186:
Kode:     """Persentase perubahan konsumsi: (skenario - baseline) / baseline x 100 (negatif = lebih hemat)."""
Penjelasan: Bagian docstring `percent_change`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 187:
Kode:     if baseline_kwh == 0:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `baseline_kwh == 0` bernilai True.

Line 188:
Kode:         return 0.0
Penjelasan: Mengembalikan hasil ekspresi `0.0` kepada pemanggil fungsi.

Line 189:
Kode:     return (scenario_kwh - baseline_kwh) / baseline_kwh * 100.0
Penjelasan: Mengembalikan hasil ekspresi `(scenario_kwh - baseline_kwh) / baseline_kwh * 100.0` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `percent_change`, baris 185-189): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Persentase perubahan konsumsi: (skenario - baseline) / baseline x 100 (negatif = lebih hemat).

~~~~

## research.py

~~~~text
File: research.py

Line 1:
Kode: """Mini research: tiga eksperimen dan penyimpanan CSV.
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 2:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 3:
Kode: Tujuan file:
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 4:
Kode:     Experiment 1: validasi enam operator Boolean terhadap referensi aritmetika 0/1.
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 5:
Kode:     Experiment 2: delapan kombinasi skenario keamanan.
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 6:
Kode:     Experiment 3: simulasi energi sehari (1440 menit) pada tiga skenario.
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 7:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 8:
Kode: DATA ASUMSI  : daya perangkat, batas penggunaan (config.py) dan profil jam di bawah.
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 9:
Kode: INPUT SIMULASI: profil hunian, gelap, dan kebiasaan pengguna per jam (konstanta di bawah).
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 10:
Kode: HASIL PENGUJIAN: hanya nilai yang dihasilkan fungsi di file ini saat dijalankan.
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 11:
Kode: Semua hasil energi adalah SIMULASI, bukan pengukuran listrik nyata.
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 12:
Kode: """
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 13:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 14:
Kode: import csv
Penjelasan: Mengimpor modul: csv.

Line 15:
Kode: from dataclasses import dataclass
Penjelasan: Mengimpor dataclass dari modul `dataclasses`.

Line 16:
Kode: from itertools import product
Penjelasan: Mengimpor product dari modul `itertools`.

Line 17:
Kode: from pathlib import Path
Penjelasan: Mengimpor Path dari modul `pathlib`.

Line 18:
Kode: from typing import Dict, List, Optional, Set, Tuple
Penjelasan: Mengimpor Dict, List, Optional, Set, Tuple dari modul `typing`.

Line 19:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 20:
Kode: from appliances import ApplianceManager
Penjelasan: Mengimpor ApplianceManager dari modul `appliances`.

Line 21:
Kode: from boolean_operations import OPERATOR_NAMES, evaluate_operator, input_combinations, reference_result
Penjelasan: Mengimpor OPERATOR_NAMES, evaluate_operator, input_combinations, reference_result dari modul `boolean_operations`.

Line 22:
Kode: from config import CATEGORY_NON_ESSENTIAL, CSV_PATH, AppConfig, default_config
Penjelasan: Mengimpor CATEGORY_NON_ESSENTIAL, CSV_PATH, AppConfig, default_config dari modul `config`.

Line 23:
Kode: from energy_manager import (Context, EnergyPolicy, compute_savings, device_energy_kwh,
Penjelasan: Mengimpor Context, EnergyPolicy, compute_savings, device_energy_kwh, enforce_policy, percent_change, request_turn_on, total_energy_kwh dari modul `energy_manager`.

Line 24:
Kode:                             enforce_policy, percent_change, request_turn_on, total_energy_kwh)
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 23 (`from energy_manager import (Context, EnergyPolicy, comput...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 25:
Kode: from lighting import LightingMode, evaluate_lighting
Penjelasan: Mengimpor LightingMode, evaluate_lighting dari modul `lighting`.

Line 26:
Kode: from security import evaluate_security
Penjelasan: Mengimpor evaluate_security dari modul `security`.

Line 27:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 28:
Kode: MINUTES_PER_DAY = 1440
Penjelasan: Menetapkan konstanta/variabel modul `MINUTES_PER_DAY` dengan nilai `1440`.

Line 29:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 30:
Kode: # --- INPUT SIMULASI (asumsi profil satu hari) ---
Penjelasan: Komentar: penjelasan untuk pembaca, tidak dieksekusi Python.

Line 31:
Kode: OCCUPIED_HOURS: Set[int] = set(range(0, 8)) | set(range(18, 24))   # rumah kosong jam 08-17
Penjelasan: Mendeklarasikan variabel `OCCUPIED_HOURS` bertipe `Set[int]` dengan nilai awal `set(range(0, 8)) | set(range(18, 24))`.

Line 32:
Kode: DARK_HOURS: Set[int] = set(range(0, 6)) | set(range(18, 24))       # gelap jam 18-05
Penjelasan: Mendeklarasikan variabel `DARK_HOURS` bertipe `Set[int]` dengan nilai awal `set(range(0, 6)) | set(range(18, 24))`.

Line 33:
Kode: ECO_HOURS: Set[int] = set(range(0, 6))                              # mode hemat aktif jam 00-05
Penjelasan: Mendeklarasikan variabel `ECO_HOURS` bertipe `Set[int]` dengan nilai awal `set(range(0, 6))`.

Line 34:
Kode: USER_WANTS_HOURS: Dict[str, Set[int]] = {                           # kebiasaan tanpa otomatisasi
Penjelasan: Mendeklarasikan variabel `USER_WANTS_HOURS` bertipe `Dict[str, Set[int]]` dengan nilai awal `{ # kebiasaan tanpa otomatisasi "Refrigerator": set(range(0, 24)), "Main Lighting": set(range(17, 24)) | se...`.

Line 35:
Kode:     "Refrigerator": set(range(0, 24)),
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 34 (`USER_WANTS_HOURS: Dict[str, Set[int]] = { # kebiasaan tan...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 36:
Kode:     "Main Lighting": set(range(17, 24)) | set(range(0, 8)),
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 34 (`USER_WANTS_HOURS: Dict[str, Set[int]] = { # kebiasaan tan...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 37:
Kode:     "Fan": set(range(10, 24)),
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 34 (`USER_WANTS_HOURS: Dict[str, Set[int]] = { # kebiasaan tan...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 38:
Kode:     "Television": set(range(12, 24)),
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 34 (`USER_WANTS_HOURS: Dict[str, Set[int]] = { # kebiasaan tan...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 39:
Kode:     "Decorative Lighting": set(range(17, 24)) | set(range(0, 3)),
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 34 (`USER_WANTS_HOURS: Dict[str, Set[int]] = { # kebiasaan tan...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 40:
Kode: }
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 34 (`USER_WANTS_HOURS: Dict[str, Set[int]] = { # kebiasaan tan...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 41:
Kode: INTERACTION_INTERVAL_MINUTES: Dict[str, int] = {"Television": 30}   # pengguna menyentuh TV tiap 30 menit
Penjelasan: Mendeklarasikan variabel `INTERACTION_INTERVAL_MINUTES` bertipe `Dict[str, int]` dengan nilai awal `{"Television": 30}`.

Line 42:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 43:
Kode: # Ekspektasi manual untuk Experiment 2: (security_mode, door_open, motion_detected) -> alarm.
Penjelasan: Komentar: penjelasan untuk pembaca, tidak dieksekusi Python.

Line 44:
Kode: EXPECTED_ALARM: Dict[Tuple[bool, bool, bool], bool] = {
Penjelasan: Mendeklarasikan variabel `EXPECTED_ALARM` bertipe `Dict[Tuple[bool, bool, bool], bool]` dengan nilai awal `{ (False, False, False): False, (False, False, True): False, (False, True, False): False, (False, True, Tru...`.

Line 45:
Kode:     (False, False, False): False, (False, False, True): False,
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 44 (`EXPECTED_ALARM: Dict[Tuple[bool, bool, bool], bool] = {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 46:
Kode:     (False, True, False): False, (False, True, True): False,
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 44 (`EXPECTED_ALARM: Dict[Tuple[bool, bool, bool], bool] = {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 47:
Kode:     (True, False, False): False, (True, False, True): True,
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 44 (`EXPECTED_ALARM: Dict[Tuple[bool, bool, bool], bool] = {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 48:
Kode:     (True, True, False): True, (True, True, True): True,
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 44 (`EXPECTED_ALARM: Dict[Tuple[bool, bool, bool], bool] = {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 49:
Kode: }
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 44 (`EXPECTED_ALARM: Dict[Tuple[bool, bool, bool], bool] = {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 50:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 51:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 52:
Kode: @dataclass(frozen=True)
Penjelasan: Dekorator `@dataclass(frozen=True)`: memodifikasi class/fungsi di bawahnya (mis. membuat dataclass).

Line 53:
Kode: class Scenario:
Penjelasan: Mendefinisikan class `Scenario` dengan dekorator @dataclass(frozen=True). Tujuan: Pengaturan satu skenario energi (automation, shutdown, limits, saving).

Line 54:
Kode:     """Pengaturan satu skenario energi (automation, shutdown, limits, saving)."""
Penjelasan: Bagian docstring `Scenario`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 55:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 56:
Kode:     name: str
Penjelasan: Mendeklarasikan atribut class `name` bertipe `str`.

Line 57:
Kode:     automation: bool
Penjelasan: Mendeklarasikan atribut class `automation` bertipe `bool`.

Line 58:
Kode:     shutdown: bool
Penjelasan: Mendeklarasikan atribut class `shutdown` bertipe `bool`.

Line 59:
Kode:     limits: bool
Penjelasan: Mendeklarasikan atribut class `limits` bertipe `bool`.

Line 60:
Kode:     saving: bool
Penjelasan: Mendeklarasikan atribut class `saving` bertipe `bool`.

Hubungan antarbaris (class `Scenario`, baris 53-60): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Pengaturan satu skenario energi (automation, shutdown, limits, saving).

Line 61:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 62:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 63:
Kode: SCENARIOS: Tuple[Scenario, ...] = (
Penjelasan: Mendeklarasikan variabel `SCENARIOS` bertipe `Tuple[Scenario, ...]` dengan nilai awal `( Scenario("A_tanpa_otomatisasi", False, False, False, False), Scenario("B_otomatisasi", True, True, False,...`.

Line 64:
Kode:     Scenario("A_tanpa_otomatisasi", False, False, False, False),
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 63 (`SCENARIOS: Tuple[Scenario, ...] = (`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 65:
Kode:     Scenario("B_otomatisasi", True, True, False, False),
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 63 (`SCENARIOS: Tuple[Scenario, ...] = (`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 66:
Kode:     Scenario("C_otomatisasi_hemat_dan_batas", True, True, True, True),
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 63 (`SCENARIOS: Tuple[Scenario, ...] = (`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 67:
Kode: )
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 63 (`SCENARIOS: Tuple[Scenario, ...] = (`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 68:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 69:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 70:
Kode: @dataclass(frozen=True)
Penjelasan: Dekorator `@dataclass(frozen=True)`: memodifikasi class/fungsi di bawahnya (mis. membuat dataclass).

Line 71:
Kode: class ScenarioResult:
Penjelasan: Mendefinisikan class `ScenarioResult` dengan dekorator @dataclass(frozen=True). Tujuan: Hasil simulasi satu skenario: baris per perangkat (nama, menit ON, kWh) dan total kWh.

Line 72:
Kode:     """Hasil simulasi satu skenario: baris per perangkat (nama, menit ON, kWh) dan total kWh."""
Penjelasan: Bagian docstring `ScenarioResult`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 73:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 74:
Kode:     scenario: Scenario
Penjelasan: Mendeklarasikan atribut class `scenario` bertipe `Scenario`.

Line 75:
Kode:     rows: Tuple[Tuple[str, int, float], ...]
Penjelasan: Mendeklarasikan atribut class `rows` bertipe `Tuple[Tuple[str, int, float], ...]`.

Line 76:
Kode:     total_kwh: float
Penjelasan: Mendeklarasikan atribut class `total_kwh` bertipe `float`.

Hubungan antarbaris (class `ScenarioResult`, baris 71-76): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Hasil simulasi satu skenario: baris per perangkat (nama, menit ON, kWh) dan total kWh.

Line 77:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 78:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 79:
Kode: def run_experiment_1() -> List[Tuple[str, int, int, float]]:
Penjelasan: Mendefinisikan fungsi `run_experiment_1` dengan parameter: (tanpa parameter) dan tipe kembalian `List[Tuple[str, int, int, float]]`. Tujuan: Validasi Boolean. Returns daftar (operator, total, benar, akurasi%).

Line 80:
Kode:     """Validasi Boolean. Returns daftar (operator, total, benar, akurasi%)."""
Penjelasan: Bagian docstring `run_experiment_1`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 81:
Kode:     results = []
Penjelasan: Menetapkan variabel `results` dengan nilai `[]`.

Line 82:
Kode:     for name in OPERATOR_NAMES:
Penjelasan: Perulangan for: variabel `name` mengambil tiap elemen dari `OPERATOR_NAMES`, dan blok di bawahnya diulang untuk tiap elemen.

Line 83:
Kode:         total = correct = 0
Penjelasan: Menetapkan variabel `total, correct` dengan nilai `0`.

Line 84:
Kode:         for inputs in input_combinations(name):
Penjelasan: Perulangan for: variabel `inputs` mengambil tiap elemen dari `input_combinations(name)`, dan blok di bawahnya diulang untuk tiap elemen.

Line 85:
Kode:             total += 1
Penjelasan: Memperbarui `total` dengan operasi `Add` terhadap `1`.

Line 86:
Kode:             if evaluate_operator(name, *inputs) == reference_result(name, inputs):
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `evaluate_operator(name, *inputs) == reference_result(name, inputs)` bernilai True.

Line 87:
Kode:                 correct += 1
Penjelasan: Memperbarui `correct` dengan operasi `Add` terhadap `1`.

Line 88:
Kode:         results.append((name, total, correct, correct / total * 100.0))
Penjelasan: Memanggil `results.append((name, total, correct, correct / total * 100.0))` (hasilnya tidak disimpan; yang penting efeknya).

Line 89:
Kode:     return results
Penjelasan: Mengembalikan hasil ekspresi `results` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `run_experiment_1`, baris 79-89): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Validasi Boolean. Returns daftar (operator, total, benar, akurasi%).

Line 90:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 91:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 92:
Kode: def run_experiment_2() -> List[Tuple[bool, bool, bool, bool, bool]]:
Penjelasan: Mendefinisikan fungsi `run_experiment_2` dengan parameter: (tanpa parameter) dan tipe kembalian `List[Tuple[bool, bool, bool, bool, bool]]`. Tujuan: Uji 8 kombinasi keamanan. Returns (mode, door, motion, ekspektasi, aktual).

Line 93:
Kode:     """Uji 8 kombinasi keamanan. Returns (mode, door, motion, ekspektasi, aktual)."""
Penjelasan: Bagian docstring `run_experiment_2`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 94:
Kode:     rows = []
Penjelasan: Menetapkan variabel `rows` dengan nilai `[]`.

Line 95:
Kode:     for mode, door, motion in product([False, True], repeat=3):
Penjelasan: Perulangan for: variabel `(mode, door, motion)` mengambil tiap elemen dari `product([False, True], repeat=3)`, dan blok di bawahnya diulang untuk tiap elemen.

Line 96:
Kode:         actual = evaluate_security(mode, door, motion).alarm_active
Penjelasan: Menetapkan variabel `actual` dengan nilai `evaluate_security(mode, door, motion).alarm_active`.

Line 97:
Kode:         rows.append((mode, door, motion, EXPECTED_ALARM[(mode, door, motion)], actual))
Penjelasan: Memanggil `rows.append((mode, door, motion, EXPECTED_ALARM[(mode, door, motion)], actual))` (hasilnya tidak disimpan; yang penting efeknya).

Line 98:
Kode:     return rows
Penjelasan: Mengembalikan hasil ekspresi `rows` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `run_experiment_2`, baris 92-98): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Uji 8 kombinasi keamanan. Returns (mode, door, motion, ekspektasi, aktual).

Line 99:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 100:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 101:
Kode: def simulate_day(scenario: Scenario, config: Optional[AppConfig] = None) -> ScenarioResult:
Penjelasan: Mendefinisikan fungsi `simulate_day` dengan parameter: scenario: Scenario, config: Optional[AppConfig]=None dan tipe kembalian `ScenarioResult`. Tujuan: Mensimulasikan satu hari menit demi menit memakai logika sistem yang sebenarnya.

Line 102:
Kode:     """Mensimulasikan satu hari menit demi menit memakai logika sistem yang sebenarnya.
Penjelasan: Bagian docstring `simulate_day`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 103:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 104:
Kode:     Skenario A: perangkat ON mengikuti kebiasaan pengguna tanpa kebijakan.
Penjelasan: Bagian docstring `simulate_day`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 105:
Kode:     Skenario B/C: permintaan penyalaan melewati request_turn_on dan enforce_policy.
Penjelasan: Bagian docstring `simulate_day`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 106:
Kode:     Permintaan Non-essential hanya dibuat di awal jam (pengguna menekan tombol).
Penjelasan: Bagian docstring `simulate_day`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 107:
Kode:     """
Penjelasan: Bagian docstring `simulate_day`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 108:
Kode:     cfg = config or default_config()
Penjelasan: Menetapkan variabel `cfg` dengan nilai `config or default_config()`. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 109:
Kode:     manager = ApplianceManager(cfg.devices)
Penjelasan: Menetapkan variabel `manager` dengan nilai `ApplianceManager(cfg.devices)`.

Line 110:
Kode:     policy = EnergyPolicy(scenario.shutdown, scenario.limits)
Penjelasan: Menetapkan variabel `policy` dengan nilai `EnergyPolicy(scenario.shutdown, scenario.limits)`.

Line 111:
Kode:     for minute in range(MINUTES_PER_DAY):
Penjelasan: Perulangan for: variabel `minute` mengambil tiap elemen dari `range(MINUTES_PER_DAY)`, dan blok di bawahnya diulang untuk tiap elemen.

Line 112:
Kode:         hour = minute // 60
Penjelasan: Menetapkan variabel `hour` dengan nilai `minute // 60`.

Line 113:
Kode:         occupied = hour in OCCUPIED_HOURS
Penjelasan: Menetapkan variabel `occupied` dengan nilai `hour in OCCUPIED_HOURS`.

Line 114:
Kode:         lamp_on = evaluate_lighting(LightingMode.AUTO, occupied, hour in DARK_HOURS).lamp_on
Penjelasan: Menetapkan variabel `lamp_on` dengan nilai `evaluate_lighting(LightingMode.AUTO, occupied, hour in DARK_HOURS).lamp_on`.

Line 115:
Kode:         context = Context(occupied, scenario.saving and hour in ECO_HOURS, lamp_on)
Penjelasan: Menetapkan variabel `context` dengan nilai `Context(occupied, scenario.saving and hour in ECO_HOURS, lamp_on)`. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 116:
Kode:         for device in manager.devices:
Penjelasan: Perulangan for: variabel `device` mengambil tiap elemen dari `manager.devices`, dan blok di bawahnya diulang untuk tiap elemen.

Line 117:
Kode:             name = device.spec.name
Penjelasan: Menetapkan variabel `name` dengan nilai `device.spec.name`.

Line 118:
Kode:             wants = hour in USER_WANTS_HOURS.get(name, set())
Penjelasan: Menetapkan variabel `wants` dengan nilai `hour in USER_WANTS_HOURS.get(name, set())`.

Line 119:
Kode:             if not scenario.automation:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `not scenario.automation` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 120:
Kode:                 if wants:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `wants` bernilai True.

Line 121:
Kode:                     manager.turn_on(name)
Penjelasan: Memanggil `manager.turn_on(name)` (hasilnya tidak disimpan; yang penting efeknya).

Line 122:
Kode:                 else:
Penjelasan: Cabang else: dijalankan bila semua kondisi if/elif/for di atasnya tidak terpenuhi.

Line 123:
Kode:                     manager.turn_off(name)
Penjelasan: Memanggil `manager.turn_off(name)` (hasilnya tidak disimpan; yang penting efeknya).

Line 124:
Kode:             elif wants and not device.is_on:
Penjelasan: Percabangan alternatif (elif): blok di bawahnya hanya dijalankan jika kondisi `wants and not device.is_on` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 125:
Kode:                 if device.spec.category != CATEGORY_NON_ESSENTIAL or minute % 60 == 0:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `device.spec.category != CATEGORY_NON_ESSENTIAL or minute % 60 == 0` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 126:
Kode:                     request_turn_on(manager, name, context, policy)
Penjelasan: Memanggil `request_turn_on(manager, name, context, policy)` (hasilnya tidak disimpan; yang penting efeknya).

Line 127:
Kode:             elif not wants and device.is_on:
Penjelasan: Percabangan alternatif (elif): blok di bawahnya hanya dijalankan jika kondisi `not wants and device.is_on` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 128:
Kode:                 manager.turn_off(name)
Penjelasan: Memanggil `manager.turn_off(name)` (hasilnya tidak disimpan; yang penting efeknya).

Line 129:
Kode:             elif device.is_on:
Penjelasan: Percabangan alternatif (elif): blok di bawahnya hanya dijalankan jika kondisi `device.is_on` bernilai True.

Line 130:
Kode:                 interval = INTERACTION_INTERVAL_MINUTES.get(name)
Penjelasan: Menetapkan variabel `interval` dengan nilai `INTERACTION_INTERVAL_MINUTES.get(name)`.

Line 131:
Kode:                 if interval and minute % interval == 0:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `interval and minute % interval == 0` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 132:
Kode:                     manager.touch(name)
Penjelasan: Memanggil `manager.touch(name)` (hasilnya tidak disimpan; yang penting efeknya).

Line 133:
Kode:         if scenario.automation:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `scenario.automation` bernilai True.

Line 134:
Kode:             enforce_policy(manager, context, policy)
Penjelasan: Memanggil `enforce_policy(manager, context, policy)` (hasilnya tidak disimpan; yang penting efeknya).

Line 135:
Kode:         manager.advance_minutes(1)
Penjelasan: Memanggil `manager.advance_minutes(1)` (hasilnya tidak disimpan; yang penting efeknya).

Line 136:
Kode:     rows = tuple((d.spec.name, d.minutes_today, device_energy_kwh(d)) for d in manager.devices)
Penjelasan: Menetapkan variabel `rows` dengan nilai `tuple((d.spec.name, d.minutes_today, device_energy_kwh(d)) for d in manager.devices)`.

Line 137:
Kode:     return ScenarioResult(scenario, rows, total_energy_kwh(manager))
Penjelasan: Mengembalikan hasil ekspresi `ScenarioResult(scenario, rows, total_energy_kwh(manager))` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `simulate_day`, baris 101-137): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Mensimulasikan satu hari menit demi menit memakai logika sistem yang sebenarnya.

Line 138:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 139:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 140:
Kode: def run_experiment_3(config: Optional[AppConfig] = None) -> List[ScenarioResult]:
Penjelasan: Mendefinisikan fungsi `run_experiment_3` dengan parameter: config: Optional[AppConfig]=None dan tipe kembalian `List[ScenarioResult]`. Tujuan: Menjalankan tiga skenario energi dan mengembalikan hasilnya.

Line 141:
Kode:     """Menjalankan tiga skenario energi dan mengembalikan hasilnya."""
Penjelasan: Bagian docstring `run_experiment_3`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 142:
Kode:     return [simulate_day(s, config) for s in SCENARIOS]
Penjelasan: Mengembalikan hasil ekspresi `[simulate_day(s, config) for s in SCENARIOS]` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `run_experiment_3`, baris 140-142): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Menjalankan tiga skenario energi dan mengembalikan hasilnya.

Line 143:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 144:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 145:
Kode: def format_experiment_1(results: List[Tuple[str, int, int, float]]) -> str:
Penjelasan: Mendefinisikan fungsi `format_experiment_1` dengan parameter: results: List[Tuple[str, int, int, float]] dan tipe kembalian `str`. Tujuan: Teks tabel hasil Experiment 1 termasuk akurasi keseluruhan.

Line 146:
Kode:     """Teks tabel hasil Experiment 1 termasuk akurasi keseluruhan."""
Penjelasan: Bagian docstring `format_experiment_1`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 147:
Kode:     lines = ["Operator | Total | Benar | Salah | Akurasi", "-" * 44]
Penjelasan: Menetapkan variabel `lines` dengan nilai `["Operator | Total | Benar | Salah | Akurasi", "-" * 44]`.

Line 148:
Kode:     for name, total, correct, accuracy in results:
Penjelasan: Perulangan for: variabel `(name, total, correct, accuracy)` mengambil tiap elemen dari `results`, dan blok di bawahnya diulang untuk tiap elemen.

Line 149:
Kode:         lines.append(f"{name:<8} | {total:>5} | {correct:>5} | {total - correct:>5} | {accuracy:6.1f}%")
Penjelasan: Memanggil `lines.append(f"{name:<8} | {total:>5} | {correct:>5} | {total - correct:>5} | {accuracy:6.1f}%")` (hasilnya tidak disimpan; yang penting efeknya).

Line 150:
Kode:     all_total = sum(r[1] for r in results)
Penjelasan: Menetapkan variabel `all_total` dengan nilai `sum(r[1] for r in results)`.

Line 151:
Kode:     all_correct = sum(r[2] for r in results)
Penjelasan: Menetapkan variabel `all_correct` dengan nilai `sum(r[2] for r in results)`.

Line 152:
Kode:     lines.append(f"TOTAL    | {all_total:>5} | {all_correct:>5} | {all_total - all_correct:>5} | "
Penjelasan: Memanggil `lines.append(f"TOTAL | {all_total:>5} | {all_correct:>5} | {all_total - all_correct:>5} | " f"{all_correct ...` (hasilnya tidak disimpan; yang penting efeknya).

Line 153:
Kode:                  f"{all_correct / all_total * 100:6.1f}%")
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 152 (`lines.append(f"TOTAL | {all_total:>5} | {all_correct:>5} ...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 154:
Kode:     return "\n".join(lines)
Penjelasan: Mengembalikan hasil ekspresi `"\n".join(lines)` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `format_experiment_1`, baris 145-154): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Teks tabel hasil Experiment 1 termasuk akurasi keseluruhan.

Line 155:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 156:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 157:
Kode: def format_experiment_2(rows: List[Tuple[bool, bool, bool, bool, bool]]) -> str:
Penjelasan: Mendefinisikan fungsi `format_experiment_2` dengan parameter: rows: List[Tuple[bool, bool, bool, bool, bool]] dan tipe kembalian `str`. Tujuan: Teks tabel hasil Experiment 2 (ekspektasi vs aktual).

Line 158:
Kode:     """Teks tabel hasil Experiment 2 (ekspektasi vs aktual)."""
Penjelasan: Bagian docstring `format_experiment_2`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 159:
Kode:     def t(v: bool) -> str:
Penjelasan: Mendefinisikan fungsi `t` dengan parameter: v: bool dan tipe kembalian `str`.

Line 160:
Kode:         return "1" if v else "0"
Penjelasan: Mengembalikan hasil ekspresi `"1" if v else "0"` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `t`, baris 159-160): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 161:
Kode:     lines = ["Mode Door Motion | Ekspektasi Aktual Status", "-" * 46]
Penjelasan: Menetapkan variabel `lines` dengan nilai `["Mode Door Motion | Ekspektasi Aktual Status", "-" * 46]`.

Line 162:
Kode:     for mode, door, motion, expected, actual in rows:
Penjelasan: Perulangan for: variabel `(mode, door, motion, expected, actual)` mengambil tiap elemen dari `rows`, dan blok di bawahnya diulang untuk tiap elemen.

Line 163:
Kode:         status = "PASS" if expected == actual else "FAIL"
Penjelasan: Menetapkan variabel `status` dengan nilai `"PASS" if expected == actual else "FAIL"`.

Line 164:
Kode:         lines.append(f"  {t(mode)}    {t(door)}     {t(motion)}   |     {t(expected)}        {t(actual)}    {status}")
Penjelasan: Memanggil `lines.append(f" {t(mode)} {t(door)} {t(motion)} | {t(expected)} {t(actual)} {status}")` (hasilnya tidak disimpan; yang penting efeknya).

Line 165:
Kode:     passed = sum(1 for r in rows if r[3] == r[4])
Penjelasan: Menetapkan variabel `passed` dengan nilai `sum(1 for r in rows if r[3] == r[4])`.

Line 166:
Kode:     lines.append(f"Lulus {passed}/{len(rows)} skenario")
Penjelasan: Memanggil `lines.append(f"Lulus {passed}/{len(rows)} skenario")` (hasilnya tidak disimpan; yang penting efeknya).

Line 167:
Kode:     return "\n".join(lines)
Penjelasan: Mengembalikan hasil ekspresi `"\n".join(lines)` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `format_experiment_2`, baris 157-167): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Teks tabel hasil Experiment 2 (ekspektasi vs aktual).

Line 168:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 169:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 170:
Kode: def format_experiment_3(results: List[ScenarioResult]) -> str:
Penjelasan: Mendefinisikan fungsi `format_experiment_3` dengan parameter: results: List[ScenarioResult] dan tipe kembalian `str`. Tujuan: Teks hasil Experiment 3 (SIMULASI, bukan pengukuran nyata).

Line 171:
Kode:     """Teks hasil Experiment 3 (SIMULASI, bukan pengukuran nyata)."""
Penjelasan: Bagian docstring `format_experiment_3`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 172:
Kode:     baseline = results[0].total_kwh
Penjelasan: Menetapkan variabel `baseline` dengan nilai `results[0].total_kwh`.

Line 173:
Kode:     lines = ["[SIMULASI - bukan pengukuran listrik nyata]"]
Penjelasan: Menetapkan variabel `lines` dengan nilai `["[SIMULASI - bukan pengukuran listrik nyata]"]`.

Line 174:
Kode:     for result in results:
Penjelasan: Perulangan for: variabel `result` mengambil tiap elemen dari `results`, dan blok di bawahnya diulang untuk tiap elemen.

Line 175:
Kode:         lines.append(f"\nSkenario {result.scenario.name}")
Penjelasan: Memanggil `lines.append(f"\nSkenario {result.scenario.name}")` (hasilnya tidak disimpan; yang penting efeknya).

Line 176:
Kode:         for name, minutes, kwh in result.rows:
Penjelasan: Perulangan for: variabel `(name, minutes, kwh)` mengambil tiap elemen dari `result.rows`, dan blok di bawahnya diulang untuk tiap elemen.

Line 177:
Kode:             lines.append(f"  {name:<20} {minutes:>5} menit ({minutes / 60:5.2f} jam)  {kwh:7.3f} kWh")
Penjelasan: Memanggil `lines.append(f" {name:<20} {minutes:>5} menit ({minutes / 60:5.2f} jam) {kwh:7.3f} kWh")` (hasilnya tidak disimpan; yang penting efeknya).

Line 178:
Kode:         lines.append(f"  {'TOTAL':<20} {'':>25}{result.total_kwh:7.3f} kWh")
Penjelasan: Memanggil `lines.append(f" {'TOTAL':<20} {'':>25}{result.total_kwh:7.3f} kWh")` (hasilnya tidak disimpan; yang penting efeknya).

Line 179:
Kode:         if result is not results[0]:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `result is not results[0]` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 180:
Kode:             saving, pct = compute_savings(baseline, result.total_kwh)
Penjelasan: Menetapkan variabel `(saving, pct)` dengan nilai `compute_savings(baseline, result.total_kwh)`.

Line 181:
Kode:             lines.append(f"  Penghematan vs A: {saving:.3f} kWh ({pct:.2f}%), "
Penjelasan: Memanggil `lines.append(f" Penghematan vs A: {saving:.3f} kWh ({pct:.2f}%), " f"perubahan konsumsi {percent_change(bas...` (hasilnya tidak disimpan; yang penting efeknya).

Line 182:
Kode:                          f"perubahan konsumsi {percent_change(baseline, result.total_kwh):+.2f}%")
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 181 (`lines.append(f" Penghematan vs A: {saving:.3f} kWh ({pct:...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 183:
Kode:     return "\n".join(lines)
Penjelasan: Mengembalikan hasil ekspresi `"\n".join(lines)` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `format_experiment_3`, baris 170-183): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Teks hasil Experiment 3 (SIMULASI, bukan pengukuran nyata).

Line 184:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 185:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 186:
Kode: def build_csv_rows(exp1, exp2, exp3: List[ScenarioResult]) -> List[List[str]]:
Penjelasan: Mendefinisikan fungsi `build_csv_rows` dengan parameter: exp1, exp2, exp3: List[ScenarioResult] dan tipe kembalian `List[List[str]]`. Tujuan: Menyusun baris CSV format panjang: experiment, case, item, metric, value, unit, data_type.

Line 187:
Kode:     """Menyusun baris CSV format panjang: experiment, case, item, metric, value, unit, data_type."""
Penjelasan: Bagian docstring `build_csv_rows`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 188:
Kode:     rows: List[List[str]] = []
Penjelasan: Mendeklarasikan variabel `rows` bertipe `List[List[str]]` dengan nilai awal `[]`.

Line 189:
Kode:     for name, total, correct, accuracy in exp1:
Penjelasan: Perulangan for: variabel `(name, total, correct, accuracy)` mengambil tiap elemen dari `exp1`, dan blok di bawahnya diulang untuk tiap elemen.

Line 190:
Kode:         rows += [["1_boolean_validation", name, "all_inputs", "total_tests", str(total), "count", "hasil_pengujian"],
Penjelasan: Memperbarui `rows` dengan operasi `Add` terhadap `[["1_boolean_validation", name, "all_inputs", "total_tests", str(total), "count", "hasil_pengujian"], ["1_b...`.

Line 191:
Kode:                  ["1_boolean_validation", name, "all_inputs", "correct", str(correct), "count", "hasil_pengujian"],
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 190 (`rows += [["1_boolean_validation", name, "all_inputs", "to...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 192:
Kode:                  ["1_boolean_validation", name, "all_inputs", "accuracy", f"{accuracy:.1f}", "percent", "hasil_pengujian"]]
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 190 (`rows += [["1_boolean_validation", name, "all_inputs", "to...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 193:
Kode:     for mode, door, motion, expected, actual in exp2:
Penjelasan: Perulangan for: variabel `(mode, door, motion, expected, actual)` mengambil tiap elemen dari `exp2`, dan blok di bawahnya diulang untuk tiap elemen.

Line 194:
Kode:         case = f"mode={int(mode)};door={int(door)};motion={int(motion)}"
Penjelasan: Menetapkan variabel `case` dengan nilai `f"mode={int(mode)};door={int(door)};motion={int(motion)}"`.

Line 195:
Kode:         rows += [["2_security_scenarios", case, "alarm", "expected", str(int(expected)), "bool", "asumsi_ekspektasi"],
Penjelasan: Memperbarui `rows` dengan operasi `Add` terhadap `[["2_security_scenarios", case, "alarm", "expected", str(int(expected)), "bool", "asumsi_ekspektasi"], ["2_...`.

Line 196:
Kode:                  ["2_security_scenarios", case, "alarm", "actual", str(int(actual)), "bool", "hasil_pengujian"]]
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 195 (`rows += [["2_security_scenarios", case, "alarm", "expecte...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 197:
Kode:     baseline = exp3[0].total_kwh
Penjelasan: Menetapkan variabel `baseline` dengan nilai `exp3[0].total_kwh`.

Line 198:
Kode:     for result in exp3:
Penjelasan: Perulangan for: variabel `result` mengambil tiap elemen dari `exp3`, dan blok di bawahnya diulang untuk tiap elemen.

Line 199:
Kode:         for name, minutes, kwh in result.rows:
Penjelasan: Perulangan for: variabel `(name, minutes, kwh)` mengambil tiap elemen dari `result.rows`, dan blok di bawahnya diulang untuk tiap elemen.

Line 200:
Kode:             rows += [["3_energy_simulation", result.scenario.name, name, "on_minutes", str(minutes), "minute", "hasil_simulasi"],
Penjelasan: Memperbarui `rows` dengan operasi `Add` terhadap `[["3_energy_simulation", result.scenario.name, name, "on_minutes", str(minutes), "minute", "hasil_simulasi"...`.

Line 201:
Kode:                      ["3_energy_simulation", result.scenario.name, name, "energy", f"{kwh:.4f}", "kWh", "hasil_simulasi"]]
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 200 (`rows += [["3_energy_simulation", result.scenario.name, na...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 202:
Kode:         rows.append(["3_energy_simulation", result.scenario.name, "TOTAL", "energy", f"{result.total_kwh:.4f}", "kWh", "hasil_simulasi"])
Penjelasan: Memanggil `rows.append(["3_energy_simulation", result.scenario.name, "TOTAL", "energy", f"{result.total_kwh:.4f}", "kW...` (hasilnya tidak disimpan; yang penting efeknya).

Line 203:
Kode:         saving, pct = compute_savings(baseline, result.total_kwh)
Penjelasan: Menetapkan variabel `(saving, pct)` dengan nilai `compute_savings(baseline, result.total_kwh)`.

Line 204:
Kode:         rows += [["3_energy_simulation", result.scenario.name, "TOTAL", "saving_vs_A", f"{saving:.4f}", "kWh", "hasil_simulasi"],
Penjelasan: Memperbarui `rows` dengan operasi `Add` terhadap `[["3_energy_simulation", result.scenario.name, "TOTAL", "saving_vs_A", f"{saving:.4f}", "kWh", "hasil_simul...`.

Line 205:
Kode:                  ["3_energy_simulation", result.scenario.name, "TOTAL", "saving_percent", f"{pct:.2f}", "percent", "hasil_simulasi"]]
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 204 (`rows += [["3_energy_simulation", result.scenario.name, "T...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 206:
Kode:     for spec in default_config().devices:
Penjelasan: Perulangan for: variabel `spec` mengambil tiap elemen dari `default_config().devices`, dan blok di bawahnya diulang untuk tiap elemen.

Line 207:
Kode:         rows.append(["3_energy_simulation", "assumption", spec.name, "power", f"{spec.power_w:g}", "W", "asumsi"])
Penjelasan: Memanggil `rows.append(["3_energy_simulation", "assumption", spec.name, "power", f"{spec.power_w:g}", "W", "asumsi"])` (hasilnya tidak disimpan; yang penting efeknya).

Line 208:
Kode:     return rows
Penjelasan: Mengembalikan hasil ekspresi `rows` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `build_csv_rows`, baris 186-208): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Menyusun baris CSV format panjang: experiment, case, item, metric, value, unit, data_type.

Line 209:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 210:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 211:
Kode: def save_results_csv(exp1, exp2, exp3, path: Path = CSV_PATH) -> Path:
Penjelasan: Mendefinisikan fungsi `save_results_csv` dengan parameter: exp1, exp2, exp3, path: Path=CSV_PATH dan tipe kembalian `Path`. Tujuan: Menyimpan seluruh hasil eksperimen ke CSV dan mengembalikan path-nya.

Line 212:
Kode:     """Menyimpan seluruh hasil eksperimen ke CSV dan mengembalikan path-nya."""
Penjelasan: Bagian docstring `save_results_csv`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 213:
Kode:     path.parent.mkdir(parents=True, exist_ok=True)
Penjelasan: Memanggil `path.parent.mkdir(parents=True, exist_ok=True)` (hasilnya tidak disimpan; yang penting efeknya). File handling: membaca/menulis/menyiapkan file data (JSON atau CSV).

Line 214:
Kode:     with path.open("w", newline="", encoding="utf-8") as handle:
Penjelasan: Blok with: membuka konteks `path.open('w', newline='', encoding='utf-8') as handle` dan menutupnya otomatis setelah blok selesai. File handling: membaca/menulis/menyiapkan file data (JSON atau CSV).

Line 215:
Kode:         writer = csv.writer(handle)
Penjelasan: Menetapkan variabel `writer` dengan nilai `csv.writer(handle)`. File handling: membaca/menulis/menyiapkan file data (JSON atau CSV).

Line 216:
Kode:         writer.writerow(["experiment", "case", "item", "metric", "value", "unit", "data_type"])
Penjelasan: Memanggil `writer.writerow(["experiment", "case", "item", "metric", "value", "unit", "data_type"])` (hasilnya tidak disimpan; yang penting efeknya). File handling: membaca/menulis/menyiapkan file data (JSON atau CSV).

Line 217:
Kode:         writer.writerows(build_csv_rows(exp1, exp2, exp3))
Penjelasan: Memanggil `writer.writerows(build_csv_rows(exp1, exp2, exp3))` (hasilnya tidak disimpan; yang penting efeknya). File handling: membaca/menulis/menyiapkan file data (JSON atau CSV).

Line 218:
Kode:     return path
Penjelasan: Mengembalikan hasil ekspresi `path` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `save_results_csv`, baris 211-218): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Menyimpan seluruh hasil eksperimen ke CSV dan mengembalikan path-nya.

Line 219:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 220:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 221:
Kode: def run_all(config: Optional[AppConfig] = None, csv_path: Path = CSV_PATH) -> str:
Penjelasan: Mendefinisikan fungsi `run_all` dengan parameter: config: Optional[AppConfig]=None, csv_path: Path=CSV_PATH dan tipe kembalian `str`. Tujuan: Menjalankan ketiga eksperimen, menyimpan CSV, dan mengembalikan laporan teks.

Line 222:
Kode:     """Menjalankan ketiga eksperimen, menyimpan CSV, dan mengembalikan laporan teks."""
Penjelasan: Bagian docstring `run_all`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 223:
Kode:     exp1, exp2, exp3 = run_experiment_1(), run_experiment_2(), run_experiment_3(config)
Penjelasan: Menetapkan variabel `(exp1, exp2, exp3)` dengan nilai `run_experiment_1(), run_experiment_2(), run_experiment_3(config)`.

Line 224:
Kode:     saved = save_results_csv(exp1, exp2, exp3, csv_path)
Penjelasan: Menetapkan variabel `saved` dengan nilai `save_results_csv(exp1, exp2, exp3, csv_path)`.

Line 225:
Kode:     return "\n".join(["=== EXPERIMENT 1: Boolean Logic Validation ===", format_experiment_1(exp1),
Penjelasan: Mengembalikan hasil ekspresi `"\n".join(["=== EXPERIMENT 1: Boolean Logic Validation ===", format_experiment_1(exp1), "", "=== EXPERIMENT...` kepada pemanggil fungsi.

Line 226:
Kode:                       "", "=== EXPERIMENT 2: Security Scenario Testing ===", format_experiment_2(exp2),
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 225 (`return "\n".join(["=== EXPERIMENT 1: Boolean Logic Valida...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 227:
Kode:                       "", "=== EXPERIMENT 3: Energy Consumption Simulation ===", format_experiment_3(exp3),
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 225 (`return "\n".join(["=== EXPERIMENT 1: Boolean Logic Valida...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 228:
Kode:                       "", f"Hasil disimpan ke: {saved}"])
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 225 (`return "\n".join(["=== EXPERIMENT 1: Boolean Logic Valida...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Hubungan antarbaris (fungsi `run_all`, baris 221-228): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Menjalankan ketiga eksperimen, menyimpan CSV, dan mengembalikan laporan teks.

~~~~

## main.py

~~~~text
File: main.py

Line 1:
Kode: """Entry point CLI: navigasi menu dan integrasi seluruh modul.
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 2:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 3:
Kode: Jalankan dengan:  python main.py
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 4:
Kode: Semua input divalidasi; input salah menampilkan pesan dan meminta ulang.
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 5:
Kode: Mengetik 0 pada sub-menu kembali ke menu sebelumnya. Hasil energi adalah SIMULASI.
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 6:
Kode: """
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 7:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 8:
Kode: from typing import List, Optional
Penjelasan: Mengimpor List, Optional dari modul `typing`.

Line 9:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 10:
Kode: import research
Penjelasan: Mengimpor modul: research.

Line 11:
Kode: from appliances import ApplianceManager
Penjelasan: Mengimpor ApplianceManager dari modul `appliances`.

Line 12:
Kode: from boolean_operations import OPERATOR_NAMES, evaluate_operator, format_truth_table, operator_arity
Penjelasan: Mengimpor OPERATOR_NAMES, evaluate_operator, format_truth_table, operator_arity dari modul `boolean_operations`.

Line 13:
Kode: from config import (CATEGORY_ESSENTIAL, CONFIG_PATH, AppConfig, DeviceSpec, UsageLimits,
Penjelasan: Mengimpor CATEGORY_ESSENTIAL, CONFIG_PATH, AppConfig, DeviceSpec, UsageLimits, default_config, load_config, save_config, validate_device_spec dari modul `config`.

Line 14:
Kode:                     default_config, load_config, save_config, validate_device_spec)
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 13 (`from config import (CATEGORY_ESSENTIAL, CONFIG_PATH, AppC...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 15:
Kode: from energy_manager import (Context, EnergyPolicy, device_energy_kwh, enforce_policy,
Penjelasan: Mengimpor Context, EnergyPolicy, device_energy_kwh, enforce_policy, evaluate_device, nonessential_allowed, request_turn_on, total_energy_kwh dari modul `energy_manager`.

Line 16:
Kode:                             evaluate_device, nonessential_allowed, request_turn_on, total_energy_kwh)
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 15 (`from energy_manager import (Context, EnergyPolicy, device...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 17:
Kode: from lighting import LightingMode, evaluate_lighting, parse_lighting_mode
Penjelasan: Mengimpor LightingMode, evaluate_lighting, parse_lighting_mode dari modul `lighting`.

Line 18:
Kode: from security import evaluate_security
Penjelasan: Mengimpor evaluate_security dari modul `security`.

Line 19:
Kode: from sensors import (SensorState, describe_state, diagnostics_incomplete, door_mismatch,
Penjelasan: Mengimpor SensorState, describe_state, diagnostics_incomplete, door_mismatch, no_activity, parse_bool dari modul `sensors`.

Line 20:
Kode:                      no_activity, parse_bool)
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 19 (`from sensors import (SensorState, describe_state, diagnos...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 21:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 22:
Kode: LINE = "=" * 40
Penjelasan: Menetapkan konstanta/variabel modul `LINE` dengan nilai `"=" * 40`.

Line 23:
Kode: THIN = "-" * 40
Penjelasan: Menetapkan konstanta/variabel modul `THIN` dengan nilai `"-" * 40`.

Line 24:
Kode: FIELDS = {
Penjelasan: Menetapkan konstanta/variabel modul `FIELDS` dengan nilai `{ "security_mode": "Mode keamanan (ON/OFF)", "door_open": "Sensor pintu utama (OPEN/CLOSED)", "door_open_re...`.

Line 25:
Kode:     "security_mode": "Mode keamanan (ON/OFF)",
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 24 (`FIELDS = {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 26:
Kode:     "door_open": "Sensor pintu utama (OPEN/CLOSED)",
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 24 (`FIELDS = {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 27:
Kode:     "door_open_redundant": "Sensor pintu redundan (OPEN/CLOSED)",
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 24 (`FIELDS = {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 28:
Kode:     "motion_detected": "Sensor gerak (DETECTED/NOT DETECTED)",
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 24 (`FIELDS = {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 29:
Kode:     "motion_sensor_online": "Sensor gerak online (YES/NO)",
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 24 (`FIELDS = {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 30:
Kode:     "occupied": "Ruangan ditempati (YES/NO)",
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 24 (`FIELDS = {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 31:
Kode:     "dark": "Ruangan gelap (YES/NO)",
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 24 (`FIELDS = {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 32:
Kode:     "energy_saving_mode": "Mode hemat energi (ON/OFF)",
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 24 (`FIELDS = {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 33:
Kode: }
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 24 (`FIELDS = {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 34:
Kode: SECURITY_FIELDS = ["security_mode", "door_open", "motion_detected", "door_open_redundant"]
Penjelasan: Menetapkan konstanta/variabel modul `SECURITY_FIELDS` dengan nilai `["security_mode", "door_open", "motion_detected", "door_open_redundant"]`.

Line 35:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 36:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 37:
Kode: def title(text: str) -> None:
Penjelasan: Mendefinisikan fungsi `title` dengan parameter: text: str dan tipe kembalian `None`. Tujuan: Mencetak judul bagian dengan pemisah.

Line 38:
Kode:     """Mencetak judul bagian dengan pemisah."""
Penjelasan: Bagian docstring `title`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 39:
Kode:     print(f"\n{LINE}\n  {text}\n{LINE}")
Penjelasan: Memanggil `print(f"\n{LINE}\n {text}\n{LINE}")` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `title`, baris 37-39): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Mencetak judul bagian dengan pemisah.

Line 40:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 41:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 42:
Kode: def read_text(prompt: str) -> str:
Penjelasan: Mendefinisikan fungsi `read_text` dengan parameter: prompt: str dan tipe kembalian `str`. Tujuan: Membaca satu baris input. Saat input berakhir (EOF/Ctrl+C), program keluar dengan rapi.

Line 43:
Kode:     """Membaca satu baris input. Saat input berakhir (EOF/Ctrl+C), program keluar dengan rapi."""
Penjelasan: Bagian docstring `read_text`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 44:
Kode:     try:
Penjelasan: Awal blok try: kode di bawahnya dijalankan dan kesalahan yang mungkin muncul ditangkap oleh blok except. Exception handling: menangani atau melaporkan kesalahan agar program tidak berhenti mendadak.

Line 45:
Kode:         return input(prompt).strip()
Penjelasan: Mengembalikan hasil ekspresi `input(prompt).strip()` kepada pemanggil fungsi.

Line 46:
Kode:     except (EOFError, KeyboardInterrupt):
Penjelasan: Penangkap kesalahan `except (EOFError, KeyboardInterrupt):`: dijalankan bila blok try melempar exception yang sesuai, sehingga program tidak berhenti mendadak.

Line 47:
Kode:         print("\nInput dihentikan. Sampai jumpa.")
Penjelasan: Memanggil `print("\nInput dihentikan. Sampai jumpa.")` (hasilnya tidak disimpan; yang penting efeknya).

Line 48:
Kode:         raise SystemExit(0)
Penjelasan: Melempar exception `SystemExit(0)` untuk melaporkan kondisi tidak valid. Exception handling: menangani atau melaporkan kesalahan agar program tidak berhenti mendadak.

Hubungan antarbaris (fungsi `read_text`, baris 42-48): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Membaca satu baris input. Saat input berakhir (EOF/Ctrl+C), program keluar dengan rapi.

Line 49:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 50:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 51:
Kode: def read_choice(prompt: str, valid: List[str]) -> str:
Penjelasan: Mendefinisikan fungsi `read_choice` dengan parameter: prompt: str, valid: List[str] dan tipe kembalian `str`. Tujuan: Meminta pilihan sampai salah satu nilai valid dimasukkan.

Line 52:
Kode:     """Meminta pilihan sampai salah satu nilai valid dimasukkan."""
Penjelasan: Bagian docstring `read_choice`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 53:
Kode:     while True:
Penjelasan: Perulangan while: blok di bawahnya diulang selama `True` bernilai True.

Line 54:
Kode:         value = read_text(prompt)
Penjelasan: Menetapkan variabel `value` dengan nilai `read_text(prompt)`. File handling: membaca/menulis/menyiapkan file data (JSON atau CSV).

Line 55:
Kode:         if value in valid:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `value in valid` bernilai True.

Line 56:
Kode:             return value
Penjelasan: Mengembalikan hasil ekspresi `value` kepada pemanggil fungsi.

Line 57:
Kode:         print(f"Pilihan tidak valid. Pilih salah satu: {', '.join(valid)}")
Penjelasan: Memanggil `print(f"Pilihan tidak valid. Pilih salah satu: {', '.join(valid)}")` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `read_choice`, baris 51-57): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Meminta pilihan sampai salah satu nilai valid dimasukkan.

Line 58:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 59:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 60:
Kode: def read_bool(prompt: str) -> Optional[bool]:
Penjelasan: Mendefinisikan fungsi `read_bool` dengan parameter: prompt: str dan tipe kembalian `Optional[bool]`. Tujuan: Meminta nilai bool (mis. on/off, yes/no, open/closed). Kosong = batal (None).

Line 61:
Kode:     """Meminta nilai bool (mis. on/off, yes/no, open/closed). Kosong = batal (None)."""
Penjelasan: Bagian docstring `read_bool`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 62:
Kode:     while True:
Penjelasan: Perulangan while: blok di bawahnya diulang selama `True` bernilai True.

Line 63:
Kode:         value = read_text(prompt + " [kosong = batal]: ")
Penjelasan: Menetapkan variabel `value` dengan nilai `read_text(prompt + " [kosong = batal]: ")`. File handling: membaca/menulis/menyiapkan file data (JSON atau CSV).

Line 64:
Kode:         if value == "":
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `value == ""` bernilai True.

Line 65:
Kode:             return None
Penjelasan: Mengembalikan hasil ekspresi `None` kepada pemanggil fungsi.

Line 66:
Kode:         parsed = parse_bool(value)
Penjelasan: Menetapkan variabel `parsed` dengan nilai `parse_bool(value)`.

Line 67:
Kode:         if parsed is not None:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `parsed is not None` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 68:
Kode:             return parsed
Penjelasan: Mengembalikan hasil ekspresi `parsed` kepada pemanggil fungsi.

Line 69:
Kode:         print("Masukan tidak dikenali. Gunakan 1/0, on/off, yes/no, true/false, open/closed.")
Penjelasan: Memanggil `print("Masukan tidak dikenali. Gunakan 1/0, on/off, yes/no, true/false, open/closed.")` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `read_bool`, baris 60-69): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Meminta nilai bool (mis. on/off, yes/no, open/closed). Kosong = batal (None).

Line 70:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 71:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 72:
Kode: def read_int(prompt: str, minimum: int = 0) -> Optional[int]:
Penjelasan: Mendefinisikan fungsi `read_int` dengan parameter: prompt: str, minimum: int=0 dan tipe kembalian `Optional[int]`. Tujuan: Meminta bilangan bulat >= minimum. Kosong = batal (None).

Line 73:
Kode:     """Meminta bilangan bulat >= minimum. Kosong = batal (None)."""
Penjelasan: Bagian docstring `read_int`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 74:
Kode:     while True:
Penjelasan: Perulangan while: blok di bawahnya diulang selama `True` bernilai True.

Line 75:
Kode:         value = read_text(prompt + " [kosong = batal]: ")
Penjelasan: Menetapkan variabel `value` dengan nilai `read_text(prompt + " [kosong = batal]: ")`. File handling: membaca/menulis/menyiapkan file data (JSON atau CSV).

Line 76:
Kode:         if value == "":
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `value == ""` bernilai True.

Line 77:
Kode:             return None
Penjelasan: Mengembalikan hasil ekspresi `None` kepada pemanggil fungsi.

Line 78:
Kode:         if value.isdigit() and int(value) >= minimum:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `value.isdigit() and int(value) >= minimum` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 79:
Kode:             return int(value)
Penjelasan: Mengembalikan hasil ekspresi `int(value)` kepada pemanggil fungsi.

Line 80:
Kode:         print(f"Masukkan bilangan bulat >= {minimum}.")
Penjelasan: Memanggil `print(f"Masukkan bilangan bulat >= {minimum}.")` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `read_int`, baris 72-80): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Meminta bilangan bulat >= minimum. Kosong = batal (None).

Line 81:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 82:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 83:
Kode: class SmartHome:
Penjelasan: Mendefinisikan class `SmartHome`. Tujuan: Keadaan aplikasi: sensor, mode lampu, perangkat, dan kebijakan energi.

Line 84:
Kode:     """Keadaan aplikasi: sensor, mode lampu, perangkat, dan kebijakan energi."""
Penjelasan: Bagian docstring `SmartHome`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 85:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 86:
Kode:     def __init__(self, config: AppConfig) -> None:
Penjelasan: Mendefinisikan fungsi `__init__` dengan parameter: self, config: AppConfig dan tipe kembalian `None`. Tujuan: Membuat keadaan awal; perangkat Essential langsung ON.

Line 87:
Kode:         """Membuat keadaan awal; perangkat Essential langsung ON."""
Penjelasan: Bagian docstring `__init__`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 88:
Kode:         self.config = config
Penjelasan: Menetapkan variabel `self.config` dengan nilai `config`.

Line 89:
Kode:         self.state = SensorState()
Penjelasan: Menetapkan variabel `self.state` dengan nilai `SensorState()`.

Line 90:
Kode:         self.mode = LightingMode.AUTO
Penjelasan: Menetapkan variabel `self.mode` dengan nilai `LightingMode.AUTO`.

Line 91:
Kode:         self.manager = ApplianceManager(config.devices)
Penjelasan: Menetapkan variabel `self.manager` dengan nilai `ApplianceManager(config.devices)`.

Line 92:
Kode:         self.policy = EnergyPolicy(config.shutdown_enabled, config.limits_enabled)
Penjelasan: Menetapkan variabel `self.policy` dengan nilai `EnergyPolicy(config.shutdown_enabled, config.limits_enabled)`.

Line 93:
Kode:         for device in self.manager.devices:
Penjelasan: Perulangan for: variabel `device` mengambil tiap elemen dari `self.manager.devices`, dan blok di bawahnya diulang untuk tiap elemen.

Line 94:
Kode:             if device.spec.category == CATEGORY_ESSENTIAL:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `device.spec.category == CATEGORY_ESSENTIAL` bernilai True.

Line 95:
Kode:                 self.manager.turn_on(device.spec.name)
Penjelasan: Memanggil `self.manager.turn_on(device.spec.name)` (hasilnya tidak disimpan; yang penting efeknya).

Line 96:
Kode:         self.refresh()
Penjelasan: Memanggil `self.refresh()` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `__init__`, baris 86-96): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Membuat keadaan awal; perangkat Essential langsung ON.

Line 97:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 98:
Kode:     def context(self) -> Context:
Penjelasan: Mendefinisikan fungsi `context` dengan parameter: self dan tipe kembalian `Context`. Tujuan: Membangun Context kebijakan dari keadaan sensor dan keputusan lampu.

Line 99:
Kode:         """Membangun Context kebijakan dari keadaan sensor dan keputusan lampu."""
Penjelasan: Bagian docstring `context`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 100:
Kode:         lamp = evaluate_lighting(self.mode, self.state.occupied, self.state.dark).lamp_on
Penjelasan: Menetapkan variabel `lamp` dengan nilai `evaluate_lighting(self.mode, self.state.occupied, self.state.dark).lamp_on`.

Line 101:
Kode:         return Context(self.state.occupied, self.state.energy_saving_mode, lamp)
Penjelasan: Mengembalikan hasil ekspresi `Context(self.state.occupied, self.state.energy_saving_mode, lamp)` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `context`, baris 98-101): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Membangun Context kebijakan dari keadaan sensor dan keputusan lampu.

Line 102:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 103:
Kode:     def refresh(self) -> List[str]:
Penjelasan: Mendefinisikan fungsi `refresh` dengan parameter: self dan tipe kembalian `List[str]`. Tujuan: Menyelaraskan perangkat dengan kondisi terbaru; mengembalikan pesan perubahan.

Line 104:
Kode:         """Menyelaraskan perangkat dengan kondisi terbaru; mengembalikan pesan perubahan."""
Penjelasan: Bagian docstring `refresh`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 105:
Kode:         ctx = self.context()
Penjelasan: Menetapkan variabel `ctx` dengan nilai `self.context()`.

Line 106:
Kode:         messages: List[str] = []
Penjelasan: Mendeklarasikan variabel `messages` bertipe `List[str]` dengan nilai awal `[]`.

Line 107:
Kode:         for device in self.manager.devices:
Penjelasan: Perulangan for: variabel `device` mengambil tiap elemen dari `self.manager.devices`, dan blok di bawahnya diulang untuk tiap elemen.

Line 108:
Kode:             if device.spec.condition == "lamp":
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `device.spec.condition == "lamp"` bernilai True.

Line 109:
Kode:                 if ctx.lamp_on and not device.is_on:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `ctx.lamp_on and not device.is_on` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 110:
Kode:                     if request_turn_on(self.manager, device.spec.name, ctx, self.policy).allowed:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `request_turn_on(self.manager, device.spec.name, ctx, self.policy).allowed` bernilai True.

Line 111:
Kode:                         messages.append(f"{device.spec.name} dinyalakan otomatis (lampu ON).")
Penjelasan: Memanggil `messages.append(f"{device.spec.name} dinyalakan otomatis (lampu ON).")` (hasilnya tidak disimpan; yang penting efeknya).

Line 112:
Kode:                 elif not ctx.lamp_on and device.is_on:
Penjelasan: Percabangan alternatif (elif): blok di bawahnya hanya dijalankan jika kondisi `not ctx.lamp_on and device.is_on` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 113:
Kode:                     self.manager.turn_off(device.spec.name)
Penjelasan: Memanggil `self.manager.turn_off(device.spec.name)` (hasilnya tidak disimpan; yang penting efeknya).

Line 114:
Kode:                     messages.append(f"{device.spec.name} dimatikan otomatis (lampu OFF).")
Penjelasan: Memanggil `messages.append(f"{device.spec.name} dimatikan otomatis (lampu OFF).")` (hasilnya tidak disimpan; yang penting efeknya).

Line 115:
Kode:         messages += enforce_policy(self.manager, ctx, self.policy)
Penjelasan: Memperbarui `messages` dengan operasi `Add` terhadap `enforce_policy(self.manager, ctx, self.policy)`.

Line 116:
Kode:         return messages
Penjelasan: Mengembalikan hasil ekspresi `messages` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `refresh`, baris 103-116): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Menyelaraskan perangkat dengan kondisi terbaru; mengembalikan pesan perubahan.

Line 117:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 118:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 119:
Kode: def show_messages(messages: List[str]) -> None:
Penjelasan: Mendefinisikan fungsi `show_messages` dengan parameter: messages: List[str] dan tipe kembalian `None`. Tujuan: Mencetak pesan perubahan otomatis, bila ada.

Line 120:
Kode:     """Mencetak pesan perubahan otomatis, bila ada."""
Penjelasan: Bagian docstring `show_messages`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 121:
Kode:     for message in messages:
Penjelasan: Perulangan for: variabel `message` mengambil tiap elemen dari `messages`, dan blok di bawahnya diulang untuk tiap elemen.

Line 122:
Kode:         print(f"  * {message}")
Penjelasan: Memanggil `print(f" * {message}")` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `show_messages`, baris 119-122): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Mencetak pesan perubahan otomatis, bila ada.

Line 123:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 124:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 125:
Kode: def edit_fields(home: SmartHome, keys: List[str]) -> None:
Penjelasan: Mendefinisikan fungsi `edit_fields` dengan parameter: home: SmartHome, keys: List[str] dan tipe kembalian `None`. Tujuan: Sub-menu mengubah field sensor yang dipilih.

Line 126:
Kode:     """Sub-menu mengubah field sensor yang dipilih."""
Penjelasan: Bagian docstring `edit_fields`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 127:
Kode:     while True:
Penjelasan: Perulangan while: blok di bawahnya diulang selama `True` bernilai True.

Line 128:
Kode:         print()
Penjelasan: Memanggil `print()` (hasilnya tidak disimpan; yang penting efeknya).

Line 129:
Kode:         for number, key in enumerate(keys, 1):
Penjelasan: Perulangan for: variabel `(number, key)` mengambil tiap elemen dari `enumerate(keys, 1)`, dan blok di bawahnya diulang untuk tiap elemen.

Line 130:
Kode:             print(f"{number}. {FIELDS[key]:<42} = {getattr(home.state, key)}")
Penjelasan: Memanggil `print(f"{number}. {FIELDS[key]:<42} = {getattr(home.state, key)}")` (hasilnya tidak disimpan; yang penting efeknya).

Line 131:
Kode:         print("0. Kembali")
Penjelasan: Memanggil `print("0. Kembali")` (hasilnya tidak disimpan; yang penting efeknya).

Line 132:
Kode:         choice = read_choice("Pilih yang diubah: ", [str(i) for i in range(len(keys) + 1)])
Penjelasan: Menetapkan variabel `choice` dengan nilai `read_choice("Pilih yang diubah: ", [str(i) for i in range(len(keys) + 1)])`.

Line 133:
Kode:         if choice == "0":
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `choice == "0"` bernilai True.

Line 134:
Kode:             return
Penjelasan: Keluar dari fungsi tanpa nilai (None).

Line 135:
Kode:         key = keys[int(choice) - 1]
Penjelasan: Menetapkan variabel `key` dengan nilai `keys[int(choice) - 1]`.

Line 136:
Kode:         value = read_bool(f"Nilai baru untuk '{FIELDS[key]}'")
Penjelasan: Menetapkan variabel `value` dengan nilai `read_bool(f"Nilai baru untuk '{FIELDS[key]}'")`.

Line 137:
Kode:         if value is not None:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `value is not None` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 138:
Kode:             setattr(home.state, key, value)
Penjelasan: Memanggil `setattr(home.state, key, value)` (hasilnya tidak disimpan; yang penting efeknya).

Line 139:
Kode:             print(f"Diubah: {FIELDS[key]} -> {value}")
Penjelasan: Memanggil `print(f"Diubah: {FIELDS[key]} -> {value}")` (hasilnya tidak disimpan; yang penting efeknya).

Line 140:
Kode:             show_messages(home.refresh())
Penjelasan: Memanggil `show_messages(home.refresh())` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `edit_fields`, baris 125-140): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Sub-menu mengubah field sensor yang dipilih.

Line 141:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 142:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 143:
Kode: def menu_sensors(home: SmartHome) -> None:
Penjelasan: Mendefinisikan fungsi `menu_sensors` dengan parameter: home: SmartHome dan tipe kembalian `None`. Tujuan: Menu 1: konfigurasi seluruh sensor dan kondisi rumah.

Line 144:
Kode:     """Menu 1: konfigurasi seluruh sensor dan kondisi rumah."""
Penjelasan: Bagian docstring `menu_sensors`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 145:
Kode:     title("HOME SENSOR CONFIGURATION")
Penjelasan: Memanggil `title("HOME SENSOR CONFIGURATION")` (hasilnya tidak disimpan; yang penting efeknya).

Line 146:
Kode:     print(describe_state(home.state))
Penjelasan: Memanggil `print(describe_state(home.state))` (hasilnya tidak disimpan; yang penting efeknya).

Line 147:
Kode:     edit_fields(home, list(FIELDS))
Penjelasan: Memanggil `edit_fields(home, list(FIELDS))` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `menu_sensors`, baris 143-147): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Menu 1: konfigurasi seluruh sensor dan kondisi rumah.

Line 148:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 149:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 150:
Kode: def menu_security(home: SmartHome) -> None:
Penjelasan: Mendefinisikan fungsi `menu_security` dengan parameter: home: SmartHome dan tipe kembalian `None`. Tujuan: Menu 2: sistem keamanan, dengan diagnostik XOR/NOR/NAND.

Line 151:
Kode:     """Menu 2: sistem keamanan, dengan diagnostik XOR/NOR/NAND."""
Penjelasan: Bagian docstring `menu_security`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 152:
Kode:     while True:
Penjelasan: Perulangan while: blok di bawahnya diulang selama `True` bernilai True.

Line 153:
Kode:         title("SECURITY SYSTEM")
Penjelasan: Memanggil `title("SECURITY SYSTEM")` (hasilnya tidak disimpan; yang penting efeknya).

Line 154:
Kode:         s = home.state
Penjelasan: Menetapkan variabel `s` dengan nilai `home.state`.

Line 155:
Kode:         result = evaluate_security(s.security_mode, s.door_open, s.motion_detected)
Penjelasan: Menetapkan variabel `result` dengan nilai `evaluate_security(s.security_mode, s.door_open, s.motion_detected)`.

Line 156:
Kode:         print("Rumus: alarm_active = security_mode AND (door_open OR motion_detected)")
Penjelasan: Memanggil `print("Rumus: alarm_active = security_mode AND (door_open OR motion_detected)")` (hasilnya tidak disimpan; yang penting efeknya).

Line 157:
Kode:         print(f"security_mode={s.security_mode} door_open={s.door_open} motion_detected={s.motion_detected}")
Penjelasan: Memanggil `print(f"security_mode={s.security_mode} door_open={s.door_open} motion_detected={s.motion_detected}")` (hasilnya tidak disimpan; yang penting efeknya).

Line 158:
Kode:         print(f"Aktivitas terdeteksi (OR): {result.activity_detected}")
Penjelasan: Memanggil `print(f"Aktivitas terdeteksi (OR): {result.activity_detected}")` (hasilnya tidak disimpan; yang penting efeknya).

Line 159:
Kode:         print(f"STATUS ALARM: {'AKTIF' if result.alarm_active else 'MATI'}")
Penjelasan: Memanggil `print(f"STATUS ALARM: {'AKTIF' if result.alarm_active else 'MATI'}")` (hasilnya tidak disimpan; yang penting efeknya).

Line 160:
Kode:         print(f"Alasan: {result.reason}")
Penjelasan: Memanggil `print(f"Alasan: {result.reason}")` (hasilnya tidak disimpan; yang penting efeknya).

Line 161:
Kode:         print(THIN)
Penjelasan: Memanggil `print(THIN)` (hasilnya tidak disimpan; yang penting efeknya).

Line 162:
Kode:         print("Diagnostik sensor:")
Penjelasan: Memanggil `print("Diagnostik sensor:")` (hasilnya tidak disimpan; yang penting efeknya).

Line 163:
Kode:         print(f"  XOR  pintu utama vs redundan berbeda : {door_mismatch(s)}"
Penjelasan: Memanggil `print(f" XOR pintu utama vs redundan berbeda : {door_mismatch(s)}" + (" (periksa sensor; belum tentu ada ya...` (hasilnya tidak disimpan; yang penting efeknya).

Line 164:
Kode:               + ("  (periksa sensor; belum tentu ada yang rusak)" if door_mismatch(s) else ""))
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 163 (`print(f" XOR pintu utama vs redundan berbeda : {door_mism...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 165:
Kode:         print(f"  NOR  tidak ada aktivitas             : {no_activity(s)}")
Penjelasan: Memanggil `print(f" NOR tidak ada aktivitas : {no_activity(s)}")` (hasilnya tidak disimpan; yang penting efeknya).

Line 166:
Kode:         print(f"  NAND diagnostik tidak lengkap        : {diagnostics_incomplete(s)}")
Penjelasan: Memanggil `print(f" NAND diagnostik tidak lengkap : {diagnostics_incomplete(s)}")` (hasilnya tidak disimpan; yang penting efeknya).

Line 167:
Kode:         print(THIN)
Penjelasan: Memanggil `print(THIN)` (hasilnya tidak disimpan; yang penting efeknya).

Line 168:
Kode:         print("1. Ubah sensor / mode keamanan\n0. Kembali ke menu utama")
Penjelasan: Memanggil `print("1. Ubah sensor / mode keamanan\n0. Kembali ke menu utama")` (hasilnya tidak disimpan; yang penting efeknya).

Line 169:
Kode:         if read_choice("Pilih: ", ["0", "1"]) == "0":
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `read_choice("Pilih: ", ["0", "1"]) == "0"` bernilai True.

Line 170:
Kode:             return
Penjelasan: Keluar dari fungsi tanpa nilai (None).

Line 171:
Kode:         edit_fields(home, SECURITY_FIELDS)
Penjelasan: Memanggil `edit_fields(home, SECURITY_FIELDS)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `menu_security`, baris 150-171): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Menu 2: sistem keamanan, dengan diagnostik XOR/NOR/NAND.

Line 172:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 173:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 174:
Kode: def menu_lighting(home: SmartHome) -> None:
Penjelasan: Mendefinisikan fungsi `menu_lighting` dengan parameter: home: SmartHome dan tipe kembalian `None`. Tujuan: Menu 3: otomatisasi lampu dengan mode AUTO/ON/OFF.

Line 175:
Kode:     """Menu 3: otomatisasi lampu dengan mode AUTO/ON/OFF."""
Penjelasan: Bagian docstring `menu_lighting`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 176:
Kode:     while True:
Penjelasan: Perulangan while: blok di bawahnya diulang selama `True` bernilai True.

Line 177:
Kode:         title("LIGHTING AUTOMATION")
Penjelasan: Memanggil `title("LIGHTING AUTOMATION")` (hasilnya tidak disimpan; yang penting efeknya).

Line 178:
Kode:         result = evaluate_lighting(home.mode, home.state.occupied, home.state.dark)
Penjelasan: Menetapkan variabel `result` dengan nilai `evaluate_lighting(home.mode, home.state.occupied, home.state.dark)`.

Line 179:
Kode:         print("Rumus AUTO: lamp_on = occupied AND dark")
Penjelasan: Memanggil `print("Rumus AUTO: lamp_on = occupied AND dark")` (hasilnya tidak disimpan; yang penting efeknya).

Line 180:
Kode:         print(f"Mode kontrol: {home.mode.value} | occupied={home.state.occupied} dark={home.state.dark}")
Penjelasan: Memanggil `print(f"Mode kontrol: {home.mode.value} | occupied={home.state.occupied} dark={home.state.dark}")` (hasilnya tidak disimpan; yang penting efeknya).

Line 181:
Kode:         print(f"Keputusan otomatis (occupied AND dark): {result.auto_decision}")
Penjelasan: Memanggil `print(f"Keputusan otomatis (occupied AND dark): {result.auto_decision}")` (hasilnya tidak disimpan; yang penting efeknya).

Line 182:
Kode:         print(f"STATUS LAMPU: {'ON' if result.lamp_on else 'OFF'}")
Penjelasan: Memanggil `print(f"STATUS LAMPU: {'ON' if result.lamp_on else 'OFF'}")` (hasilnya tidak disimpan; yang penting efeknya).

Line 183:
Kode:         print(f"Alasan: {result.reason}")
Penjelasan: Memanggil `print(f"Alasan: {result.reason}")` (hasilnya tidak disimpan; yang penting efeknya).

Line 184:
Kode:         print(THIN)
Penjelasan: Memanggil `print(THIN)` (hasilnya tidak disimpan; yang penting efeknya).

Line 185:
Kode:         print("1. Ganti mode (AUTO/ON/OFF)\n2. Ubah occupied/dark\n0. Kembali")
Penjelasan: Memanggil `print("1. Ganti mode (AUTO/ON/OFF)\n2. Ubah occupied/dark\n0. Kembali")` (hasilnya tidak disimpan; yang penting efeknya).

Line 186:
Kode:         choice = read_choice("Pilih: ", ["0", "1", "2"])
Penjelasan: Menetapkan variabel `choice` dengan nilai `read_choice("Pilih: ", ["0", "1", "2"])`.

Line 187:
Kode:         if choice == "0":
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `choice == "0"` bernilai True.

Line 188:
Kode:             return
Penjelasan: Keluar dari fungsi tanpa nilai (None).

Line 189:
Kode:         if choice == "2":
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `choice == "2"` bernilai True.

Line 190:
Kode:             edit_fields(home, ["occupied", "dark"])
Penjelasan: Memanggil `edit_fields(home, ["occupied", "dark"])` (hasilnya tidak disimpan; yang penting efeknya).

Line 191:
Kode:             continue
Penjelasan: Melanjutkan ke iterasi berikutnya pada perulangan terdekat.

Line 192:
Kode:         mode = None
Penjelasan: Menetapkan variabel `mode` dengan nilai `None`.

Line 193:
Kode:         while mode is None:
Penjelasan: Perulangan while: blok di bawahnya diulang selama `mode is None` bernilai True.

Line 194:
Kode:             text = read_text("Mode baru (1=AUTO, 2=ON, 3=OFF) [kosong = batal]: ")
Penjelasan: Menetapkan variabel `text` dengan nilai `read_text("Mode baru (1=AUTO, 2=ON, 3=OFF) [kosong = batal]: ")`. File handling: membaca/menulis/menyiapkan file data (JSON atau CSV).

Line 195:
Kode:             if text == "":
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `text == ""` bernilai True.

Line 196:
Kode:                 break
Penjelasan: Menghentikan perulangan terdekat.

Line 197:
Kode:             mode = parse_lighting_mode(text)
Penjelasan: Menetapkan variabel `mode` dengan nilai `parse_lighting_mode(text)`.

Line 198:
Kode:             if mode is None:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `mode is None` bernilai True.

Line 199:
Kode:                 print("Mode tidak valid.")
Penjelasan: Memanggil `print("Mode tidak valid.")` (hasilnya tidak disimpan; yang penting efeknya).

Line 200:
Kode:         if mode is not None:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `mode is not None` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 201:
Kode:             print(f"Mode lampu berubah: {home.mode.value} -> {mode.value}")
Penjelasan: Memanggil `print(f"Mode lampu berubah: {home.mode.value} -> {mode.value}")` (hasilnya tidak disimpan; yang penting efeknya).

Line 202:
Kode:             home.mode = mode
Penjelasan: Menetapkan variabel `home.mode` dengan nilai `mode`.

Line 203:
Kode:             show_messages(home.refresh())
Penjelasan: Memanggil `show_messages(home.refresh())` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `menu_lighting`, baris 174-203): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Menu 3: otomatisasi lampu dengan mode AUTO/ON/OFF.

Line 204:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 205:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 206:
Kode: def print_devices(home: SmartHome) -> None:
Penjelasan: Mendefinisikan fungsi `print_devices` dengan parameter: home: SmartHome dan tipe kembalian `None`. Tujuan: Mencetak tabel perangkat beserta keputusan kebijakan dan alasannya.

Line 207:
Kode:     """Mencetak tabel perangkat beserta keputusan kebijakan dan alasannya."""
Penjelasan: Bagian docstring `print_devices`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 208:
Kode:     ctx = home.context()
Penjelasan: Menetapkan variabel `ctx` dengan nilai `home.context()`.

Line 209:
Kode:     print(f"{'No':<3}{'Perangkat':<21}{'Kategori':<14}{'Daya':>6}  {'Status':<7}{'Menit':>6}{'Aktv':>5}{'Idle':>6}")
Penjelasan: Memanggil `print(f"{'No':<3}{'Perangkat':<21}{'Kategori':<14}{'Daya':>6} {'Status':<7}{'Menit':>6}{'Aktv':>5}{'Idle':>...` (hasilnya tidak disimpan; yang penting efeknya).

Line 210:
Kode:     print(THIN * 2)
Penjelasan: Memanggil `print(THIN * 2)` (hasilnya tidak disimpan; yang penting efeknya).

Line 211:
Kode:     for number, d in enumerate(home.manager.devices, 1):
Penjelasan: Perulangan for: variabel `(number, d)` mengambil tiap elemen dari `enumerate(home.manager.devices, 1)`, dan blok di bawahnya diulang untuk tiap elemen.

Line 212:
Kode:         print(f"{number:<3}{d.spec.name:<21}{d.spec.category:<14}{d.spec.power_w:>5.0f}W  "
Penjelasan: Memanggil `print(f"{number:<3}{d.spec.name:<21}{d.spec.category:<14}{d.spec.power_w:>5.0f}W " f"{'ON' if d.is_on else ...` (hasilnya tidak disimpan; yang penting efeknya).

Line 213:
Kode:               f"{'ON' if d.is_on else 'OFF':<7}{d.minutes_today:>6}{d.activations_today:>5}{d.idle_minutes:>6}")
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 212 (`print(f"{number:<3}{d.spec.name:<21}{d.spec.category:<14}...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 214:
Kode:         decision = evaluate_device(d, ctx, home.policy, activation=not d.is_on)
Penjelasan: Menetapkan variabel `decision` dengan nilai `evaluate_device(d, ctx, home.policy, activation=not d.is_on)`.

Line 215:
Kode:         print(f"    -> {decision.reason}")
Penjelasan: Memanggil `print(f" -> {decision.reason}")` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `print_devices`, baris 206-215): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Mencetak tabel perangkat beserta keputusan kebijakan dan alasannya.

Line 216:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 217:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 218:
Kode: def menu_appliances(home: SmartHome) -> None:
Penjelasan: Mendefinisikan fungsi `menu_appliances` dengan parameter: home: SmartHome dan tipe kembalian `None`. Tujuan: Menu 4: melihat dan mengubah status perangkat (simulasi).

Line 219:
Kode:     """Menu 4: melihat dan mengubah status perangkat (simulasi)."""
Penjelasan: Bagian docstring `menu_appliances`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 220:
Kode:     while True:
Penjelasan: Perulangan while: blok di bawahnya diulang selama `True` bernilai True.

Line 221:
Kode:         title("HOME APPLIANCES (nilai daya = asumsi simulasi)")
Penjelasan: Memanggil `title("HOME APPLIANCES (nilai daya = asumsi simulasi)")` (hasilnya tidak disimpan; yang penting efeknya).

Line 222:
Kode:         print_devices(home)
Penjelasan: Memanggil `print_devices(home)` (hasilnya tidak disimpan; yang penting efeknya).

Line 223:
Kode:         print(THIN * 2)
Penjelasan: Memanggil `print(THIN * 2)` (hasilnya tidak disimpan; yang penting efeknya).

Line 224:
Kode:         number = read_int(f"Nomor perangkat untuk ON/OFF (1-{len(home.manager.devices)}), 0 = kembali", 0)
Penjelasan: Menetapkan variabel `number` dengan nilai `read_int(f"Nomor perangkat untuk ON/OFF (1-{len(home.manager.devices)}), 0 = kembali", 0)`.

Line 225:
Kode:         if number is None or number == 0:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `number is None or number == 0` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 226:
Kode:             return
Penjelasan: Keluar dari fungsi tanpa nilai (None).

Line 227:
Kode:         if number > len(home.manager.devices):
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `number > len(home.manager.devices)` bernilai True.

Line 228:
Kode:             print("Nomor perangkat tidak ada.")
Penjelasan: Memanggil `print("Nomor perangkat tidak ada.")` (hasilnya tidak disimpan; yang penting efeknya).

Line 229:
Kode:             continue
Penjelasan: Melanjutkan ke iterasi berikutnya pada perulangan terdekat.

Line 230:
Kode:         device = home.manager.devices[number - 1]
Penjelasan: Menetapkan variabel `device` dengan nilai `home.manager.devices[number - 1]`.

Line 231:
Kode:         if device.is_on:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `device.is_on` bernilai True.

Line 232:
Kode:             if device.spec.category == CATEGORY_ESSENTIAL:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `device.spec.category == CATEGORY_ESSENTIAL` bernilai True.

Line 233:
Kode:                 print("Ditolak: perangkat esensial harus tetap aktif.")
Penjelasan: Memanggil `print("Ditolak: perangkat esensial harus tetap aktif.")` (hasilnya tidak disimpan; yang penting efeknya).

Line 234:
Kode:             else:
Penjelasan: Cabang else: dijalankan bila semua kondisi if/elif/for di atasnya tidak terpenuhi.

Line 235:
Kode:                 home.manager.turn_off(device.spec.name)
Penjelasan: Memanggil `home.manager.turn_off(device.spec.name)` (hasilnya tidak disimpan; yang penting efeknya).

Line 236:
Kode:                 print(f"{device.spec.name} dimatikan.")
Penjelasan: Memanggil `print(f"{device.spec.name} dimatikan.")` (hasilnya tidak disimpan; yang penting efeknya).

Line 237:
Kode:         else:
Penjelasan: Cabang else: dijalankan bila semua kondisi if/elif/for di atasnya tidak terpenuhi.

Line 238:
Kode:             decision = request_turn_on(home.manager, device.spec.name, home.context(), home.policy)
Penjelasan: Menetapkan variabel `decision` dengan nilai `request_turn_on(home.manager, device.spec.name, home.context(), home.policy)`.

Line 239:
Kode:             print(("Berhasil dinyalakan. " if decision.allowed else "Ditolak. ") + decision.reason)
Penjelasan: Memanggil `print(("Berhasil dinyalakan. " if decision.allowed else "Ditolak. ") + decision.reason)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `menu_appliances`, baris 218-239): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Menu 4: melihat dan mengubah status perangkat (simulasi).

Line 240:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 241:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 242:
Kode: def edit_limit(home: SmartHome) -> None:
Penjelasan: Mendefinisikan fungsi `edit_limit` dengan parameter: home: SmartHome dan tipe kembalian `None`. Tujuan: Mengubah satu batas penggunaan perangkat dan menyimpannya ke data/config.json.

Line 243:
Kode:     """Mengubah satu batas penggunaan perangkat dan menyimpannya ke data/config.json."""
Penjelasan: Bagian docstring `edit_limit`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 244:
Kode:     number = read_int(f"Nomor perangkat (1-{len(home.manager.devices)})", 1)
Penjelasan: Menetapkan variabel `number` dengan nilai `read_int(f"Nomor perangkat (1-{len(home.manager.devices)})", 1)`.

Line 245:
Kode:     if number is None or number > len(home.manager.devices):
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `number is None or number > len(home.manager.devices)` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 246:
Kode:         print("Dibatalkan atau nomor tidak ada.")
Penjelasan: Memanggil `print("Dibatalkan atau nomor tidak ada.")` (hasilnya tidak disimpan; yang penting efeknya).

Line 247:
Kode:         return
Penjelasan: Keluar dari fungsi tanpa nilai (None).

Line 248:
Kode:     spec = home.manager.devices[number - 1].spec
Penjelasan: Menetapkan variabel `spec` dengan nilai `home.manager.devices[number - 1].spec`.

Line 249:
Kode:     options = {"1": "max_daily_minutes", "2": "max_daily_activations", "3": "inactivity_timeout_minutes"}
Penjelasan: Menetapkan variabel `options` dengan nilai `{"1": "max_daily_minutes", "2": "max_daily_activations", "3": "inactivity_timeout_minutes"}`.

Line 250:
Kode:     print("1. Batas durasi harian (menit)\n2. Batas frekuensi aktivasi/hari\n3. Inactivity timeout (menit)")
Penjelasan: Memanggil `print("1. Batas durasi harian (menit)\n2. Batas frekuensi aktivasi/hari\n3. Inactivity timeout (menit)")` (hasilnya tidak disimpan; yang penting efeknya).

Line 251:
Kode:     field = options[read_choice("Pilih batas: ", list(options))]
Penjelasan: Menetapkan variabel `field` dengan nilai `options[read_choice("Pilih batas: ", list(options))]`.

Line 252:
Kode:     value = read_int("Nilai baru (bilangan bulat > 0)", 1)
Penjelasan: Menetapkan variabel `value` dengan nilai `read_int("Nilai baru (bilangan bulat > 0)", 1)`.

Line 253:
Kode:     if value is None:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `value is None` bernilai True.

Line 254:
Kode:         return
Penjelasan: Keluar dari fungsi tanpa nilai (None).

Line 255:
Kode:     values = {"max_daily_minutes": spec.limits.max_daily_minutes,
Penjelasan: Menetapkan variabel `values` dengan nilai `{"max_daily_minutes": spec.limits.max_daily_minutes, "max_daily_activations": spec.limits.max_daily_activat...`.

Line 256:
Kode:               "max_daily_activations": spec.limits.max_daily_activations,
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 255 (`values = {"max_daily_minutes": spec.limits.max_daily_minu...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 257:
Kode:               "inactivity_timeout_minutes": spec.limits.inactivity_timeout_minutes}
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 255 (`values = {"max_daily_minutes": spec.limits.max_daily_minu...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 258:
Kode:     values[field] = value
Penjelasan: Menetapkan variabel `values[field]` dengan nilai `value`.

Line 259:
Kode:     new_spec = DeviceSpec(spec.name, spec.category, spec.power_w, spec.condition, UsageLimits(**values))
Penjelasan: Menetapkan variabel `new_spec` dengan nilai `DeviceSpec(spec.name, spec.category, spec.power_w, spec.condition, UsageLimits(**values))`.

Line 260:
Kode:     try:
Penjelasan: Awal blok try: kode di bawahnya dijalankan dan kesalahan yang mungkin muncul ditangkap oleh blok except. Exception handling: menangani atau melaporkan kesalahan agar program tidak berhenti mendadak.

Line 261:
Kode:         validate_device_spec(new_spec)
Penjelasan: Memanggil `validate_device_spec(new_spec)` (hasilnya tidak disimpan; yang penting efeknya).

Line 262:
Kode:     except ValueError as error:
Penjelasan: Penangkap kesalahan `except ValueError as error:`: dijalankan bila blok try melempar exception yang sesuai, sehingga program tidak berhenti mendadak.

Line 263:
Kode:         print(f"Ditolak: {error}")
Penjelasan: Memanggil `print(f"Ditolak: {error}")` (hasilnya tidak disimpan; yang penting efeknya).

Line 264:
Kode:         return
Penjelasan: Keluar dari fungsi tanpa nilai (None).

Line 265:
Kode:     home.manager.devices[number - 1].spec = new_spec
Penjelasan: Menetapkan variabel `home.manager.devices[number - 1].spec` dengan nilai `new_spec`.

Line 266:
Kode:     home.config.devices[number - 1] = new_spec
Penjelasan: Menetapkan variabel `home.config.devices[number - 1]` dengan nilai `new_spec`.

Line 267:
Kode:     save_config(home.config)
Penjelasan: Memanggil `save_config(home.config)` (hasilnya tidak disimpan; yang penting efeknya).

Line 268:
Kode:     print(f"Batas {field} untuk {spec.name} = {value} (disimpan ke {CONFIG_PATH.name}). "
Penjelasan: Memanggil `print(f"Batas {field} untuk {spec.name} = {value} (disimpan ke {CONFIG_PATH.name}). " "Batas hanya diterapk...` (hasilnya tidak disimpan; yang penting efeknya).

Line 269:
Kode:           "Batas hanya diterapkan kebijakan pada perangkat Non-essential.")
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 268 (`print(f"Batas {field} untuk {spec.name} = {value} (disimp...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Hubungan antarbaris (fungsi `edit_limit`, baris 242-269): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Mengubah satu batas penggunaan perangkat dan menyimpannya ke data/config.json.

Line 270:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 271:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 272:
Kode: def menu_energy(home: SmartHome) -> None:
Penjelasan: Mendefinisikan fungsi `menu_energy` dengan parameter: home: SmartHome dan tipe kembalian `None`. Tujuan: Menu 5: kebijakan hemat energi, waktu simulasi, laporan konsumsi.

Line 273:
Kode:     """Menu 5: kebijakan hemat energi, waktu simulasi, laporan konsumsi."""
Penjelasan: Bagian docstring `menu_energy`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 274:
Kode:     while True:
Penjelasan: Perulangan while: blok di bawahnya diulang selama `True` bernilai True.

Line 275:
Kode:         title("ENERGY MANAGEMENT (SIMULASI)")
Penjelasan: Memanggil `title("ENERGY MANAGEMENT (SIMULASI)")` (hasilnya tidak disimpan; yang penting efeknya).

Line 276:
Kode:         ctx = home.context()
Penjelasan: Menetapkan variabel `ctx` dengan nilai `home.context()`.

Line 277:
Kode:         print("Strategy 1: nonessential_allowed = occupied AND NOT energy_saving_mode")
Penjelasan: Memanggil `print("Strategy 1: nonessential_allowed = occupied AND NOT energy_saving_mode")` (hasilnya tidak disimpan; yang penting efeknya).

Line 278:
Kode:         print(f"  occupied={ctx.occupied} energy_saving_mode={ctx.energy_saving_mode} -> "
Penjelasan: Memanggil `print(f" occupied={ctx.occupied} energy_saving_mode={ctx.energy_saving_mode} -> " f"nonessential_allowed={n...` (hasilnya tidak disimpan; yang penting efeknya).

Line 279:
Kode:               f"nonessential_allowed={nonessential_allowed(ctx, home.policy)}")
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 278 (`print(f" occupied={ctx.occupied} energy_saving_mode={ctx....`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 280:
Kode:         print(f"  Strategy 1 (shutdown): {'ON' if home.policy.shutdown_enabled else 'OFF'} | "
Penjelasan: Memanggil `print(f" Strategy 1 (shutdown): {'ON' if home.policy.shutdown_enabled else 'OFF'} | " f"Strategy 2 (batas p...` (hasilnya tidak disimpan; yang penting efeknya).

Line 281:
Kode:               f"Strategy 2 (batas penggunaan): {'ON' if home.policy.limits_enabled else 'OFF'}")
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 280 (`print(f" Strategy 1 (shutdown): {'ON' if home.policy.shut...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 282:
Kode:         print(THIN)
Penjelasan: Memanggil `print(THIN)` (hasilnya tidak disimpan; yang penting efeknya).

Line 283:
Kode:         print("1. Lihat perangkat & keputusan    2. Ubah mode hemat energi")
Penjelasan: Memanggil `print("1. Lihat perangkat & keputusan 2. Ubah mode hemat energi")` (hasilnya tidak disimpan; yang penting efeknya).

Line 284:
Kode:         print("3. Saklar Strategy 1              4. Saklar Strategy 2")
Penjelasan: Memanggil `print("3. Saklar Strategy 1 4. Saklar Strategy 2")` (hasilnya tidak disimpan; yang penting efeknya).

Line 285:
Kode:         print("5. Majukan waktu simulasi (menit) 6. Laporan konsumsi hari ini")
Penjelasan: Memanggil `print("5. Majukan waktu simulasi (menit) 6. Laporan konsumsi hari ini")` (hasilnya tidak disimpan; yang penting efeknya).

Line 286:
Kode:         print("7. Ubah batas penggunaan          8. Hari baru (reset penghitung)")
Penjelasan: Memanggil `print("7. Ubah batas penggunaan 8. Hari baru (reset penghitung)")` (hasilnya tidak disimpan; yang penting efeknya).

Line 287:
Kode:         print("9. Bandingkan skenario energi     0. Kembali")
Penjelasan: Memanggil `print("9. Bandingkan skenario energi 0. Kembali")` (hasilnya tidak disimpan; yang penting efeknya).

Line 288:
Kode:         choice = read_choice("Pilih: ", [str(i) for i in range(10)])
Penjelasan: Menetapkan variabel `choice` dengan nilai `read_choice("Pilih: ", [str(i) for i in range(10)])`.

Line 289:
Kode:         if choice == "0":
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `choice == "0"` bernilai True.

Line 290:
Kode:             return
Penjelasan: Keluar dari fungsi tanpa nilai (None).

Line 291:
Kode:         if choice == "1":
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `choice == "1"` bernilai True.

Line 292:
Kode:             print_devices(home)
Penjelasan: Memanggil `print_devices(home)` (hasilnya tidak disimpan; yang penting efeknya).

Line 293:
Kode:         elif choice == "2":
Penjelasan: Percabangan alternatif (elif): blok di bawahnya hanya dijalankan jika kondisi `choice == "2"` bernilai True.

Line 294:
Kode:             value = read_bool("Mode hemat energi")
Penjelasan: Menetapkan variabel `value` dengan nilai `read_bool("Mode hemat energi")`.

Line 295:
Kode:             if value is not None:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `value is not None` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 296:
Kode:                 home.state.energy_saving_mode = value
Penjelasan: Menetapkan variabel `home.state.energy_saving_mode` dengan nilai `value`.

Line 297:
Kode:                 show_messages(home.refresh())
Penjelasan: Memanggil `show_messages(home.refresh())` (hasilnya tidak disimpan; yang penting efeknya).

Line 298:
Kode:         elif choice == "3":
Penjelasan: Percabangan alternatif (elif): blok di bawahnya hanya dijalankan jika kondisi `choice == "3"` bernilai True.

Line 299:
Kode:             home.policy.shutdown_enabled = not home.policy.shutdown_enabled
Penjelasan: Menetapkan variabel `home.policy.shutdown_enabled` dengan nilai `not home.policy.shutdown_enabled`. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 300:
Kode:             show_messages(home.refresh())
Penjelasan: Memanggil `show_messages(home.refresh())` (hasilnya tidak disimpan; yang penting efeknya).

Line 301:
Kode:         elif choice == "4":
Penjelasan: Percabangan alternatif (elif): blok di bawahnya hanya dijalankan jika kondisi `choice == "4"` bernilai True.

Line 302:
Kode:             home.policy.limits_enabled = not home.policy.limits_enabled
Penjelasan: Menetapkan variabel `home.policy.limits_enabled` dengan nilai `not home.policy.limits_enabled`. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 303:
Kode:             show_messages(home.refresh())
Penjelasan: Memanggil `show_messages(home.refresh())` (hasilnya tidak disimpan; yang penting efeknya).

Line 304:
Kode:         elif choice == "5":
Penjelasan: Percabangan alternatif (elif): blok di bawahnya hanya dijalankan jika kondisi `choice == "5"` bernilai True.

Line 305:
Kode:             minutes = read_int("Berapa menit dimajukan", 0)
Penjelasan: Menetapkan variabel `minutes` dengan nilai `read_int("Berapa menit dimajukan", 0)`.

Line 306:
Kode:             if minutes is not None:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `minutes is not None` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 307:
Kode:                 for _ in range(minutes):
Penjelasan: Perulangan for: variabel `_` mengambil tiap elemen dari `range(minutes)`, dan blok di bawahnya diulang untuk tiap elemen.

Line 308:
Kode:                     home.manager.advance_minutes(1)
Penjelasan: Memanggil `home.manager.advance_minutes(1)` (hasilnya tidak disimpan; yang penting efeknya).

Line 309:
Kode:                     show_messages(home.refresh())
Penjelasan: Memanggil `show_messages(home.refresh())` (hasilnya tidak disimpan; yang penting efeknya).

Line 310:
Kode:                 print(f"Waktu simulasi maju {minutes} menit.")
Penjelasan: Memanggil `print(f"Waktu simulasi maju {minutes} menit.")` (hasilnya tidak disimpan; yang penting efeknya).

Line 311:
Kode:         elif choice == "6":
Penjelasan: Percabangan alternatif (elif): blok di bawahnya hanya dijalankan jika kondisi `choice == "6"` bernilai True.

Line 312:
Kode:             for d in home.manager.devices:
Penjelasan: Perulangan for: variabel `d` mengambil tiap elemen dari `home.manager.devices`, dan blok di bawahnya diulang untuk tiap elemen.

Line 313:
Kode:                 print(f"{d.spec.name:<21}{d.minutes_today:>5} menit  {device_energy_kwh(d):8.4f} kWh")
Penjelasan: Memanggil `print(f"{d.spec.name:<21}{d.minutes_today:>5} menit {device_energy_kwh(d):8.4f} kWh")` (hasilnya tidak disimpan; yang penting efeknya).

Line 314:
Kode:             print(f"{'TOTAL':<21}{'':>12}{total_energy_kwh(home.manager):8.4f} kWh  (simulasi)")
Penjelasan: Memanggil `print(f"{'TOTAL':<21}{'':>12}{total_energy_kwh(home.manager):8.4f} kWh (simulasi)")` (hasilnya tidak disimpan; yang penting efeknya).

Line 315:
Kode:         elif choice == "7":
Penjelasan: Percabangan alternatif (elif): blok di bawahnya hanya dijalankan jika kondisi `choice == "7"` bernilai True.

Line 316:
Kode:             edit_limit(home)
Penjelasan: Memanggil `edit_limit(home)` (hasilnya tidak disimpan; yang penting efeknya).

Line 317:
Kode:         elif choice == "8":
Penjelasan: Percabangan alternatif (elif): blok di bawahnya hanya dijalankan jika kondisi `choice == "8"` bernilai True.

Line 318:
Kode:             home.manager.reset_day()
Penjelasan: Memanggil `home.manager.reset_day()` (hasilnya tidak disimpan; yang penting efeknya).

Line 319:
Kode:             print("Penghitung harian di-reset.")
Penjelasan: Memanggil `print("Penghitung harian di-reset.")` (hasilnya tidak disimpan; yang penting efeknya).

Line 320:
Kode:         else:
Penjelasan: Cabang else: dijalankan bila semua kondisi if/elif/for di atasnya tidak terpenuhi.

Line 321:
Kode:             print(research.format_experiment_3(research.run_experiment_3(home.config)))
Penjelasan: Memanggil `print(research.format_experiment_3(research.run_experiment_3(home.config)))` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `menu_energy`, baris 272-321): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Menu 5: kebijakan hemat energi, waktu simulasi, laporan konsumsi.

Line 322:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 323:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 324:
Kode: def menu_boolean(home: SmartHome) -> None:
Penjelasan: Mendefinisikan fungsi `menu_boolean` dengan parameter: home: SmartHome dan tipe kembalian `None`. Tujuan: Menu 6: demonstrasi enam operator Boolean.

Line 325:
Kode:     """Menu 6: demonstrasi enam operator Boolean."""
Penjelasan: Bagian docstring `menu_boolean`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 326:
Kode:     while True:
Penjelasan: Perulangan while: blok di bawahnya diulang selama `True` bernilai True.

Line 327:
Kode:         title("BOOLEAN OPERATIONS DEMONSTRATION")
Penjelasan: Memanggil `title("BOOLEAN OPERATIONS DEMONSTRATION")` (hasilnya tidak disimpan; yang penting efeknya).

Line 328:
Kode:         for number, name in enumerate(OPERATOR_NAMES, 1):
Penjelasan: Perulangan for: variabel `(number, name)` mengambil tiap elemen dari `enumerate(OPERATOR_NAMES, 1)`, dan blok di bawahnya diulang untuk tiap elemen.

Line 329:
Kode:             print(f"{number}. {name}")
Penjelasan: Memanggil `print(f"{number}. {name}")` (hasilnya tidak disimpan; yang penting efeknya).

Line 330:
Kode:         print("7. Tampilkan semua tabel kebenaran\n0. Kembali")
Penjelasan: Memanggil `print("7. Tampilkan semua tabel kebenaran\n0. Kembali")` (hasilnya tidak disimpan; yang penting efeknya).

Line 331:
Kode:         choice = read_choice("Pilih: ", [str(i) for i in range(8)])
Penjelasan: Menetapkan variabel `choice` dengan nilai `read_choice("Pilih: ", [str(i) for i in range(8)])`.

Line 332:
Kode:         if choice == "0":
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `choice == "0"` bernilai True.

Line 333:
Kode:             return
Penjelasan: Keluar dari fungsi tanpa nilai (None).

Line 334:
Kode:         if choice == "7":
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `choice == "7"` bernilai True.

Line 335:
Kode:             for name in OPERATOR_NAMES:
Penjelasan: Perulangan for: variabel `name` mengambil tiap elemen dari `OPERATOR_NAMES`, dan blok di bawahnya diulang untuk tiap elemen.

Line 336:
Kode:                 print(f"\n{name}\n{format_truth_table(name)}")
Penjelasan: Memanggil `print(f"\n{name}\n{format_truth_table(name)}")` (hasilnya tidak disimpan; yang penting efeknya).

Line 337:
Kode:             continue
Penjelasan: Melanjutkan ke iterasi berikutnya pada perulangan terdekat.

Line 338:
Kode:         name = OPERATOR_NAMES[int(choice) - 1]
Penjelasan: Menetapkan variabel `name` dengan nilai `OPERATOR_NAMES[int(choice) - 1]`.

Line 339:
Kode:         values: List[bool] = []
Penjelasan: Mendeklarasikan variabel `values` bertipe `List[bool]` dengan nilai awal `[]`.

Line 340:
Kode:         for label in ["A", "B"][:operator_arity(name)]:
Penjelasan: Perulangan for: variabel `label` mengambil tiap elemen dari `["A", "B"][:operator_arity(name)]`, dan blok di bawahnya diulang untuk tiap elemen.

Line 341:
Kode:             value = read_bool(f"Nilai {label}")
Penjelasan: Menetapkan variabel `value` dengan nilai `read_bool(f"Nilai {label}")`.

Line 342:
Kode:             if value is None:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `value is None` bernilai True.

Line 343:
Kode:                 break
Penjelasan: Menghentikan perulangan terdekat.

Line 344:
Kode:             values.append(value)
Penjelasan: Memanggil `values.append(value)` (hasilnya tidak disimpan; yang penting efeknya).

Line 345:
Kode:         if len(values) == operator_arity(name):
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `len(values) == operator_arity(name)` bernilai True.

Line 346:
Kode:             shown = ", ".join(f"{int(v)}" for v in values)
Penjelasan: Menetapkan variabel `shown` dengan nilai `", ".join(f"{int(v)}" for v in values)`.

Line 347:
Kode:             print(f"\n{name}({shown}) = {int(evaluate_operator(name, *values))}")
Penjelasan: Memanggil `print(f"\n{name}({shown}) = {int(evaluate_operator(name, *values))}")` (hasilnya tidak disimpan; yang penting efeknya).

Line 348:
Kode:             print(format_truth_table(name))
Penjelasan: Memanggil `print(format_truth_table(name))` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `menu_boolean`, baris 324-348): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Menu 6: demonstrasi enam operator Boolean.

Line 349:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 350:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 351:
Kode: def menu_research(home: SmartHome) -> None:
Penjelasan: Mendefinisikan fungsi `menu_research` dengan parameter: home: SmartHome dan tipe kembalian `None`. Tujuan: Menu 7: menjalankan mini research dan menyimpan CSV.

Line 352:
Kode:     """Menu 7: menjalankan mini research dan menyimpan CSV."""
Penjelasan: Bagian docstring `menu_research`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 353:
Kode:     title("MINI RESEARCH & SIMULATION REPORT")
Penjelasan: Memanggil `title("MINI RESEARCH & SIMULATION REPORT")` (hasilnya tidak disimpan; yang penting efeknya).

Line 354:
Kode:     print(research.run_all(home.config))
Penjelasan: Memanggil `print(research.run_all(home.config))` (hasilnya tidak disimpan; yang penting efeknya).

Line 355:
Kode:     read_text("\nTekan Enter untuk kembali...")
Penjelasan: Memanggil `read_text("\nTekan Enter untuk kembali...")` (hasilnya tidak disimpan; yang penting efeknya). File handling: membaca/menulis/menyiapkan file data (JSON atau CSV).

Hubungan antarbaris (fungsi `menu_research`, baris 351-355): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Menu 7: menjalankan mini research dan menyimpan CSV.

Line 356:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 357:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 358:
Kode: def main() -> None:
Penjelasan: Mendefinisikan fungsi `main` dengan parameter: (tanpa parameter) dan tipe kembalian `None`. Tujuan: Memuat konfigurasi lalu menjalankan loop menu utama.

Line 359:
Kode:     """Memuat konfigurasi lalu menjalankan loop menu utama."""
Penjelasan: Bagian docstring `main`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 360:
Kode:     try:
Penjelasan: Awal blok try: kode di bawahnya dijalankan dan kesalahan yang mungkin muncul ditangkap oleh blok except. Exception handling: menangani atau melaporkan kesalahan agar program tidak berhenti mendadak.

Line 361:
Kode:         config = load_config()
Penjelasan: Menetapkan variabel `config` dengan nilai `load_config()`.

Line 362:
Kode:     except ValueError as error:
Penjelasan: Penangkap kesalahan `except ValueError as error:`: dijalankan bila blok try melempar exception yang sesuai, sehingga program tidak berhenti mendadak.

Line 363:
Kode:         print(f"Peringatan: {error}\nMemakai konfigurasi default.")
Penjelasan: Memanggil `print(f"Peringatan: {error}\nMemakai konfigurasi default.")` (hasilnya tidak disimpan; yang penting efeknya).

Line 364:
Kode:         config = default_config()
Penjelasan: Menetapkan variabel `config` dengan nilai `default_config()`.

Line 365:
Kode:     home = SmartHome(config)
Penjelasan: Menetapkan variabel `home` dengan nilai `SmartHome(config)`.

Line 366:
Kode:     actions = {"1": menu_sensors, "2": menu_security, "3": menu_lighting, "4": menu_appliances,
Penjelasan: Menetapkan variabel `actions` dengan nilai `{"1": menu_sensors, "2": menu_security, "3": menu_lighting, "4": menu_appliances, "5": menu_energy, "6": me...`.

Line 367:
Kode:                "5": menu_energy, "6": menu_boolean, "7": menu_research}
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 366 (`actions = {"1": menu_sensors, "2": menu_security, "3": me...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 368:
Kode:     while True:
Penjelasan: Perulangan while: blok di bawahnya diulang selama `True` bernilai True.

Line 369:
Kode:         title("SMART HOME AUTOMATION SYSTEM")
Penjelasan: Memanggil `title("SMART HOME AUTOMATION SYSTEM")` (hasilnya tidak disimpan; yang penting efeknya).

Line 370:
Kode:         print("1. Home Sensor Configuration\n2. Security System\n3. Lighting Automation\n"
Penjelasan: Memanggil `print("1. Home Sensor Configuration\n2. Security System\n3. Lighting Automation\n" "4. Home Appliances\n5. ...` (hasilnya tidak disimpan; yang penting efeknya).

Line 371:
Kode:               "4. Home Appliances\n5. Energy Management\n6. Boolean Operations Demonstration\n"
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 370 (`print("1. Home Sensor Configuration\n2. Security System\n...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 372:
Kode:               "7. Mini Research & Simulation Report\n8. Exit")
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 370 (`print("1. Home Sensor Configuration\n2. Security System\n...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 373:
Kode:         choice = read_choice("\nSelect menu: ", [str(i) for i in range(1, 9)])
Penjelasan: Menetapkan variabel `choice` dengan nilai `read_choice("\nSelect menu: ", [str(i) for i in range(1, 9)])`.

Line 374:
Kode:         if choice == "8":
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `choice == "8"` bernilai True.

Line 375:
Kode:             print("Terima kasih.")
Penjelasan: Memanggil `print("Terima kasih.")` (hasilnya tidak disimpan; yang penting efeknya).

Line 376:
Kode:             return
Penjelasan: Keluar dari fungsi tanpa nilai (None).

Line 377:
Kode:         actions[choice](home)
Penjelasan: Memanggil `actions[choice](home)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `main`, baris 358-377): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Memuat konfigurasi lalu menjalankan loop menu utama.

Line 378:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 379:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 380:
Kode: if __name__ == "__main__":
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `__name__ == "__main__"` bernilai True.

Line 381:
Kode:     main()
Penjelasan: Memanggil `main()` (hasilnya tidak disimpan; yang penting efeknya).

~~~~

## tests/test_boolean_operations.py

~~~~text
File: tests/test_boolean_operations.py

Line 1:
Kode: """Unit test enam operator Boolean, tabel kebenaran, dan validasi masukan."""
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 2:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 3:
Kode: import os
Penjelasan: Mengimpor modul: os.

Line 4:
Kode: import sys
Penjelasan: Mengimpor modul: sys.

Line 5:
Kode: import unittest
Penjelasan: Mengimpor modul: unittest.

Line 6:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 7:
Kode: sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
Penjelasan: Memanggil `sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))` (hasilnya tidak disimpan; yang penting efeknya).

Line 8:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 9:
Kode: from boolean_operations import (boolean_and, boolean_nand, boolean_nor, boolean_not, boolean_or,
Penjelasan: Mengimpor boolean_and, boolean_nand, boolean_nor, boolean_not, boolean_or, boolean_xor, evaluate_operator, format_truth_table, operator_arity, reference_result, truth_table dari modul `boolean_operations`.

Line 10:
Kode:                                 boolean_xor, evaluate_operator, format_truth_table,
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 9 (`from boolean_operations import (boolean_and, boolean_nand...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 11:
Kode:                                 operator_arity, reference_result, truth_table)
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 9 (`from boolean_operations import (boolean_and, boolean_nand...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 12:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 13:
Kode: # Tabel kebenaran yang ditulis manual (urutan: 00, 01, 10, 11).
Penjelasan: Komentar: penjelasan untuk pembaca, tidak dieksekusi Python.

Line 14:
Kode: EXPECTED = {
Penjelasan: Menetapkan konstanta/variabel modul `EXPECTED` dengan nilai `{ "AND": [False, False, False, True], "OR": [False, True, True, True], "XOR": [False, True, True, False], "...`.

Line 15:
Kode:     "AND": [False, False, False, True],
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 14 (`EXPECTED = {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 16:
Kode:     "OR": [False, True, True, True],
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 14 (`EXPECTED = {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 17:
Kode:     "XOR": [False, True, True, False],
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 14 (`EXPECTED = {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 18:
Kode:     "NAND": [True, True, True, False],
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 14 (`EXPECTED = {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 19:
Kode:     "NOR": [True, False, False, False],
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 14 (`EXPECTED = {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 20:
Kode: }
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 14 (`EXPECTED = {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 21:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 22:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 23:
Kode: class TestBooleanOperations(unittest.TestCase):
Penjelasan: Mendefinisikan class `TestBooleanOperations` turunan unittest.TestCase. Tujuan: Menguji seluruh kombinasi masukan setiap operator.

Line 24:
Kode:     """Menguji seluruh kombinasi masukan setiap operator."""
Penjelasan: Bagian docstring `TestBooleanOperations`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 25:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 26:
Kode:     FUNCS = {"AND": boolean_and, "OR": boolean_or, "XOR": boolean_xor,
Penjelasan: Menetapkan variabel `FUNCS` dengan nilai `{"AND": boolean_and, "OR": boolean_or, "XOR": boolean_xor, "NAND": boolean_nand, "NOR": boolean_nor}`.

Line 27:
Kode:              "NAND": boolean_nand, "NOR": boolean_nor}
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 26 (`FUNCS = {"AND": boolean_and, "OR": boolean_or, "XOR": boo...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 28:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 29:
Kode:     def test_binary_operators_match_manual_tables(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_binary_operators_match_manual_tables` dengan parameter: self dan tipe kembalian `None`.

Line 30:
Kode:         pairs = [(False, False), (False, True), (True, False), (True, True)]
Penjelasan: Menetapkan variabel `pairs` dengan nilai `[(False, False), (False, True), (True, False), (True, True)]`.

Line 31:
Kode:         for name, func in self.FUNCS.items():
Penjelasan: Perulangan for: variabel `(name, func)` mengambil tiap elemen dari `self.FUNCS.items()`, dan blok di bawahnya diulang untuk tiap elemen.

Line 32:
Kode:             for pair, expected in zip(pairs, EXPECTED[name]):
Penjelasan: Perulangan for: variabel `(pair, expected)` mengambil tiap elemen dari `zip(pairs, EXPECTED[name])`, dan blok di bawahnya diulang untuk tiap elemen.

Line 33:
Kode:                 with self.subTest(op=name, inputs=pair):
Penjelasan: Blok with: membuka konteks `self.subTest(op=name, inputs=pair)` dan menutupnya otomatis setelah blok selesai.

Line 34:
Kode:                     self.assertIs(func(*pair), expected)
Penjelasan: Memanggil `self.assertIs(func(*pair), expected)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_binary_operators_match_manual_tables`, baris 29-34): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 35:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 36:
Kode:     def test_not(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_not` dengan parameter: self dan tipe kembalian `None`.

Line 37:
Kode:         self.assertIs(boolean_not(True), False)
Penjelasan: Memanggil `self.assertIs(boolean_not(True), False)` (hasilnya tidak disimpan; yang penting efeknya). Ekspresi Boolean: memakai operator NOT dari boolean_operations.py.

Line 38:
Kode:         self.assertIs(boolean_not(False), True)
Penjelasan: Memanggil `self.assertIs(boolean_not(False), True)` (hasilnya tidak disimpan; yang penting efeknya). Ekspresi Boolean: memakai operator NOT dari boolean_operations.py.

Hubungan antarbaris (fungsi `test_not`, baris 36-38): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 39:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 40:
Kode:     def test_results_are_real_bool(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_results_are_real_bool` dengan parameter: self dan tipe kembalian `None`.

Line 41:
Kode:         self.assertIs(boolean_and(True, True), True)
Penjelasan: Memanggil `self.assertIs(boolean_and(True, True), True)` (hasilnya tidak disimpan; yang penting efeknya). Ekspresi Boolean: memakai operator AND dari boolean_operations.py.

Line 42:
Kode:         self.assertIsInstance(boolean_or(False, False), bool)
Penjelasan: Memanggil `self.assertIsInstance(boolean_or(False, False), bool)` (hasilnya tidak disimpan; yang penting efeknya). Ekspresi Boolean: memakai operator OR dari boolean_operations.py.

Hubungan antarbaris (fungsi `test_results_are_real_bool`, baris 40-42): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 43:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 44:
Kode:     def test_evaluate_operator_by_name(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_evaluate_operator_by_name` dengan parameter: self dan tipe kembalian `None`.

Line 45:
Kode:         self.assertIs(evaluate_operator("xor", True, False), True)
Penjelasan: Memanggil `self.assertIs(evaluate_operator("xor", True, False), True)` (hasilnya tidak disimpan; yang penting efeknya).

Line 46:
Kode:         self.assertIs(evaluate_operator("NOT", True), False)
Penjelasan: Memanggil `self.assertIs(evaluate_operator("NOT", True), False)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_evaluate_operator_by_name`, baris 44-46): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 47:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 48:
Kode:     def test_reference_matches_functions(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_reference_matches_functions` dengan parameter: self dan tipe kembalian `None`.

Line 49:
Kode:         for name in list(EXPECTED) + ["NOT"]:
Penjelasan: Perulangan for: variabel `name` mengambil tiap elemen dari `list(EXPECTED) + ["NOT"]`, dan blok di bawahnya diulang untuk tiap elemen.

Line 50:
Kode:             for inputs, output in truth_table(name):
Penjelasan: Perulangan for: variabel `(inputs, output)` mengambil tiap elemen dari `truth_table(name)`, dan blok di bawahnya diulang untuk tiap elemen.

Line 51:
Kode:                 self.assertEqual(output, reference_result(name, inputs))
Penjelasan: Memanggil `self.assertEqual(output, reference_result(name, inputs))` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_reference_matches_functions`, baris 48-51): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 52:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 53:
Kode:     def test_invalid_operator_and_arity(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_invalid_operator_and_arity` dengan parameter: self dan tipe kembalian `None`.

Line 54:
Kode:         with self.assertRaises(ValueError):
Penjelasan: Blok with: membuka konteks `self.assertRaises(ValueError)` dan menutupnya otomatis setelah blok selesai.

Line 55:
Kode:             operator_arity("IMPLIES")
Penjelasan: Memanggil `operator_arity("IMPLIES")` (hasilnya tidak disimpan; yang penting efeknya).

Line 56:
Kode:         with self.assertRaises(ValueError):
Penjelasan: Blok with: membuka konteks `self.assertRaises(ValueError)` dan menutupnya otomatis setelah blok selesai.

Line 57:
Kode:             evaluate_operator("AND", True)
Penjelasan: Memanggil `evaluate_operator("AND", True)` (hasilnya tidak disimpan; yang penting efeknya).

Line 58:
Kode:         with self.assertRaises(ValueError):
Penjelasan: Blok with: membuka konteks `self.assertRaises(ValueError)` dan menutupnya otomatis setelah blok selesai.

Line 59:
Kode:             evaluate_operator("NOT", True, False)
Penjelasan: Memanggil `evaluate_operator("NOT", True, False)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_invalid_operator_and_arity`, baris 53-59): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 60:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 61:
Kode:     def test_truth_table_format(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_truth_table_format` dengan parameter: self dan tipe kembalian `None`.

Line 62:
Kode:         text = format_truth_table("NAND")
Penjelasan: Menetapkan variabel `text` dengan nilai `format_truth_table("NAND")`.

Line 63:
Kode:         self.assertIn("A B | NAND", text)
Penjelasan: Memanggil `self.assertIn("A B | NAND", text)` (hasilnya tidak disimpan; yang penting efeknya).

Line 64:
Kode:         self.assertEqual(len(truth_table("NOT")), 2)
Penjelasan: Memanggil `self.assertEqual(len(truth_table("NOT")), 2)` (hasilnya tidak disimpan; yang penting efeknya).

Line 65:
Kode:         self.assertEqual(len(truth_table("NOR")), 4)
Penjelasan: Memanggil `self.assertEqual(len(truth_table("NOR")), 4)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_truth_table_format`, baris 61-65): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 66:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 67:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 68:
Kode: if __name__ == "__main__":
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `__name__ == "__main__"` bernilai True.

Line 69:
Kode:     unittest.main()
Penjelasan: Memanggil `unittest.main()` (hasilnya tidak disimpan; yang penting efeknya).

~~~~

## tests/test_security.py

~~~~text
File: tests/test_security.py

Line 1:
Kode: """Unit test logika alarm (8 kombinasi) dan diagnostik sensor."""
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 2:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 3:
Kode: import os
Penjelasan: Mengimpor modul: os.

Line 4:
Kode: import sys
Penjelasan: Mengimpor modul: sys.

Line 5:
Kode: import unittest
Penjelasan: Mengimpor modul: unittest.

Line 6:
Kode: from itertools import product
Penjelasan: Mengimpor product dari modul `itertools`.

Line 7:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 8:
Kode: sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
Penjelasan: Memanggil `sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))` (hasilnya tidak disimpan; yang penting efeknya).

Line 9:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 10:
Kode: from security import evaluate_security
Penjelasan: Mengimpor evaluate_security dari modul `security`.

Line 11:
Kode: from sensors import (SensorState, diagnostics_incomplete, door_mismatch, no_activity, parse_bool)
Penjelasan: Mengimpor SensorState, diagnostics_incomplete, door_mismatch, no_activity, parse_bool dari modul `sensors`.

Line 12:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 13:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 14:
Kode: class TestSecurity(unittest.TestCase):
Penjelasan: Mendefinisikan class `TestSecurity` turunan unittest.TestCase. Tujuan: Menguji rumus alarm_active = security_mode AND (door_open OR motion_detected).

Line 15:
Kode:     """Menguji rumus alarm_active = security_mode AND (door_open OR motion_detected)."""
Penjelasan: Bagian docstring `TestSecurity`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 16:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 17:
Kode:     def test_all_eight_combinations(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_all_eight_combinations` dengan parameter: self dan tipe kembalian `None`.

Line 18:
Kode:         for mode, door, motion in product([False, True], repeat=3):
Penjelasan: Perulangan for: variabel `(mode, door, motion)` mengambil tiap elemen dari `product([False, True], repeat=3)`, dan blok di bawahnya diulang untuk tiap elemen.

Line 19:
Kode:             expected = mode and (door or motion)
Penjelasan: Menetapkan variabel `expected` dengan nilai `mode and (door or motion)`. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 20:
Kode:             with self.subTest(mode=mode, door=door, motion=motion):
Penjelasan: Blok with: membuka konteks `self.subTest(mode=mode, door=door, motion=motion)` dan menutupnya otomatis setelah blok selesai.

Line 21:
Kode:                 self.assertIs(evaluate_security(mode, door, motion).alarm_active, expected)
Penjelasan: Memanggil `self.assertIs(evaluate_security(mode, door, motion).alarm_active, expected)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_all_eight_combinations`, baris 17-21): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 22:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 23:
Kode:     def test_mode_off_never_alarms(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_mode_off_never_alarms` dengan parameter: self dan tipe kembalian `None`.

Line 24:
Kode:         result = evaluate_security(False, True, True)
Penjelasan: Menetapkan variabel `result` dengan nilai `evaluate_security(False, True, True)`.

Line 25:
Kode:         self.assertFalse(result.alarm_active)
Penjelasan: Memanggil `self.assertFalse(result.alarm_active)` (hasilnya tidak disimpan; yang penting efeknya).

Line 26:
Kode:         self.assertIn("mode keamanan OFF", result.reason)
Penjelasan: Memanggil `self.assertIn("mode keamanan OFF", result.reason)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_mode_off_never_alarms`, baris 23-26): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 27:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 28:
Kode:     def test_reasons(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_reasons` dengan parameter: self dan tipe kembalian `None`.

Line 29:
Kode:         self.assertIn("pintu terbuka", evaluate_security(True, True, False).reason)
Penjelasan: Memanggil `self.assertIn("pintu terbuka", evaluate_security(True, True, False).reason)` (hasilnya tidak disimpan; yang penting efeknya).

Line 30:
Kode:         self.assertIn("gerakan terdeteksi", evaluate_security(True, False, True).reason)
Penjelasan: Memanggil `self.assertIn("gerakan terdeteksi", evaluate_security(True, False, True).reason)` (hasilnya tidak disimpan; yang penting efeknya).

Line 31:
Kode:         self.assertIn("tidak ada gerakan", evaluate_security(True, False, False).reason)
Penjelasan: Memanggil `self.assertIn("tidak ada gerakan", evaluate_security(True, False, False).reason)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_reasons`, baris 28-31): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 32:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 33:
Kode:     def test_xor_door_mismatch_and_nor(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_xor_door_mismatch_and_nor` dengan parameter: self dan tipe kembalian `None`.

Line 34:
Kode:         self.assertTrue(door_mismatch(SensorState(door_open=True, door_open_redundant=False)))
Penjelasan: Memanggil `self.assertTrue(door_mismatch(SensorState(door_open=True, door_open_redundant=False)))` (hasilnya tidak disimpan; yang penting efeknya).

Line 35:
Kode:         self.assertFalse(door_mismatch(SensorState(door_open=True, door_open_redundant=True)))
Penjelasan: Memanggil `self.assertFalse(door_mismatch(SensorState(door_open=True, door_open_redundant=True)))` (hasilnya tidak disimpan; yang penting efeknya).

Line 36:
Kode:         self.assertTrue(no_activity(SensorState()))
Penjelasan: Memanggil `self.assertTrue(no_activity(SensorState()))` (hasilnya tidak disimpan; yang penting efeknya).

Line 37:
Kode:         self.assertFalse(no_activity(SensorState(motion_detected=True)))
Penjelasan: Memanggil `self.assertFalse(no_activity(SensorState(motion_detected=True)))` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_xor_door_mismatch_and_nor`, baris 33-37): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 38:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 39:
Kode:     def test_nand_diagnostics(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_nand_diagnostics` dengan parameter: self dan tipe kembalian `None`.

Line 40:
Kode:         self.assertFalse(diagnostics_incomplete(SensorState()))
Penjelasan: Memanggil `self.assertFalse(diagnostics_incomplete(SensorState()))` (hasilnya tidak disimpan; yang penting efeknya).

Line 41:
Kode:         self.assertTrue(diagnostics_incomplete(SensorState(motion_sensor_online=False)))
Penjelasan: Memanggil `self.assertTrue(diagnostics_incomplete(SensorState(motion_sensor_online=False)))` (hasilnya tidak disimpan; yang penting efeknya).

Line 42:
Kode:         self.assertTrue(diagnostics_incomplete(SensorState(door_open=True)))
Penjelasan: Memanggil `self.assertTrue(diagnostics_incomplete(SensorState(door_open=True)))` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_nand_diagnostics`, baris 39-42): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 43:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 44:
Kode:     def test_parse_bool_validation(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_parse_bool_validation` dengan parameter: self dan tipe kembalian `None`.

Line 45:
Kode:         self.assertIs(parse_bool(" YES "), True)
Penjelasan: Memanggil `self.assertIs(parse_bool(" YES "), True)` (hasilnya tidak disimpan; yang penting efeknya).

Line 46:
Kode:         self.assertIs(parse_bool("closed"), False)
Penjelasan: Memanggil `self.assertIs(parse_bool("closed"), False)` (hasilnya tidak disimpan; yang penting efeknya).

Line 47:
Kode:         self.assertIsNone(parse_bool("mungkin"))
Penjelasan: Memanggil `self.assertIsNone(parse_bool("mungkin"))` (hasilnya tidak disimpan; yang penting efeknya).

Line 48:
Kode:         self.assertIsNone(parse_bool(""))
Penjelasan: Memanggil `self.assertIsNone(parse_bool(""))` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_parse_bool_validation`, baris 44-48): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 49:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 50:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 51:
Kode: if __name__ == "__main__":
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `__name__ == "__main__"` bernilai True.

Line 52:
Kode:     unittest.main()
Penjelasan: Memanggil `unittest.main()` (hasilnya tidak disimpan; yang penting efeknya).

~~~~

## tests/test_lighting.py

~~~~text
File: tests/test_lighting.py

Line 1:
Kode: """Unit test tiga mode pencahayaan dan prioritas manual override."""
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 2:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 3:
Kode: import os
Penjelasan: Mengimpor modul: os.

Line 4:
Kode: import sys
Penjelasan: Mengimpor modul: sys.

Line 5:
Kode: import unittest
Penjelasan: Mengimpor modul: unittest.

Line 6:
Kode: from itertools import product
Penjelasan: Mengimpor product dari modul `itertools`.

Line 7:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 8:
Kode: sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
Penjelasan: Memanggil `sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))` (hasilnya tidak disimpan; yang penting efeknya).

Line 9:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 10:
Kode: from lighting import LightingMode, evaluate_lighting, parse_lighting_mode
Penjelasan: Mengimpor LightingMode, evaluate_lighting, parse_lighting_mode dari modul `lighting`.

Line 11:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 12:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 13:
Kode: class TestLighting(unittest.TestCase):
Penjelasan: Mendefinisikan class `TestLighting` turunan unittest.TestCase. Tujuan: Menguji AUTO (occupied AND dark), ON, dan OFF.

Line 14:
Kode:     """Menguji AUTO (occupied AND dark), ON, dan OFF."""
Penjelasan: Bagian docstring `TestLighting`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 15:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 16:
Kode:     def test_auto_follows_boolean(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_auto_follows_boolean` dengan parameter: self dan tipe kembalian `None`.

Line 17:
Kode:         for occupied, dark in product([False, True], repeat=2):
Penjelasan: Perulangan for: variabel `(occupied, dark)` mengambil tiap elemen dari `product([False, True], repeat=2)`, dan blok di bawahnya diulang untuk tiap elemen.

Line 18:
Kode:             result = evaluate_lighting(LightingMode.AUTO, occupied, dark)
Penjelasan: Menetapkan variabel `result` dengan nilai `evaluate_lighting(LightingMode.AUTO, occupied, dark)`.

Line 19:
Kode:             self.assertIs(result.lamp_on, occupied and dark)
Penjelasan: Memanggil `self.assertIs(result.lamp_on, occupied and dark)` (hasilnya tidak disimpan; yang penting efeknya). Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Hubungan antarbaris (fungsi `test_auto_follows_boolean`, baris 16-19): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 20:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 21:
Kode:     def test_on_always_on(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_on_always_on` dengan parameter: self dan tipe kembalian `None`.

Line 22:
Kode:         for occupied, dark in product([False, True], repeat=2):
Penjelasan: Perulangan for: variabel `(occupied, dark)` mengambil tiap elemen dari `product([False, True], repeat=2)`, dan blok di bawahnya diulang untuk tiap elemen.

Line 23:
Kode:             self.assertTrue(evaluate_lighting(LightingMode.ON, occupied, dark).lamp_on)
Penjelasan: Memanggil `self.assertTrue(evaluate_lighting(LightingMode.ON, occupied, dark).lamp_on)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_on_always_on`, baris 21-23): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 24:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 25:
Kode:     def test_off_always_off(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_off_always_off` dengan parameter: self dan tipe kembalian `None`.

Line 26:
Kode:         for occupied, dark in product([False, True], repeat=2):
Penjelasan: Perulangan for: variabel `(occupied, dark)` mengambil tiap elemen dari `product([False, True], repeat=2)`, dan blok di bawahnya diulang untuk tiap elemen.

Line 27:
Kode:             self.assertFalse(evaluate_lighting(LightingMode.OFF, occupied, dark).lamp_on)
Penjelasan: Memanggil `self.assertFalse(evaluate_lighting(LightingMode.OFF, occupied, dark).lamp_on)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_off_always_off`, baris 25-27): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 28:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 29:
Kode:     def test_override_has_priority_over_auto_decision(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_override_has_priority_over_auto_decision` dengan parameter: self dan tipe kembalian `None`.

Line 30:
Kode:         result = evaluate_lighting(LightingMode.OFF, True, True)
Penjelasan: Menetapkan variabel `result` dengan nilai `evaluate_lighting(LightingMode.OFF, True, True)`.

Line 31:
Kode:         self.assertTrue(result.auto_decision)
Penjelasan: Memanggil `self.assertTrue(result.auto_decision)` (hasilnya tidak disimpan; yang penting efeknya).

Line 32:
Kode:         self.assertFalse(result.lamp_on)
Penjelasan: Memanggil `self.assertFalse(result.lamp_on)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_override_has_priority_over_auto_decision`, baris 29-32): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 33:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 34:
Kode:     def test_reason_texts(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_reason_texts` dengan parameter: self dan tipe kembalian `None`.

Line 35:
Kode:         self.assertIn("tidak ditempati", evaluate_lighting(LightingMode.AUTO, False, True).reason)
Penjelasan: Memanggil `self.assertIn("tidak ditempati", evaluate_lighting(LightingMode.AUTO, False, True).reason)` (hasilnya tidak disimpan; yang penting efeknya).

Line 36:
Kode:         self.assertIn("tidak gelap", evaluate_lighting(LightingMode.AUTO, True, False).reason)
Penjelasan: Memanggil `self.assertIn("tidak gelap", evaluate_lighting(LightingMode.AUTO, True, False).reason)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_reason_texts`, baris 34-36): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 37:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 38:
Kode:     def test_parse_mode(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_parse_mode` dengan parameter: self dan tipe kembalian `None`.

Line 39:
Kode:         self.assertIs(parse_lighting_mode("auto"), LightingMode.AUTO)
Penjelasan: Memanggil `self.assertIs(parse_lighting_mode("auto"), LightingMode.AUTO)` (hasilnya tidak disimpan; yang penting efeknya).

Line 40:
Kode:         self.assertIs(parse_lighting_mode("2"), LightingMode.ON)
Penjelasan: Memanggil `self.assertIs(parse_lighting_mode("2"), LightingMode.ON)` (hasilnya tidak disimpan; yang penting efeknya).

Line 41:
Kode:         self.assertIs(parse_lighting_mode("OFF"), LightingMode.OFF)
Penjelasan: Memanggil `self.assertIs(parse_lighting_mode("OFF"), LightingMode.OFF)` (hasilnya tidak disimpan; yang penting efeknya).

Line 42:
Kode:         self.assertIsNone(parse_lighting_mode("dim"))
Penjelasan: Memanggil `self.assertIsNone(parse_lighting_mode("dim"))` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_parse_mode`, baris 38-42): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 43:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 44:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 45:
Kode: if __name__ == "__main__":
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `__name__ == "__main__"` bernilai True.

Line 46:
Kode:     unittest.main()
Penjelasan: Memanggil `unittest.main()` (hasilnya tidak disimpan; yang penting efeknya).

~~~~

## tests/test_appliances.py

~~~~text
File: tests/test_appliances.py

Line 1:
Kode: """Unit test klasifikasi perangkat, pencarian, waktu simulasi, dan validasi konfigurasi."""
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 2:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 3:
Kode: import os
Penjelasan: Mengimpor modul: os.

Line 4:
Kode: import sys
Penjelasan: Mengimpor modul: sys.

Line 5:
Kode: import tempfile
Penjelasan: Mengimpor modul: tempfile.

Line 6:
Kode: import unittest
Penjelasan: Mengimpor modul: unittest.

Line 7:
Kode: from pathlib import Path
Penjelasan: Mengimpor Path dari modul `pathlib`.

Line 8:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 9:
Kode: sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
Penjelasan: Memanggil `sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))` (hasilnya tidak disimpan; yang penting efeknya).

Line 10:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 11:
Kode: from appliances import ApplianceManager
Penjelasan: Mengimpor ApplianceManager dari modul `appliances`.

Line 12:
Kode: from config import (CATEGORY_CONDITIONAL, CATEGORY_ESSENTIAL, CATEGORY_NON_ESSENTIAL, AppConfig,
Penjelasan: Mengimpor CATEGORY_CONDITIONAL, CATEGORY_ESSENTIAL, CATEGORY_NON_ESSENTIAL, AppConfig, DeviceSpec, UsageLimits, default_config, load_config, save_config, validate_config, validate_device_spec dari modul `config`.

Line 13:
Kode:                     DeviceSpec, UsageLimits, default_config, load_config, save_config,
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 12 (`from config import (CATEGORY_CONDITIONAL, CATEGORY_ESSENT...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 14:
Kode:                     validate_config, validate_device_spec)
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 12 (`from config import (CATEGORY_CONDITIONAL, CATEGORY_ESSENT...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 15:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 16:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 17:
Kode: class TestAppliances(unittest.TestCase):
Penjelasan: Mendefinisikan class `TestAppliances` turunan unittest.TestCase. Tujuan: Menguji ApplianceManager dan config.

Line 18:
Kode:     """Menguji ApplianceManager dan config."""
Penjelasan: Bagian docstring `TestAppliances`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 19:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 20:
Kode:     def setUp(self) -> None:
Penjelasan: Mendefinisikan fungsi `setUp` dengan parameter: self dan tipe kembalian `None`.

Line 21:
Kode:         self.manager = ApplianceManager(default_config().devices)
Penjelasan: Menetapkan variabel `self.manager` dengan nilai `ApplianceManager(default_config().devices)`.

Hubungan antarbaris (fungsi `setUp`, baris 20-21): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 22:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 23:
Kode:     def test_default_classification(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_default_classification` dengan parameter: self dan tipe kembalian `None`.

Line 24:
Kode:         cats = {d.spec.name: d.spec.category for d in self.manager.devices}
Penjelasan: Menetapkan variabel `cats` dengan nilai `{d.spec.name: d.spec.category for d in self.manager.devices}`.

Line 25:
Kode:         self.assertEqual(cats["Refrigerator"], CATEGORY_ESSENTIAL)
Penjelasan: Memanggil `self.assertEqual(cats["Refrigerator"], CATEGORY_ESSENTIAL)` (hasilnya tidak disimpan; yang penting efeknya).

Line 26:
Kode:         self.assertEqual(cats["Main Lighting"], CATEGORY_CONDITIONAL)
Penjelasan: Memanggil `self.assertEqual(cats["Main Lighting"], CATEGORY_CONDITIONAL)` (hasilnya tidak disimpan; yang penting efeknya).

Line 27:
Kode:         self.assertEqual(cats["Fan"], CATEGORY_CONDITIONAL)
Penjelasan: Memanggil `self.assertEqual(cats["Fan"], CATEGORY_CONDITIONAL)` (hasilnya tidak disimpan; yang penting efeknya).

Line 28:
Kode:         self.assertEqual(cats["Television"], CATEGORY_NON_ESSENTIAL)
Penjelasan: Memanggil `self.assertEqual(cats["Television"], CATEGORY_NON_ESSENTIAL)` (hasilnya tidak disimpan; yang penting efeknya).

Line 29:
Kode:         self.assertEqual(cats["Decorative Lighting"], CATEGORY_NON_ESSENTIAL)
Penjelasan: Memanggil `self.assertEqual(cats["Decorative Lighting"], CATEGORY_NON_ESSENTIAL)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_default_classification`, baris 23-29): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 30:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 31:
Kode:     def test_default_power_values(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_default_power_values` dengan parameter: self dan tipe kembalian `None`.

Line 32:
Kode:         power = {d.spec.name: d.spec.power_w for d in self.manager.devices}
Penjelasan: Menetapkan variabel `power` dengan nilai `{d.spec.name: d.spec.power_w for d in self.manager.devices}`.

Line 33:
Kode:         self.assertEqual(power, {"Refrigerator": 150.0, "Main Lighting": 12.0, "Fan": 45.0,
Penjelasan: Memanggil `self.assertEqual(power, {"Refrigerator": 150.0, "Main Lighting": 12.0, "Fan": 45.0, "Television": 80.0, "De...` (hasilnya tidak disimpan; yang penting efeknya).

Line 34:
Kode:                                  "Television": 80.0, "Decorative Lighting": 20.0})
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 33 (`self.assertEqual(power, {"Refrigerator": 150.0, "Main Lig...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Hubungan antarbaris (fungsi `test_default_power_values`, baris 31-34): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 35:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 36:
Kode:     def test_find_by_name_and_number(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_find_by_name_and_number` dengan parameter: self dan tipe kembalian `None`.

Line 37:
Kode:         self.assertEqual(self.manager.find("television").spec.name, "Television")
Penjelasan: Memanggil `self.assertEqual(self.manager.find("television").spec.name, "Television")` (hasilnya tidak disimpan; yang penting efeknya).

Line 38:
Kode:         self.assertEqual(self.manager.find("1").spec.name, "Refrigerator")
Penjelasan: Memanggil `self.assertEqual(self.manager.find("1").spec.name, "Refrigerator")` (hasilnya tidak disimpan; yang penting efeknya).

Line 39:
Kode:         with self.assertRaises(ValueError):
Penjelasan: Blok with: membuka konteks `self.assertRaises(ValueError)` dan menutupnya otomatis setelah blok selesai.

Line 40:
Kode:             self.manager.find("99")
Penjelasan: Memanggil `self.manager.find("99")` (hasilnya tidak disimpan; yang penting efeknya).

Line 41:
Kode:         with self.assertRaises(ValueError):
Penjelasan: Blok with: membuka konteks `self.assertRaises(ValueError)` dan menutupnya otomatis setelah blok selesai.

Line 42:
Kode:             self.manager.find("Oven")
Penjelasan: Memanggil `self.manager.find("Oven")` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_find_by_name_and_number`, baris 36-42): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 43:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 44:
Kode:     def test_turn_on_off_and_counters(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_turn_on_off_and_counters` dengan parameter: self dan tipe kembalian `None`.

Line 45:
Kode:         self.assertTrue(self.manager.turn_on("Fan"))
Penjelasan: Memanggil `self.assertTrue(self.manager.turn_on("Fan"))` (hasilnya tidak disimpan; yang penting efeknya).

Line 46:
Kode:         self.assertFalse(self.manager.turn_on("Fan"))
Penjelasan: Memanggil `self.assertFalse(self.manager.turn_on("Fan"))` (hasilnya tidak disimpan; yang penting efeknya).

Line 47:
Kode:         self.assertEqual(self.manager.find("Fan").activations_today, 1)
Penjelasan: Memanggil `self.assertEqual(self.manager.find("Fan").activations_today, 1)` (hasilnya tidak disimpan; yang penting efeknya).

Line 48:
Kode:         self.manager.advance_minutes(30)
Penjelasan: Memanggil `self.manager.advance_minutes(30)` (hasilnya tidak disimpan; yang penting efeknya).

Line 49:
Kode:         fan = self.manager.find("Fan")
Penjelasan: Menetapkan variabel `fan` dengan nilai `self.manager.find("Fan")`.

Line 50:
Kode:         self.assertEqual((fan.minutes_today, fan.idle_minutes), (30, 30))
Penjelasan: Memanggil `self.assertEqual((fan.minutes_today, fan.idle_minutes), (30, 30))` (hasilnya tidak disimpan; yang penting efeknya).

Line 51:
Kode:         self.manager.touch("Fan")
Penjelasan: Memanggil `self.manager.touch("Fan")` (hasilnya tidak disimpan; yang penting efeknya).

Line 52:
Kode:         self.assertEqual(fan.idle_minutes, 0)
Penjelasan: Memanggil `self.assertEqual(fan.idle_minutes, 0)` (hasilnya tidak disimpan; yang penting efeknya).

Line 53:
Kode:         self.assertTrue(self.manager.turn_off("Fan"))
Penjelasan: Memanggil `self.assertTrue(self.manager.turn_off("Fan"))` (hasilnya tidak disimpan; yang penting efeknya).

Line 54:
Kode:         self.assertFalse(self.manager.turn_off("Fan"))
Penjelasan: Memanggil `self.assertFalse(self.manager.turn_off("Fan"))` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_turn_on_off_and_counters`, baris 44-54): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 55:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 56:
Kode:     def test_off_device_does_not_accumulate_time(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_off_device_does_not_accumulate_time` dengan parameter: self dan tipe kembalian `None`.

Line 57:
Kode:         self.manager.advance_minutes(100)
Penjelasan: Memanggil `self.manager.advance_minutes(100)` (hasilnya tidak disimpan; yang penting efeknya).

Line 58:
Kode:         self.assertEqual(self.manager.find("Television").minutes_today, 0)
Penjelasan: Memanggil `self.assertEqual(self.manager.find("Television").minutes_today, 0)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_off_device_does_not_accumulate_time`, baris 56-58): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 59:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 60:
Kode:     def test_invalid_minutes(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_invalid_minutes` dengan parameter: self dan tipe kembalian `None`.

Line 61:
Kode:         for bad in (-1, 1.5, True):
Penjelasan: Perulangan for: variabel `bad` mengambil tiap elemen dari `(-1, 1.5, True)`, dan blok di bawahnya diulang untuk tiap elemen.

Line 62:
Kode:             with self.assertRaises(ValueError):
Penjelasan: Blok with: membuka konteks `self.assertRaises(ValueError)` dan menutupnya otomatis setelah blok selesai.

Line 63:
Kode:                 self.manager.advance_minutes(bad)
Penjelasan: Memanggil `self.manager.advance_minutes(bad)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_invalid_minutes`, baris 60-63): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 64:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 65:
Kode:     def test_duplicate_names_rejected(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_duplicate_names_rejected` dengan parameter: self dan tipe kembalian `None`.

Line 66:
Kode:         spec = DeviceSpec("X", CATEGORY_ESSENTIAL, 1.0)
Penjelasan: Menetapkan variabel `spec` dengan nilai `DeviceSpec("X", CATEGORY_ESSENTIAL, 1.0)`.

Line 67:
Kode:         with self.assertRaises(ValueError):
Penjelasan: Blok with: membuka konteks `self.assertRaises(ValueError)` dan menutupnya otomatis setelah blok selesai.

Line 68:
Kode:             ApplianceManager([spec, spec])
Penjelasan: Memanggil `ApplianceManager([spec, spec])` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_duplicate_names_rejected`, baris 65-68): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 69:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 70:
Kode:     def test_reset_day(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_reset_day` dengan parameter: self dan tipe kembalian `None`.

Line 71:
Kode:         self.manager.turn_on("Fan")
Penjelasan: Memanggil `self.manager.turn_on("Fan")` (hasilnya tidak disimpan; yang penting efeknya).

Line 72:
Kode:         self.manager.advance_minutes(10)
Penjelasan: Memanggil `self.manager.advance_minutes(10)` (hasilnya tidak disimpan; yang penting efeknya).

Line 73:
Kode:         self.manager.reset_day()
Penjelasan: Memanggil `self.manager.reset_day()` (hasilnya tidak disimpan; yang penting efeknya).

Line 74:
Kode:         fan = self.manager.find("Fan")
Penjelasan: Menetapkan variabel `fan` dengan nilai `self.manager.find("Fan")`.

Line 75:
Kode:         self.assertEqual((fan.minutes_today, fan.activations_today, fan.idle_minutes), (0, 0, 0))
Penjelasan: Memanggil `self.assertEqual((fan.minutes_today, fan.activations_today, fan.idle_minutes), (0, 0, 0))` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_reset_day`, baris 70-75): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 76:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 77:
Kode:     def test_config_validation(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_config_validation` dengan parameter: self dan tipe kembalian `None`.

Line 78:
Kode:         with self.assertRaises(ValueError):
Penjelasan: Blok with: membuka konteks `self.assertRaises(ValueError)` dan menutupnya otomatis setelah blok selesai.

Line 79:
Kode:             validate_device_spec(DeviceSpec("A", "Unknown", 1.0))
Penjelasan: Memanggil `validate_device_spec(DeviceSpec("A", "Unknown", 1.0))` (hasilnya tidak disimpan; yang penting efeknya).

Line 80:
Kode:         with self.assertRaises(ValueError):
Penjelasan: Blok with: membuka konteks `self.assertRaises(ValueError)` dan menutupnya otomatis setelah blok selesai.

Line 81:
Kode:             validate_device_spec(DeviceSpec("A", CATEGORY_ESSENTIAL, -5.0))
Penjelasan: Memanggil `validate_device_spec(DeviceSpec("A", CATEGORY_ESSENTIAL, -5.0))` (hasilnya tidak disimpan; yang penting efeknya).

Line 82:
Kode:         with self.assertRaises(ValueError):
Penjelasan: Blok with: membuka konteks `self.assertRaises(ValueError)` dan menutupnya otomatis setelah blok selesai.

Line 83:
Kode:             validate_device_spec(DeviceSpec("A", CATEGORY_NON_ESSENTIAL, 5.0, limits=UsageLimits(0, None, None)))
Penjelasan: Memanggil `validate_device_spec(DeviceSpec("A", CATEGORY_NON_ESSENTIAL, 5.0, limits=UsageLimits(0, None, None)))` (hasilnya tidak disimpan; yang penting efeknya).

Line 84:
Kode:         with self.assertRaises(ValueError):
Penjelasan: Blok with: membuka konteks `self.assertRaises(ValueError)` dan menutupnya otomatis setelah blok selesai.

Line 85:
Kode:             validate_config(AppConfig([DeviceSpec("A", CATEGORY_ESSENTIAL, 1.0),
Penjelasan: Memanggil `validate_config(AppConfig([DeviceSpec("A", CATEGORY_ESSENTIAL, 1.0), DeviceSpec("a", CATEGORY_ESSENTIAL, 1....` (hasilnya tidak disimpan; yang penting efeknya).

Line 86:
Kode:                                        DeviceSpec("a", CATEGORY_ESSENTIAL, 1.0)]))
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 85 (`validate_config(AppConfig([DeviceSpec("A", CATEGORY_ESSEN...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Hubungan antarbaris (fungsi `test_config_validation`, baris 77-86): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 87:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 88:
Kode:     def test_config_roundtrip_and_bad_json(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_config_roundtrip_and_bad_json` dengan parameter: self dan tipe kembalian `None`.

Line 89:
Kode:         with tempfile.TemporaryDirectory() as folder:
Penjelasan: Blok with: membuka konteks `tempfile.TemporaryDirectory() as folder` dan menutupnya otomatis setelah blok selesai.

Line 90:
Kode:             path = Path(folder) / "config.json"
Penjelasan: Menetapkan variabel `path` dengan nilai `Path(folder) / "config.json"`.

Line 91:
Kode:             self.assertEqual(len(load_config(path).devices), 5)   # file tidak ada -> default
Penjelasan: Memanggil `self.assertEqual(len(load_config(path).devices), 5)` (hasilnya tidak disimpan; yang penting efeknya).

Line 92:
Kode:             save_config(default_config(), path)
Penjelasan: Memanggil `save_config(default_config(), path)` (hasilnya tidak disimpan; yang penting efeknya).

Line 93:
Kode:             self.assertEqual(load_config(path).devices, default_config().devices)
Penjelasan: Memanggil `self.assertEqual(load_config(path).devices, default_config().devices)` (hasilnya tidak disimpan; yang penting efeknya).

Line 94:
Kode:             path.write_text("{bukan json", encoding="utf-8")
Penjelasan: Memanggil `path.write_text("{bukan json", encoding="utf-8")` (hasilnya tidak disimpan; yang penting efeknya). File handling: membaca/menulis/menyiapkan file data (JSON atau CSV).

Line 95:
Kode:             with self.assertRaises(ValueError):
Penjelasan: Blok with: membuka konteks `self.assertRaises(ValueError)` dan menutupnya otomatis setelah blok selesai.

Line 96:
Kode:                 load_config(path)
Penjelasan: Memanggil `load_config(path)` (hasilnya tidak disimpan; yang penting efeknya).

Line 97:
Kode:             path.write_text("{}", encoding="utf-8")
Penjelasan: Memanggil `path.write_text("{}", encoding="utf-8")` (hasilnya tidak disimpan; yang penting efeknya). File handling: membaca/menulis/menyiapkan file data (JSON atau CSV).

Line 98:
Kode:             with self.assertRaises(ValueError):
Penjelasan: Blok with: membuka konteks `self.assertRaises(ValueError)` dan menutupnya otomatis setelah blok selesai.

Line 99:
Kode:                 load_config(path)
Penjelasan: Memanggil `load_config(path)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_config_roundtrip_and_bad_json`, baris 88-99): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 100:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 101:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 102:
Kode: if __name__ == "__main__":
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `__name__ == "__main__"` bernilai True.

Line 103:
Kode:     unittest.main()
Penjelasan: Memanggil `unittest.main()` (hasilnya tidak disimpan; yang penting efeknya).

~~~~

## tests/test_energy_manager.py

~~~~text
File: tests/test_energy_manager.py

Line 1:
Kode: """Unit test kebijakan energi, batas penggunaan, kalkulasi kWh, dan simulasi riset."""
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 2:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 3:
Kode: import os
Penjelasan: Mengimpor modul: os.

Line 4:
Kode: import sys
Penjelasan: Mengimpor modul: sys.

Line 5:
Kode: import tempfile
Penjelasan: Mengimpor modul: tempfile.

Line 6:
Kode: import unittest
Penjelasan: Mengimpor modul: unittest.

Line 7:
Kode: from itertools import product
Penjelasan: Mengimpor product dari modul `itertools`.

Line 8:
Kode: from pathlib import Path
Penjelasan: Mengimpor Path dari modul `pathlib`.

Line 9:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 10:
Kode: sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
Penjelasan: Memanggil `sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))` (hasilnya tidak disimpan; yang penting efeknya).

Line 11:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 12:
Kode: import research
Penjelasan: Mengimpor modul: research.

Line 13:
Kode: from appliances import ApplianceManager
Penjelasan: Mengimpor ApplianceManager dari modul `appliances`.

Line 14:
Kode: from config import default_config
Penjelasan: Mengimpor default_config dari modul `config`.

Line 15:
Kode: from energy_manager import (Context, EnergyPolicy, compute_savings, device_energy_kwh, energy_kwh,
Penjelasan: Mengimpor Context, EnergyPolicy, compute_savings, device_energy_kwh, energy_kwh, enforce_policy, evaluate_device, nonessential_allowed, percent_change, request_turn_on, total_energy_kwh, usage_flags dari modul `energy_manager`.

Line 16:
Kode:                             enforce_policy, evaluate_device, nonessential_allowed, percent_change,
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 15 (`from energy_manager import (Context, EnergyPolicy, comput...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 17:
Kode:                             request_turn_on, total_energy_kwh, usage_flags)
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 15 (`from energy_manager import (Context, EnergyPolicy, comput...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 18:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 19:
Kode: HOME_OK = Context(occupied=True, energy_saving_mode=False, lamp_on=True)
Penjelasan: Menetapkan konstanta/variabel modul `HOME_OK` dengan nilai `Context(occupied=True, energy_saving_mode=False, lamp_on=True)`.

Line 20:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 21:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 22:
Kode: def make() -> ApplianceManager:
Penjelasan: Mendefinisikan fungsi `make` dengan parameter: (tanpa parameter) dan tipe kembalian `ApplianceManager`. Tujuan: Manager baru dari konfigurasi default (deterministik).

Line 23:
Kode:     """Manager baru dari konfigurasi default (deterministik)."""
Penjelasan: Bagian docstring `make`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 24:
Kode:     return ApplianceManager(default_config().devices)
Penjelasan: Mengembalikan hasil ekspresi `ApplianceManager(default_config().devices)` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `make`, baris 22-24): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Manager baru dari konfigurasi default (deterministik).

Line 25:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 26:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 27:
Kode: class TestStrategy1(unittest.TestCase):
Penjelasan: Mendefinisikan class `TestStrategy1` turunan unittest.TestCase. Tujuan: Strategy 1: occupied AND NOT energy_saving_mode.

Line 28:
Kode:     """Strategy 1: occupied AND NOT energy_saving_mode."""
Penjelasan: Bagian docstring `TestStrategy1`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 29:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 30:
Kode:     def test_formula_all_combinations(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_formula_all_combinations` dengan parameter: self dan tipe kembalian `None`.

Line 31:
Kode:         policy = EnergyPolicy()
Penjelasan: Menetapkan variabel `policy` dengan nilai `EnergyPolicy()`.

Line 32:
Kode:         for occupied, saving in product([False, True], repeat=2):
Penjelasan: Perulangan for: variabel `(occupied, saving)` mengambil tiap elemen dari `product([False, True], repeat=2)`, dan blok di bawahnya diulang untuk tiap elemen.

Line 33:
Kode:             ctx = Context(occupied, saving, True)
Penjelasan: Menetapkan variabel `ctx` dengan nilai `Context(occupied, saving, True)`.

Line 34:
Kode:             self.assertIs(nonessential_allowed(ctx, policy), occupied and not saving)
Penjelasan: Memanggil `self.assertIs(nonessential_allowed(ctx, policy), occupied and not saving)` (hasilnya tidak disimpan; yang penting efeknya). Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Hubungan antarbaris (fungsi `test_formula_all_combinations`, baris 30-34): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 35:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 36:
Kode:     def test_disabled_strategy_always_allows(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_disabled_strategy_always_allows` dengan parameter: self dan tipe kembalian `None`.

Line 37:
Kode:         self.assertTrue(nonessential_allowed(Context(False, True, False), EnergyPolicy(shutdown_enabled=False)))
Penjelasan: Memanggil `self.assertTrue(nonessential_allowed(Context(False, True, False), EnergyPolicy(shutdown_enabled=False)))` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_disabled_strategy_always_allows`, baris 36-37): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 38:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 39:
Kode:     def test_nonessential_shutdown_when_unoccupied_or_saving(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_nonessential_shutdown_when_unoccupied_or_saving` dengan parameter: self dan tipe kembalian `None`.

Line 40:
Kode:         for ctx in (Context(False, False, True), Context(True, True, True)):
Penjelasan: Perulangan for: variabel `ctx` mengambil tiap elemen dari `(Context(False, False, True), Context(True, True, True))`, dan blok di bawahnya diulang untuk tiap elemen.

Line 41:
Kode:             manager = make()
Penjelasan: Menetapkan variabel `manager` dengan nilai `make()`.

Line 42:
Kode:             policy = EnergyPolicy()
Penjelasan: Menetapkan variabel `policy` dengan nilai `EnergyPolicy()`.

Line 43:
Kode:             for name in ("Television", "Decorative Lighting"):
Penjelasan: Perulangan for: variabel `name` mengambil tiap elemen dari `("Television", "Decorative Lighting")`, dan blok di bawahnya diulang untuk tiap elemen.

Line 44:
Kode:                 manager.turn_on(name)
Penjelasan: Memanggil `manager.turn_on(name)` (hasilnya tidak disimpan; yang penting efeknya).

Line 45:
Kode:             turned_off = enforce_policy(manager, ctx, policy)
Penjelasan: Menetapkan variabel `turned_off` dengan nilai `enforce_policy(manager, ctx, policy)`.

Line 46:
Kode:             self.assertEqual(len(turned_off), 2)
Penjelasan: Memanggil `self.assertEqual(len(turned_off), 2)` (hasilnya tidak disimpan; yang penting efeknya).

Line 47:
Kode:             self.assertFalse(manager.find("Television").is_on)
Penjelasan: Memanggil `self.assertFalse(manager.find("Television").is_on)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_nonessential_shutdown_when_unoccupied_or_saving`, baris 39-47): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 48:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 49:
Kode:     def test_essential_never_shut_down(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_essential_never_shut_down` dengan parameter: self dan tipe kembalian `None`.

Line 50:
Kode:         manager = make()
Penjelasan: Menetapkan variabel `manager` dengan nilai `make()`.

Line 51:
Kode:         manager.turn_on("Refrigerator")
Penjelasan: Memanggil `manager.turn_on("Refrigerator")` (hasilnya tidak disimpan; yang penting efeknya).

Line 52:
Kode:         enforce_policy(manager, Context(False, True, False), EnergyPolicy())
Penjelasan: Memanggil `enforce_policy(manager, Context(False, True, False), EnergyPolicy())` (hasilnya tidak disimpan; yang penting efeknya).

Line 53:
Kode:         self.assertTrue(manager.find("Refrigerator").is_on)
Penjelasan: Memanggil `self.assertTrue(manager.find("Refrigerator").is_on)` (hasilnya tidak disimpan; yang penting efeknya).

Line 54:
Kode:         decision = evaluate_device(manager.find("Refrigerator"), Context(False, True, False), EnergyPolicy(), False)
Penjelasan: Menetapkan variabel `decision` dengan nilai `evaluate_device(manager.find("Refrigerator"), Context(False, True, False), EnergyPolicy(), False)`.

Line 55:
Kode:         self.assertTrue(decision.allowed)
Penjelasan: Memanggil `self.assertTrue(decision.allowed)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_essential_never_shut_down`, baris 49-55): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 56:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 57:
Kode:     def test_essential_exempt_from_usage_limits(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_essential_exempt_from_usage_limits` dengan parameter: self dan tipe kembalian `None`.

Line 58:
Kode:         manager = make()
Penjelasan: Menetapkan variabel `manager` dengan nilai `make()`.

Line 59:
Kode:         manager.turn_on("Refrigerator")
Penjelasan: Memanggil `manager.turn_on("Refrigerator")` (hasilnya tidak disimpan; yang penting efeknya).

Line 60:
Kode:         manager.advance_minutes(5000)
Penjelasan: Memanggil `manager.advance_minutes(5000)` (hasilnya tidak disimpan; yang penting efeknya).

Line 61:
Kode:         self.assertTrue(evaluate_device(manager.find("Refrigerator"), HOME_OK, EnergyPolicy(), False).allowed)
Penjelasan: Memanggil `self.assertTrue(evaluate_device(manager.find("Refrigerator"), HOME_OK, EnergyPolicy(), False).allowed)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_essential_exempt_from_usage_limits`, baris 57-61): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 62:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 63:
Kode:     def test_conditional_rules(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_conditional_rules` dengan parameter: self dan tipe kembalian `None`.

Line 64:
Kode:         manager = make()
Penjelasan: Menetapkan variabel `manager` dengan nilai `make()`.

Line 65:
Kode:         fan = manager.find("Fan")
Penjelasan: Menetapkan variabel `fan` dengan nilai `manager.find("Fan")`.

Line 66:
Kode:         self.assertTrue(evaluate_device(fan, Context(True, False, False), EnergyPolicy(), True).allowed)
Penjelasan: Memanggil `self.assertTrue(evaluate_device(fan, Context(True, False, False), EnergyPolicy(), True).allowed)` (hasilnya tidak disimpan; yang penting efeknya).

Line 67:
Kode:         self.assertFalse(evaluate_device(fan, Context(False, False, True), EnergyPolicy(), True).allowed)
Penjelasan: Memanggil `self.assertFalse(evaluate_device(fan, Context(False, False, True), EnergyPolicy(), True).allowed)` (hasilnya tidak disimpan; yang penting efeknya).

Line 68:
Kode:         lamp = manager.find("Main Lighting")
Penjelasan: Menetapkan variabel `lamp` dengan nilai `manager.find("Main Lighting")`.

Line 69:
Kode:         self.assertTrue(evaluate_device(lamp, Context(True, False, True), EnergyPolicy(), True).allowed)
Penjelasan: Memanggil `self.assertTrue(evaluate_device(lamp, Context(True, False, True), EnergyPolicy(), True).allowed)` (hasilnya tidak disimpan; yang penting efeknya).

Line 70:
Kode:         self.assertFalse(evaluate_device(lamp, Context(True, False, False), EnergyPolicy(), True).allowed)
Penjelasan: Memanggil `self.assertFalse(evaluate_device(lamp, Context(True, False, False), EnergyPolicy(), True).allowed)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_conditional_rules`, baris 63-70): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 71:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 72:
Kode:     def test_request_turn_on_respects_policy(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_request_turn_on_respects_policy` dengan parameter: self dan tipe kembalian `None`.

Line 73:
Kode:         manager = make()
Penjelasan: Menetapkan variabel `manager` dengan nilai `make()`.

Line 74:
Kode:         denied = request_turn_on(manager, "Television", Context(True, True, True), EnergyPolicy())
Penjelasan: Menetapkan variabel `denied` dengan nilai `request_turn_on(manager, "Television", Context(True, True, True), EnergyPolicy())`.

Line 75:
Kode:         self.assertFalse(denied.allowed)
Penjelasan: Memanggil `self.assertFalse(denied.allowed)` (hasilnya tidak disimpan; yang penting efeknya).

Line 76:
Kode:         self.assertFalse(manager.find("Television").is_on)
Penjelasan: Memanggil `self.assertFalse(manager.find("Television").is_on)` (hasilnya tidak disimpan; yang penting efeknya).

Line 77:
Kode:         allowed = request_turn_on(manager, "Television", HOME_OK, EnergyPolicy())
Penjelasan: Menetapkan variabel `allowed` dengan nilai `request_turn_on(manager, "Television", HOME_OK, EnergyPolicy())`.

Line 78:
Kode:         self.assertTrue(allowed.allowed)
Penjelasan: Memanggil `self.assertTrue(allowed.allowed)` (hasilnya tidak disimpan; yang penting efeknya).

Line 79:
Kode:         self.assertTrue(manager.find("Television").is_on)
Penjelasan: Memanggil `self.assertTrue(manager.find("Television").is_on)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_request_turn_on_respects_policy`, baris 72-79): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 80:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 81:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 82:
Kode: class TestStrategy2(unittest.TestCase):
Penjelasan: Mendefinisikan class `TestStrategy2` turunan unittest.TestCase. Tujuan: Strategy 2: durasi, frekuensi, dan inactivity timeout (waktu simulasi, tanpa jam nyata).

Line 83:
Kode:     """Strategy 2: durasi, frekuensi, dan inactivity timeout (waktu simulasi, tanpa jam nyata)."""
Penjelasan: Bagian docstring `TestStrategy2`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 84:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 85:
Kode:     def test_duration_limit_shuts_down_tv(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_duration_limit_shuts_down_tv` dengan parameter: self dan tipe kembalian `None`.

Line 86:
Kode:         manager, policy = make(), EnergyPolicy()
Penjelasan: Menetapkan variabel `(manager, policy)` dengan nilai `make(), EnergyPolicy()`.

Line 87:
Kode:         request_turn_on(manager, "Television", HOME_OK, policy)
Penjelasan: Memanggil `request_turn_on(manager, "Television", HOME_OK, policy)` (hasilnya tidak disimpan; yang penting efeknya).

Line 88:
Kode:         manager.advance_minutes(239)
Penjelasan: Memanggil `manager.advance_minutes(239)` (hasilnya tidak disimpan; yang penting efeknya).

Line 89:
Kode:         manager.touch("Television")
Penjelasan: Memanggil `manager.touch("Television")` (hasilnya tidak disimpan; yang penting efeknya).

Line 90:
Kode:         self.assertTrue(evaluate_device(manager.find("Television"), HOME_OK, policy, False).allowed)
Penjelasan: Memanggil `self.assertTrue(evaluate_device(manager.find("Television"), HOME_OK, policy, False).allowed)` (hasilnya tidak disimpan; yang penting efeknya).

Line 91:
Kode:         manager.advance_minutes(1)
Penjelasan: Memanggil `manager.advance_minutes(1)` (hasilnya tidak disimpan; yang penting efeknya).

Line 92:
Kode:         manager.touch("Television")
Penjelasan: Memanggil `manager.touch("Television")` (hasilnya tidak disimpan; yang penting efeknya).

Line 93:
Kode:         self.assertFalse(evaluate_device(manager.find("Television"), HOME_OK, policy, False).allowed)
Penjelasan: Memanggil `self.assertFalse(evaluate_device(manager.find("Television"), HOME_OK, policy, False).allowed)` (hasilnya tidak disimpan; yang penting efeknya).

Line 94:
Kode:         enforce_policy(manager, HOME_OK, policy)
Penjelasan: Memanggil `enforce_policy(manager, HOME_OK, policy)` (hasilnya tidak disimpan; yang penting efeknya).

Line 95:
Kode:         self.assertFalse(manager.find("Television").is_on)
Penjelasan: Memanggil `self.assertFalse(manager.find("Television").is_on)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_duration_limit_shuts_down_tv`, baris 85-95): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 96:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 97:
Kode:     def test_duration_limit_blocks_reactivation(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_duration_limit_blocks_reactivation` dengan parameter: self dan tipe kembalian `None`.

Line 98:
Kode:         manager, policy = make(), EnergyPolicy()
Penjelasan: Menetapkan variabel `(manager, policy)` dengan nilai `make(), EnergyPolicy()`.

Line 99:
Kode:         request_turn_on(manager, "Television", HOME_OK, policy)
Penjelasan: Memanggil `request_turn_on(manager, "Television", HOME_OK, policy)` (hasilnya tidak disimpan; yang penting efeknya).

Line 100:
Kode:         manager.advance_minutes(240)
Penjelasan: Memanggil `manager.advance_minutes(240)` (hasilnya tidak disimpan; yang penting efeknya).

Line 101:
Kode:         manager.turn_off("Television")
Penjelasan: Memanggil `manager.turn_off("Television")` (hasilnya tidak disimpan; yang penting efeknya).

Line 102:
Kode:         decision = request_turn_on(manager, "Television", HOME_OK, policy)
Penjelasan: Menetapkan variabel `decision` dengan nilai `request_turn_on(manager, "Television", HOME_OK, policy)`.

Line 103:
Kode:         self.assertFalse(decision.allowed)
Penjelasan: Memanggil `self.assertFalse(decision.allowed)` (hasilnya tidak disimpan; yang penting efeknya).

Line 104:
Kode:         self.assertIn("durasi", decision.reason)
Penjelasan: Memanggil `self.assertIn("durasi", decision.reason)` (hasilnya tidak disimpan; yang penting efeknya).

Line 105:
Kode:         manager.reset_day()
Penjelasan: Memanggil `manager.reset_day()` (hasilnya tidak disimpan; yang penting efeknya).

Line 106:
Kode:         self.assertTrue(request_turn_on(manager, "Television", HOME_OK, policy).allowed)
Penjelasan: Memanggil `self.assertTrue(request_turn_on(manager, "Television", HOME_OK, policy).allowed)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_duration_limit_blocks_reactivation`, baris 97-106): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 107:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 108:
Kode:     def test_frequency_limit_blocks_activation_not_running_device(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_frequency_limit_blocks_activation_not_running_device` dengan parameter: self dan tipe kembalian `None`.

Line 109:
Kode:         manager, policy = make(), EnergyPolicy()
Penjelasan: Menetapkan variabel `(manager, policy)` dengan nilai `make(), EnergyPolicy()`.

Line 110:
Kode:         for _ in range(6):
Penjelasan: Perulangan for: variabel `_` mengambil tiap elemen dari `range(6)`, dan blok di bawahnya diulang untuk tiap elemen.

Line 111:
Kode:             self.assertTrue(request_turn_on(manager, "Television", HOME_OK, policy).allowed)
Penjelasan: Memanggil `self.assertTrue(request_turn_on(manager, "Television", HOME_OK, policy).allowed)` (hasilnya tidak disimpan; yang penting efeknya).

Line 112:
Kode:             manager.turn_off("Television")
Penjelasan: Memanggil `manager.turn_off("Television")` (hasilnya tidak disimpan; yang penting efeknya).

Line 113:
Kode:         denied = request_turn_on(manager, "Television", HOME_OK, policy)
Penjelasan: Menetapkan variabel `denied` dengan nilai `request_turn_on(manager, "Television", HOME_OK, policy)`.

Line 114:
Kode:         self.assertFalse(denied.allowed)
Penjelasan: Memanggil `self.assertFalse(denied.allowed)` (hasilnya tidak disimpan; yang penting efeknya).

Line 115:
Kode:         self.assertIn("frekuensi", denied.reason)
Penjelasan: Memanggil `self.assertIn("frekuensi", denied.reason)` (hasilnya tidak disimpan; yang penting efeknya).

Line 116:
Kode:         # perangkat yang sedang ON pada aktivasi terakhir yang sah tidak dimatikan karena frekuensi
Penjelasan: Komentar: penjelasan untuk pembaca, tidak dieksekusi Python.

Line 117:
Kode:         manager.reset_day()
Penjelasan: Memanggil `manager.reset_day()` (hasilnya tidak disimpan; yang penting efeknya).

Line 118:
Kode:         for _ in range(5):
Penjelasan: Perulangan for: variabel `_` mengambil tiap elemen dari `range(5)`, dan blok di bawahnya diulang untuk tiap elemen.

Line 119:
Kode:             request_turn_on(manager, "Television", HOME_OK, policy)
Penjelasan: Memanggil `request_turn_on(manager, "Television", HOME_OK, policy)` (hasilnya tidak disimpan; yang penting efeknya).

Line 120:
Kode:             manager.turn_off("Television")
Penjelasan: Memanggil `manager.turn_off("Television")` (hasilnya tidak disimpan; yang penting efeknya).

Line 121:
Kode:         self.assertTrue(request_turn_on(manager, "Television", HOME_OK, policy).allowed)
Penjelasan: Memanggil `self.assertTrue(request_turn_on(manager, "Television", HOME_OK, policy).allowed)` (hasilnya tidak disimpan; yang penting efeknya).

Line 122:
Kode:         self.assertEqual(manager.find("Television").activations_today, 6)
Penjelasan: Memanggil `self.assertEqual(manager.find("Television").activations_today, 6)` (hasilnya tidak disimpan; yang penting efeknya).

Line 123:
Kode:         self.assertTrue(evaluate_device(manager.find("Television"), HOME_OK, policy, False).allowed)
Penjelasan: Memanggil `self.assertTrue(evaluate_device(manager.find("Television"), HOME_OK, policy, False).allowed)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_frequency_limit_blocks_activation_not_running_device`, baris 108-123): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 124:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 125:
Kode:     def test_inactivity_timeout(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_inactivity_timeout` dengan parameter: self dan tipe kembalian `None`.

Line 126:
Kode:         manager, policy = make(), EnergyPolicy()
Penjelasan: Menetapkan variabel `(manager, policy)` dengan nilai `make(), EnergyPolicy()`.

Line 127:
Kode:         request_turn_on(manager, "Decorative Lighting", HOME_OK, policy)
Penjelasan: Memanggil `request_turn_on(manager, "Decorative Lighting", HOME_OK, policy)` (hasilnya tidak disimpan; yang penting efeknya).

Line 128:
Kode:         manager.advance_minutes(59)
Penjelasan: Memanggil `manager.advance_minutes(59)` (hasilnya tidak disimpan; yang penting efeknya).

Line 129:
Kode:         self.assertTrue(evaluate_device(manager.find("Decorative Lighting"), HOME_OK, policy, False).allowed)
Penjelasan: Memanggil `self.assertTrue(evaluate_device(manager.find("Decorative Lighting"), HOME_OK, policy, False).allowed)` (hasilnya tidak disimpan; yang penting efeknya).

Line 130:
Kode:         manager.advance_minutes(1)
Penjelasan: Memanggil `manager.advance_minutes(1)` (hasilnya tidak disimpan; yang penting efeknya).

Line 131:
Kode:         decision = evaluate_device(manager.find("Decorative Lighting"), HOME_OK, policy, False)
Penjelasan: Menetapkan variabel `decision` dengan nilai `evaluate_device(manager.find("Decorative Lighting"), HOME_OK, policy, False)`.

Line 132:
Kode:         self.assertFalse(decision.allowed)
Penjelasan: Memanggil `self.assertFalse(decision.allowed)` (hasilnya tidak disimpan; yang penting efeknya).

Line 133:
Kode:         self.assertIn("inactivity", decision.reason)
Penjelasan: Memanggil `self.assertIn("inactivity", decision.reason)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_inactivity_timeout`, baris 125-133): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 134:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 135:
Kode:     def test_touch_resets_inactivity(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_touch_resets_inactivity` dengan parameter: self dan tipe kembalian `None`.

Line 136:
Kode:         manager, policy = make(), EnergyPolicy()
Penjelasan: Menetapkan variabel `(manager, policy)` dengan nilai `make(), EnergyPolicy()`.

Line 137:
Kode:         request_turn_on(manager, "Decorative Lighting", HOME_OK, policy)
Penjelasan: Memanggil `request_turn_on(manager, "Decorative Lighting", HOME_OK, policy)` (hasilnya tidak disimpan; yang penting efeknya).

Line 138:
Kode:         manager.advance_minutes(59)
Penjelasan: Memanggil `manager.advance_minutes(59)` (hasilnya tidak disimpan; yang penting efeknya).

Line 139:
Kode:         manager.touch("Decorative Lighting")
Penjelasan: Memanggil `manager.touch("Decorative Lighting")` (hasilnya tidak disimpan; yang penting efeknya).

Line 140:
Kode:         manager.advance_minutes(59)
Penjelasan: Memanggil `manager.advance_minutes(59)` (hasilnya tidak disimpan; yang penting efeknya).

Line 141:
Kode:         self.assertTrue(evaluate_device(manager.find("Decorative Lighting"), HOME_OK, policy, False).allowed)
Penjelasan: Memanggil `self.assertTrue(evaluate_device(manager.find("Decorative Lighting"), HOME_OK, policy, False).allowed)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_touch_resets_inactivity`, baris 135-141): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 142:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 143:
Kode:     def test_usage_flags_are_booleans(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_usage_flags_are_booleans` dengan parameter: self dan tipe kembalian `None`.

Line 144:
Kode:         manager = make()
Penjelasan: Menetapkan variabel `manager` dengan nilai `make()`.

Line 145:
Kode:         flags = usage_flags(manager.find("Television"), activation=True)
Penjelasan: Menetapkan variabel `flags` dengan nilai `usage_flags(manager.find("Television"), activation=True)`.

Line 146:
Kode:         self.assertTrue(all(isinstance(f, bool) for f in flags))
Penjelasan: Memanggil `self.assertTrue(all(isinstance(f, bool) for f in flags))` (hasilnya tidak disimpan; yang penting efeknya).

Line 147:
Kode:         self.assertEqual(flags, (False, False, False))
Penjelasan: Memanggil `self.assertEqual(flags, (False, False, False))` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_usage_flags_are_booleans`, baris 143-147): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 148:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 149:
Kode:     def test_limits_can_be_disabled(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_limits_can_be_disabled` dengan parameter: self dan tipe kembalian `None`.

Line 150:
Kode:         manager = make()
Penjelasan: Menetapkan variabel `manager` dengan nilai `make()`.

Line 151:
Kode:         manager.turn_on("Television")
Penjelasan: Memanggil `manager.turn_on("Television")` (hasilnya tidak disimpan; yang penting efeknya).

Line 152:
Kode:         manager.advance_minutes(1000)
Penjelasan: Memanggil `manager.advance_minutes(1000)` (hasilnya tidak disimpan; yang penting efeknya).

Line 153:
Kode:         self.assertTrue(evaluate_device(manager.find("Television"), HOME_OK,
Penjelasan: Memanggil `self.assertTrue(evaluate_device(manager.find("Television"), HOME_OK, EnergyPolicy(limits_enabled=False), Fa...` (hasilnya tidak disimpan; yang penting efeknya).

Line 154:
Kode:                                         EnergyPolicy(limits_enabled=False), False).allowed)
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 153 (`self.assertTrue(evaluate_device(manager.find("Television"...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Hubungan antarbaris (fungsi `test_limits_can_be_disabled`, baris 149-154): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 155:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 156:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 157:
Kode: class TestEnergyCalculation(unittest.TestCase):
Penjelasan: Mendefinisikan class `TestEnergyCalculation` turunan unittest.TestCase. Tujuan: Rumus kWh = W x jam / 1000.

Line 158:
Kode:     """Rumus kWh = W x jam / 1000."""
Penjelasan: Bagian docstring `TestEnergyCalculation`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 159:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 160:
Kode:     def test_formula(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_formula` dengan parameter: self dan tipe kembalian `None`.

Line 161:
Kode:         self.assertAlmostEqual(energy_kwh(150, 24), 3.6)
Penjelasan: Memanggil `self.assertAlmostEqual(energy_kwh(150, 24), 3.6)` (hasilnya tidak disimpan; yang penting efeknya).

Line 162:
Kode:         self.assertAlmostEqual(energy_kwh(80, 1.5), 0.12)
Penjelasan: Memanggil `self.assertAlmostEqual(energy_kwh(80, 1.5), 0.12)` (hasilnya tidak disimpan; yang penting efeknya).

Line 163:
Kode:         self.assertEqual(energy_kwh(100, 0), 0.0)
Penjelasan: Memanggil `self.assertEqual(energy_kwh(100, 0), 0.0)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_formula`, baris 160-163): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 164:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 165:
Kode:     def test_negative_rejected(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_negative_rejected` dengan parameter: self dan tipe kembalian `None`.

Line 166:
Kode:         with self.assertRaises(ValueError):
Penjelasan: Blok with: membuka konteks `self.assertRaises(ValueError)` dan menutupnya otomatis setelah blok selesai.

Line 167:
Kode:             energy_kwh(-1, 1)
Penjelasan: Memanggil `energy_kwh(-1, 1)` (hasilnya tidak disimpan; yang penting efeknya).

Line 168:
Kode:         with self.assertRaises(ValueError):
Penjelasan: Blok with: membuka konteks `self.assertRaises(ValueError)` dan menutupnya otomatis setelah blok selesai.

Line 169:
Kode:             energy_kwh(1, -1)
Penjelasan: Memanggil `energy_kwh(1, -1)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_negative_rejected`, baris 165-169): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 170:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 171:
Kode:     def test_off_device_zero_and_essential_counted(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_off_device_zero_and_essential_counted` dengan parameter: self dan tipe kembalian `None`.

Line 172:
Kode:         manager = make()
Penjelasan: Menetapkan variabel `manager` dengan nilai `make()`.

Line 173:
Kode:         manager.turn_on("Refrigerator")
Penjelasan: Memanggil `manager.turn_on("Refrigerator")` (hasilnya tidak disimpan; yang penting efeknya).

Line 174:
Kode:         manager.advance_minutes(60)
Penjelasan: Memanggil `manager.advance_minutes(60)` (hasilnya tidak disimpan; yang penting efeknya).

Line 175:
Kode:         self.assertEqual(device_energy_kwh(manager.find("Television")), 0.0)
Penjelasan: Memanggil `self.assertEqual(device_energy_kwh(manager.find("Television")), 0.0)` (hasilnya tidak disimpan; yang penting efeknya).

Line 176:
Kode:         self.assertAlmostEqual(total_energy_kwh(manager), 0.15)
Penjelasan: Memanggil `self.assertAlmostEqual(total_energy_kwh(manager), 0.15)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_off_device_zero_and_essential_counted`, baris 171-176): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 177:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 178:
Kode:     def test_savings(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_savings` dengan parameter: self dan tipe kembalian `None`.

Line 179:
Kode:         saving, percent = compute_savings(5.0, 4.0)
Penjelasan: Menetapkan variabel `(saving, percent)` dengan nilai `compute_savings(5.0, 4.0)`.

Line 180:
Kode:         self.assertAlmostEqual(saving, 1.0)
Penjelasan: Memanggil `self.assertAlmostEqual(saving, 1.0)` (hasilnya tidak disimpan; yang penting efeknya).

Line 181:
Kode:         self.assertAlmostEqual(percent, 20.0)
Penjelasan: Memanggil `self.assertAlmostEqual(percent, 20.0)` (hasilnya tidak disimpan; yang penting efeknya).

Line 182:
Kode:         self.assertAlmostEqual(percent_change(5.0, 4.0), -20.0)
Penjelasan: Memanggil `self.assertAlmostEqual(percent_change(5.0, 4.0), -20.0)` (hasilnya tidak disimpan; yang penting efeknya).

Line 183:
Kode:         self.assertEqual(compute_savings(0.0, 0.0), (0.0, 0.0))
Penjelasan: Memanggil `self.assertEqual(compute_savings(0.0, 0.0), (0.0, 0.0))` (hasilnya tidak disimpan; yang penting efeknya).

Line 184:
Kode:         with self.assertRaises(ValueError):
Penjelasan: Blok with: membuka konteks `self.assertRaises(ValueError)` dan menutupnya otomatis setelah blok selesai.

Line 185:
Kode:             compute_savings(4.0, 5.0)
Penjelasan: Memanggil `compute_savings(4.0, 5.0)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_savings`, baris 178-185): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 186:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 187:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 188:
Kode: class TestResearch(unittest.TestCase):
Penjelasan: Mendefinisikan class `TestResearch` turunan unittest.TestCase. Tujuan: Eksperimen harus deterministik dan konsisten.

Line 189:
Kode:     """Eksperimen harus deterministik dan konsisten."""
Penjelasan: Bagian docstring `TestResearch`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 190:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 191:
Kode:     def test_experiment_1_accuracy_100(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_experiment_1_accuracy_100` dengan parameter: self dan tipe kembalian `None`.

Line 192:
Kode:         results = research.run_experiment_1()
Penjelasan: Menetapkan variabel `results` dengan nilai `research.run_experiment_1()`.

Line 193:
Kode:         self.assertEqual(sum(r[1] for r in results), 22)
Penjelasan: Memanggil `self.assertEqual(sum(r[1] for r in results), 22)` (hasilnya tidak disimpan; yang penting efeknya).

Line 194:
Kode:         self.assertTrue(all(r[3] == 100.0 for r in results))
Penjelasan: Memanggil `self.assertTrue(all(r[3] == 100.0 for r in results))` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_experiment_1_accuracy_100`, baris 191-194): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 195:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 196:
Kode:     def test_experiment_2_eight_cases_all_pass(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_experiment_2_eight_cases_all_pass` dengan parameter: self dan tipe kembalian `None`.

Line 197:
Kode:         rows = research.run_experiment_2()
Penjelasan: Menetapkan variabel `rows` dengan nilai `research.run_experiment_2()`.

Line 198:
Kode:         self.assertEqual(len(rows), 8)
Penjelasan: Memanggil `self.assertEqual(len(rows), 8)` (hasilnya tidak disimpan; yang penting efeknya).

Line 199:
Kode:         self.assertTrue(all(r[3] == r[4] for r in rows))
Penjelasan: Memanggil `self.assertTrue(all(r[3] == r[4] for r in rows))` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_experiment_2_eight_cases_all_pass`, baris 196-199): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 200:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 201:
Kode:     def test_experiment_3_ordering_and_nonnegative_savings(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_experiment_3_ordering_and_nonnegative_savings` dengan parameter: self dan tipe kembalian `None`.

Line 202:
Kode:         a, b, c = research.run_experiment_3()
Penjelasan: Menetapkan variabel `(a, b, c)` dengan nilai `research.run_experiment_3()`.

Line 203:
Kode:         self.assertGreaterEqual(a.total_kwh, b.total_kwh)
Penjelasan: Memanggil `self.assertGreaterEqual(a.total_kwh, b.total_kwh)` (hasilnya tidak disimpan; yang penting efeknya).

Line 204:
Kode:         self.assertGreaterEqual(b.total_kwh, c.total_kwh)
Penjelasan: Memanggil `self.assertGreaterEqual(b.total_kwh, c.total_kwh)` (hasilnya tidak disimpan; yang penting efeknya).

Line 205:
Kode:         self.assertGreater(a.total_kwh, c.total_kwh)
Penjelasan: Memanggil `self.assertGreater(a.total_kwh, c.total_kwh)` (hasilnya tidak disimpan; yang penting efeknya).

Line 206:
Kode:         for result in (b, c):
Penjelasan: Perulangan for: variabel `result` mengambil tiap elemen dari `(b, c)`, dan blok di bawahnya diulang untuk tiap elemen.

Line 207:
Kode:             saving, percent = compute_savings(a.total_kwh, result.total_kwh)
Penjelasan: Menetapkan variabel `(saving, percent)` dengan nilai `compute_savings(a.total_kwh, result.total_kwh)`.

Line 208:
Kode:             self.assertGreaterEqual(saving, 0)
Penjelasan: Memanggil `self.assertGreaterEqual(saving, 0)` (hasilnya tidak disimpan; yang penting efeknya).

Line 209:
Kode:             self.assertGreaterEqual(percent, 0)
Penjelasan: Memanggil `self.assertGreaterEqual(percent, 0)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_experiment_3_ordering_and_nonnegative_savings`, baris 201-209): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 210:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 211:
Kode:     def test_experiment_3_essential_always_full_day(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_experiment_3_essential_always_full_day` dengan parameter: self dan tipe kembalian `None`.

Line 212:
Kode:         for result in research.run_experiment_3():
Penjelasan: Perulangan for: variabel `result` mengambil tiap elemen dari `research.run_experiment_3()`, dan blok di bawahnya diulang untuk tiap elemen.

Line 213:
Kode:             fridge = [row for row in result.rows if row[0] == "Refrigerator"][0]
Penjelasan: Menetapkan variabel `fridge` dengan nilai `[row for row in result.rows if row[0] == "Refrigerator"][0]`.

Line 214:
Kode:             self.assertEqual(fridge[1], 1440)
Penjelasan: Memanggil `self.assertEqual(fridge[1], 1440)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_experiment_3_essential_always_full_day`, baris 211-214): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 215:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 216:
Kode:     def test_experiment_3_is_deterministic(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_experiment_3_is_deterministic` dengan parameter: self dan tipe kembalian `None`.

Line 217:
Kode:         first = [r.total_kwh for r in research.run_experiment_3()]
Penjelasan: Menetapkan variabel `first` dengan nilai `[r.total_kwh for r in research.run_experiment_3()]`.

Line 218:
Kode:         second = [r.total_kwh for r in research.run_experiment_3()]
Penjelasan: Menetapkan variabel `second` dengan nilai `[r.total_kwh for r in research.run_experiment_3()]`.

Line 219:
Kode:         self.assertEqual(first, second)
Penjelasan: Memanggil `self.assertEqual(first, second)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_experiment_3_is_deterministic`, baris 216-219): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 220:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 221:
Kode:     def test_csv_written(self) -> None:
Penjelasan: Mendefinisikan fungsi `test_csv_written` dengan parameter: self dan tipe kembalian `None`.

Line 222:
Kode:         with tempfile.TemporaryDirectory() as folder:
Penjelasan: Blok with: membuka konteks `tempfile.TemporaryDirectory() as folder` dan menutupnya otomatis setelah blok selesai.

Line 223:
Kode:             path = Path(folder) / "out.csv"
Penjelasan: Menetapkan variabel `path` dengan nilai `Path(folder) / "out.csv"`.

Line 224:
Kode:             research.run_all(csv_path=path)
Penjelasan: Memanggil `research.run_all(csv_path=path)` (hasilnya tidak disimpan; yang penting efeknya).

Line 225:
Kode:             lines = path.read_text(encoding="utf-8").splitlines()
Penjelasan: Menetapkan variabel `lines` dengan nilai `path.read_text(encoding="utf-8").splitlines()`. File handling: membaca/menulis/menyiapkan file data (JSON atau CSV).

Line 226:
Kode:             self.assertEqual(lines[0], "experiment,case,item,metric,value,unit,data_type")
Penjelasan: Memanggil `self.assertEqual(lines[0], "experiment,case,item,metric,value,unit,data_type")` (hasilnya tidak disimpan; yang penting efeknya).

Line 227:
Kode:             self.assertGreater(len(lines), 50)
Penjelasan: Memanggil `self.assertGreater(len(lines), 50)` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `test_csv_written`, baris 221-227): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran.

Line 228:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 229:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 230:
Kode: if __name__ == "__main__":
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `__name__ == "__main__"` bernilai True.

Line 231:
Kode:     unittest.main()
Penjelasan: Memanggil `unittest.main()` (hasilnya tidak disimpan; yang penting efeknya).

~~~~

## tools/generate_line_guide.py

~~~~text
File: tools/generate_line_guide.py

Line 1:
Kode: """Pembuat docs/LINE_BY_LINE_GUIDE.md secara otomatis dari source code final.
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 2:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 3:
Kode: Tujuan file:
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 4:
Kode:     Menjamin nomor baris pada panduan SELALU sama dengan source code. Setiap
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 5:
Kode:     baris dibaca memakai modul `ast` (Standard Library) sehingga penjelasan
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 6:
Kode:     mengacu pada struktur program yang sebenarnya (import, fungsi, parameter,
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 7:
Kode:     return, kondisi, loop, ekspresi Boolean, file handling, exception, dll.).
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 8:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 9:
Kode: Cara pakai (jalankan dari folder proyek, ulangi setiap kali kode berubah):
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 10:
Kode:     python tools/generate_line_guide.py
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 11:
Kode: """
Penjelasan: Bagian docstring modul: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 12:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 13:
Kode: import ast
Penjelasan: Mengimpor modul: ast.

Line 14:
Kode: import re
Penjelasan: Mengimpor modul: re.

Line 15:
Kode: from pathlib import Path
Penjelasan: Mengimpor Path dari modul `pathlib`.

Line 16:
Kode: from typing import Dict, List, Optional, Set, Tuple
Penjelasan: Mengimpor Dict, List, Optional, Set, Tuple dari modul `typing`.

Line 17:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 18:
Kode: ROOT = Path(__file__).resolve().parent.parent
Penjelasan: Menetapkan konstanta/variabel modul `ROOT` dengan nilai `Path(__file__).resolve().parent.parent`.

Line 19:
Kode: OUTPUT = ROOT / "docs" / "LINE_BY_LINE_GUIDE.md"
Penjelasan: Menetapkan konstanta/variabel modul `OUTPUT` dengan nilai `ROOT / "docs" / "LINE_BY_LINE_GUIDE.md"`.

Line 20:
Kode: FENCE = "~~~~"
Penjelasan: Menetapkan konstanta/variabel modul `FENCE` dengan nilai `"~~~~"`.

Line 21:
Kode: COMPOUND = (ast.FunctionDef, ast.ClassDef, ast.If, ast.For, ast.While, ast.Try, ast.With)
Penjelasan: Menetapkan konstanta/variabel modul `COMPOUND` dengan nilai `(ast.FunctionDef, ast.ClassDef, ast.If, ast.For, ast.While, ast.Try, ast.With)`.

Line 22:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 23:
Kode: SOURCE_FILES = [
Penjelasan: Menetapkan konstanta/variabel modul `SOURCE_FILES` dengan nilai `[ "boolean_operations.py", "config.py", "sensors.py", "security.py", "lighting.py", "appliances.py", "energ...`.

Line 24:
Kode:     "boolean_operations.py", "config.py", "sensors.py", "security.py", "lighting.py",
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 23 (`SOURCE_FILES = [`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 25:
Kode:     "appliances.py", "energy_manager.py", "research.py", "main.py",
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 23 (`SOURCE_FILES = [`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 26:
Kode:     "tests/test_boolean_operations.py", "tests/test_security.py", "tests/test_lighting.py",
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 23 (`SOURCE_FILES = [`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 27:
Kode:     "tests/test_appliances.py", "tests/test_energy_manager.py",
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 23 (`SOURCE_FILES = [`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 28:
Kode:     "tools/generate_line_guide.py",
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 23 (`SOURCE_FILES = [`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 29:
Kode: ]
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 23 (`SOURCE_FILES = [`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 30:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 31:
Kode: BOOLEAN_FUNCTIONS = {
Penjelasan: Menetapkan konstanta/variabel modul `BOOLEAN_FUNCTIONS` dengan nilai `{ "boolean_and(": "AND", "boolean_or(": "OR", "boolean_not(": "NOT", "boolean_xor(": "XOR", "boolean_nand("...`.

Line 32:
Kode:     "boolean_and(": "AND", "boolean_or(": "OR", "boolean_not(": "NOT",
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 31 (`BOOLEAN_FUNCTIONS = {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 33:
Kode:     "boolean_xor(": "XOR", "boolean_nand(": "NAND", "boolean_nor(": "NOR",
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 31 (`BOOLEAN_FUNCTIONS = {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 34:
Kode: }
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 31 (`BOOLEAN_FUNCTIONS = {`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 35:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 36:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 37:
Kode: def short(text: str, limit: int = 110) -> str:
Penjelasan: Mendefinisikan fungsi `short` dengan parameter: text: str, limit: int=110 dan tipe kembalian `str`. Tujuan: Memendekkan teks panjang agar penjelasan tetap terbaca.

Line 38:
Kode:     """Memendekkan teks panjang agar penjelasan tetap terbaca."""
Penjelasan: Bagian docstring `short`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 39:
Kode:     text = " ".join(text.split())
Penjelasan: Menetapkan variabel `text` dengan nilai `" ".join(text.split())`.

Line 40:
Kode:     return text if len(text) <= limit else text[: limit - 3] + "..."
Penjelasan: Mengembalikan hasil ekspresi `text if len(text) <= limit else text[: limit - 3] + "..."` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `short`, baris 37-40): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Memendekkan teks panjang agar penjelasan tetap terbaca.

Line 41:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 42:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 43:
Kode: def segment(source: str, node: Optional[ast.AST]) -> str:
Penjelasan: Mendefinisikan fungsi `segment` dengan parameter: source: str, node: Optional[ast.AST] dan tipe kembalian `str`. Tujuan: Mengambil potongan kode sumber suatu node (string kosong bila tidak ada).

Line 44:
Kode:     """Mengambil potongan kode sumber suatu node (string kosong bila tidak ada)."""
Penjelasan: Bagian docstring `segment`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 45:
Kode:     if node is None:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `node is None` bernilai True.

Line 46:
Kode:         return ""
Penjelasan: Mengembalikan hasil ekspresi `""` kepada pemanggil fungsi.

Line 47:
Kode:     return short(ast.get_source_segment(source, node) or "")
Penjelasan: Mengembalikan hasil ekspresi `short(ast.get_source_segment(source, node) or "")` kepada pemanggil fungsi. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Hubungan antarbaris (fungsi `segment`, baris 43-47): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Mengambil potongan kode sumber suatu node (string kosong bila tidak ada).

Line 48:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 49:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 50:
Kode: def first_sentence(doc: Optional[str]) -> str:
Penjelasan: Mendefinisikan fungsi `first_sentence` dengan parameter: doc: Optional[str] dan tipe kembalian `str`. Tujuan: Kalimat/baris pertama sebuah docstring.

Line 51:
Kode:     """Kalimat/baris pertama sebuah docstring."""
Penjelasan: Bagian docstring `first_sentence`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 52:
Kode:     if not doc:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `not doc` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 53:
Kode:         return ""
Penjelasan: Mengembalikan hasil ekspresi `""` kepada pemanggil fungsi.

Line 54:
Kode:     return doc.strip().splitlines()[0].strip()
Penjelasan: Mengembalikan hasil ekspresi `doc.strip().splitlines()[0].strip()` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `first_sentence`, baris 50-54): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Kalimat/baris pertama sebuah docstring.

Line 55:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 56:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 57:
Kode: def extra_notes(code: str) -> str:
Penjelasan: Mendefinisikan fungsi `extra_notes` dengan parameter: code: str dan tipe kembalian `str`. Tujuan: Catatan tambahan: ekspresi Boolean, file handling, dan exception handling.

Line 58:
Kode:     """Catatan tambahan: ekspresi Boolean, file handling, dan exception handling."""
Penjelasan: Bagian docstring `extra_notes`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 59:
Kode:     notes = []
Penjelasan: Menetapkan variabel `notes` dengan nilai `[]`.

Line 60:
Kode:     code = re.sub(r"(\"[^\"]*\"|'[^']*')", '""', code)   # abaikan isi string literal
Penjelasan: Menetapkan variabel `code` dengan nilai `re.sub(r"(\"[^\"]*\"|'[^']*')", '""', code)`.

Line 61:
Kode:     ops = [name for token, name in BOOLEAN_FUNCTIONS.items() if token in code]
Penjelasan: Menetapkan variabel `ops` dengan nilai `[name for token, name in BOOLEAN_FUNCTIONS.items() if token in code]`.

Line 62:
Kode:     if ops:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `ops` bernilai True.

Line 63:
Kode:         notes.append(f"Ekspresi Boolean: memakai operator {', '.join(ops)} dari boolean_operations.py.")
Penjelasan: Memanggil `notes.append(f"Ekspresi Boolean: memakai operator {', '.join(ops)} dari boolean_operations.py.")` (hasilnya tidak disimpan; yang penting efeknya).

Line 64:
Kode:     if any(f" {word} " in f" {code} " for word in ("and", "or")) or " not " in f" {code} " \
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `any(f" {word} " in f" {code} " for word in ("and", "or")) or " not " in f" {code} " \ or code.strip().start...` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 65:
Kode:             or code.strip().startswith("not "):
Penjelasan: Lanjutan header yang dimulai pada baris 64: bagian parameter/kondisi yang ditulis lebih dari satu baris.

Line 66:
Kode:         notes.append("Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).")
Penjelasan: Memanggil `notes.append("Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).")` (hasilnya tidak disimpan; yang penting efeknya).

Line 67:
Kode:     if any(token in code for token in ("read_text", "write_text", "open(", "csv.writer", "writerow",
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `any(token in code for token in ("read_text", "write_text", "open(", "csv.writer", "writerow", "json.loads",...` bernilai True.

Line 68:
Kode:                                        "json.loads", "json.dumps", "mkdir")):
Penjelasan: Lanjutan header yang dimulai pada baris 67: bagian parameter/kondisi yang ditulis lebih dari satu baris.

Line 69:
Kode:         notes.append("File handling: membaca/menulis/menyiapkan file data (JSON atau CSV).")
Penjelasan: Memanggil `notes.append("File handling: membaca/menulis/menyiapkan file data (JSON atau CSV).")` (hasilnya tidak disimpan; yang penting efeknya).

Line 70:
Kode:     if code.strip().startswith(("raise ", "except")) or code.strip() == "try:":
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `code.strip().startswith(("raise ", "except")) or code.strip() == "try:"` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 71:
Kode:         notes.append("Exception handling: menangani atau melaporkan kesalahan agar program tidak berhenti mendadak.")
Penjelasan: Memanggil `notes.append("Exception handling: menangani atau melaporkan kesalahan agar program tidak berhenti mendadak.")` (hasilnya tidak disimpan; yang penting efeknya).

Line 72:
Kode:     return " ".join(notes)
Penjelasan: Mengembalikan hasil ekspresi `" ".join(notes)` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `extra_notes`, baris 57-72): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Catatan tambahan: ekspresi Boolean, file handling, dan exception handling.

Line 73:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 74:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 75:
Kode: def describe_function(node: ast.FunctionDef, source: str) -> str:
Penjelasan: Mendefinisikan fungsi `describe_function` dengan parameter: node: ast.FunctionDef, source: str dan tipe kembalian `str`. Tujuan: Penjelasan baris `def`.

Line 76:
Kode:     """Penjelasan baris `def`."""
Penjelasan: Bagian docstring `describe_function`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 77:
Kode:     args = ast.unparse(node.args) or "(tanpa parameter)"
Penjelasan: Menetapkan variabel `args` dengan nilai `ast.unparse(node.args) or "(tanpa parameter)"`. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 78:
Kode:     returns = f" dan tipe kembalian `{ast.unparse(node.returns)}`" if node.returns else ""
Penjelasan: Menetapkan variabel `returns` dengan nilai `f" dan tipe kembalian `{ast.unparse(node.returns)}`" if node.returns else ""`.

Line 79:
Kode:     purpose = first_sentence(ast.get_docstring(node))
Penjelasan: Menetapkan variabel `purpose` dengan nilai `first_sentence(ast.get_docstring(node))`.

Line 80:
Kode:     text = f"Mendefinisikan fungsi `{node.name}` dengan parameter: {args}{returns}."
Penjelasan: Menetapkan variabel `text` dengan nilai `f"Mendefinisikan fungsi `{node.name}` dengan parameter: {args}{returns}."`.

Line 81:
Kode:     return text + (f" Tujuan: {purpose}" if purpose else "")
Penjelasan: Mengembalikan hasil ekspresi `text + (f" Tujuan: {purpose}" if purpose else "")` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `describe_function`, baris 75-81): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Penjelasan baris `def`.

Line 82:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 83:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 84:
Kode: def describe_statement(node: ast.stmt, source: str, text: str, in_class: bool, at_module: bool) -> str:
Penjelasan: Mendefinisikan fungsi `describe_statement` dengan parameter: node: ast.stmt, source: str, text: str, in_class: bool, at_module: bool dan tipe kembalian `str`. Tujuan: Penjelasan satu pernyataan berdasarkan jenis node AST-nya.

Line 85:
Kode:     """Penjelasan satu pernyataan berdasarkan jenis node AST-nya."""
Penjelasan: Bagian docstring `describe_statement`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 86:
Kode:     if isinstance(node, ast.Import):
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `isinstance(node, ast.Import)` bernilai True.

Line 87:
Kode:         return "Mengimpor modul: " + ", ".join(a.name for a in node.names) + "."
Penjelasan: Mengembalikan hasil ekspresi `"Mengimpor modul: " + ", ".join(a.name for a in node.names) + "."` kepada pemanggil fungsi.

Line 88:
Kode:     if isinstance(node, ast.ImportFrom):
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `isinstance(node, ast.ImportFrom)` bernilai True.

Line 89:
Kode:         names = ", ".join(a.name for a in node.names)
Penjelasan: Menetapkan variabel `names` dengan nilai `", ".join(a.name for a in node.names)`.

Line 90:
Kode:         return f"Mengimpor {names} dari modul `{node.module}`."
Penjelasan: Mengembalikan hasil ekspresi `f"Mengimpor {names} dari modul `{node.module}`."` kepada pemanggil fungsi.

Line 91:
Kode:     if isinstance(node, ast.FunctionDef):
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `isinstance(node, ast.FunctionDef)` bernilai True.

Line 92:
Kode:         return describe_function(node, source)
Penjelasan: Mengembalikan hasil ekspresi `describe_function(node, source)` kepada pemanggil fungsi.

Line 93:
Kode:     if isinstance(node, ast.ClassDef):
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `isinstance(node, ast.ClassDef)` bernilai True.

Line 94:
Kode:         bases = ", ".join(ast.unparse(b) for b in node.bases)
Penjelasan: Menetapkan variabel `bases` dengan nilai `", ".join(ast.unparse(b) for b in node.bases)`.

Line 95:
Kode:         decorators = ", ".join("@" + ast.unparse(d) for d in node.decorator_list)
Penjelasan: Menetapkan variabel `decorators` dengan nilai `", ".join("@" + ast.unparse(d) for d in node.decorator_list)`.

Line 96:
Kode:         purpose = first_sentence(ast.get_docstring(node))
Penjelasan: Menetapkan variabel `purpose` dengan nilai `first_sentence(ast.get_docstring(node))`.

Line 97:
Kode:         extra = (f" turunan {bases}" if bases else "") + (f" dengan dekorator {decorators}" if decorators else "")
Penjelasan: Menetapkan variabel `extra` dengan nilai `(f" turunan {bases}" if bases else "") + (f" dengan dekorator {decorators}" if decorators else "")`.

Line 98:
Kode:         return f"Mendefinisikan class `{node.name}`{extra}." + (f" Tujuan: {purpose}" if purpose else "")
Penjelasan: Mengembalikan hasil ekspresi `f"Mendefinisikan class `{node.name}`{extra}." + (f" Tujuan: {purpose}" if purpose else "")` kepada pemanggil fungsi.

Line 99:
Kode:     if isinstance(node, ast.Return):
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `isinstance(node, ast.Return)` bernilai True.

Line 100:
Kode:         value = segment(source, node.value)
Penjelasan: Menetapkan variabel `value` dengan nilai `segment(source, node.value)`.

Line 101:
Kode:         return f"Mengembalikan hasil ekspresi `{value}` kepada pemanggil fungsi." if value else \
Penjelasan: Mengembalikan hasil ekspresi `f"Mengembalikan hasil ekspresi `{value}` kepada pemanggil fungsi." if value else \ "Keluar dari fungsi tanp...` kepada pemanggil fungsi.

Line 102:
Kode:             "Keluar dari fungsi tanpa nilai (None)."
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 101 (`return f"Mengembalikan hasil ekspresi `{value}` kepada pe...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 103:
Kode:     if isinstance(node, ast.AnnAssign):
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `isinstance(node, ast.AnnAssign)` bernilai True.

Line 104:
Kode:         target = ast.unparse(node.target)
Penjelasan: Menetapkan variabel `target` dengan nilai `ast.unparse(node.target)`.

Line 105:
Kode:         kind = "atribut class" if in_class else "variabel"
Penjelasan: Menetapkan variabel `kind` dengan nilai `"atribut class" if in_class else "variabel"`.

Line 106:
Kode:         default = f" dengan nilai awal `{segment(source, node.value)}`" if node.value else ""
Penjelasan: Menetapkan variabel `default` dengan nilai `f" dengan nilai awal `{segment(source, node.value)}`" if node.value else ""`.

Line 107:
Kode:         return f"Mendeklarasikan {kind} `{target}` bertipe `{ast.unparse(node.annotation)}`{default}."
Penjelasan: Mengembalikan hasil ekspresi `f"Mendeklarasikan {kind} `{target}` bertipe `{ast.unparse(node.annotation)}`{default}."` kepada pemanggil fungsi.

Line 108:
Kode:     if isinstance(node, ast.Assign):
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `isinstance(node, ast.Assign)` bernilai True.

Line 109:
Kode:         targets = ", ".join(ast.unparse(t) for t in node.targets)
Penjelasan: Menetapkan variabel `targets` dengan nilai `", ".join(ast.unparse(t) for t in node.targets)`.

Line 110:
Kode:         kind = "konstanta/variabel modul" if at_module else "variabel"
Penjelasan: Menetapkan variabel `kind` dengan nilai `"konstanta/variabel modul" if at_module else "variabel"`.

Line 111:
Kode:         return f"Menetapkan {kind} `{targets}` dengan nilai `{segment(source, node.value)}`."
Penjelasan: Mengembalikan hasil ekspresi `f"Menetapkan {kind} `{targets}` dengan nilai `{segment(source, node.value)}`."` kepada pemanggil fungsi.

Line 112:
Kode:     if isinstance(node, ast.AugAssign):
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `isinstance(node, ast.AugAssign)` bernilai True.

Line 113:
Kode:         return f"Memperbarui `{ast.unparse(node.target)}` dengan operasi `{type(node.op).__name__}` terhadap `{segment(source, node.value)}`."
Penjelasan: Mengembalikan hasil ekspresi `f"Memperbarui `{ast.unparse(node.target)}` dengan operasi `{type(node.op).__name__}` terhadap `{segment(sou...` kepada pemanggil fungsi.

Line 114:
Kode:     if isinstance(node, ast.If):
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `isinstance(node, ast.If)` bernilai True.

Line 115:
Kode:         kind = "Percabangan alternatif (elif)" if text.lstrip().startswith("elif") else "Percabangan (if)"
Penjelasan: Menetapkan variabel `kind` dengan nilai `"Percabangan alternatif (elif)" if text.lstrip().startswith("elif") else "Percabangan (if)"`.

Line 116:
Kode:         return f"{kind}: blok di bawahnya hanya dijalankan jika kondisi `{segment(source, node.test)}` bernilai True."
Penjelasan: Mengembalikan hasil ekspresi `f"{kind}: blok di bawahnya hanya dijalankan jika kondisi `{segment(source, node.test)}` bernilai True."` kepada pemanggil fungsi.

Line 117:
Kode:     if isinstance(node, ast.For):
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `isinstance(node, ast.For)` bernilai True.

Line 118:
Kode:         return (f"Perulangan for: variabel `{ast.unparse(node.target)}` mengambil tiap elemen dari "
Penjelasan: Mengembalikan hasil ekspresi `f"Perulangan for: variabel `{ast.unparse(node.target)}` mengambil tiap elemen dari " f"`{segment(source, no...` kepada pemanggil fungsi.

Line 119:
Kode:                 f"`{segment(source, node.iter)}`, dan blok di bawahnya diulang untuk tiap elemen.")
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 118 (`return (f"Perulangan for: variabel `{ast.unparse(node.tar...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 120:
Kode:     if isinstance(node, ast.While):
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `isinstance(node, ast.While)` bernilai True.

Line 121:
Kode:         return f"Perulangan while: blok di bawahnya diulang selama `{segment(source, node.test)}` bernilai True."
Penjelasan: Mengembalikan hasil ekspresi `f"Perulangan while: blok di bawahnya diulang selama `{segment(source, node.test)}` bernilai True."` kepada pemanggil fungsi.

Line 122:
Kode:     if isinstance(node, ast.Try):
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `isinstance(node, ast.Try)` bernilai True.

Line 123:
Kode:         return "Awal blok try: kode di bawahnya dijalankan dan kesalahan yang mungkin muncul ditangkap oleh blok except."
Penjelasan: Mengembalikan hasil ekspresi `"Awal blok try: kode di bawahnya dijalankan dan kesalahan yang mungkin muncul ditangkap oleh blok except."` kepada pemanggil fungsi.

Line 124:
Kode:     if isinstance(node, ast.With):
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `isinstance(node, ast.With)` bernilai True.

Line 125:
Kode:         items = ", ".join(ast.unparse(i) for i in node.items)
Penjelasan: Menetapkan variabel `items` dengan nilai `", ".join(ast.unparse(i) for i in node.items)`.

Line 126:
Kode:         return f"Blok with: membuka konteks `{items}` dan menutupnya otomatis setelah blok selesai."
Penjelasan: Mengembalikan hasil ekspresi `f"Blok with: membuka konteks `{items}` dan menutupnya otomatis setelah blok selesai."` kepada pemanggil fungsi.

Line 127:
Kode:     if isinstance(node, ast.Raise):
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `isinstance(node, ast.Raise)` bernilai True.

Line 128:
Kode:         return f"Melempar exception `{segment(source, node.exc)}` untuk melaporkan kondisi tidak valid."
Penjelasan: Mengembalikan hasil ekspresi `f"Melempar exception `{segment(source, node.exc)}` untuk melaporkan kondisi tidak valid."` kepada pemanggil fungsi.

Line 129:
Kode:     if isinstance(node, ast.Assert):
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `isinstance(node, ast.Assert)` bernilai True.

Line 130:
Kode:         return f"Memastikan kondisi `{segment(source, node.test)}` benar."
Penjelasan: Mengembalikan hasil ekspresi `f"Memastikan kondisi `{segment(source, node.test)}` benar."` kepada pemanggil fungsi.

Line 131:
Kode:     if isinstance(node, ast.Pass):
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `isinstance(node, ast.Pass)` bernilai True.

Line 132:
Kode:         return "Pernyataan kosong; tidak melakukan apa pun."
Penjelasan: Mengembalikan hasil ekspresi `"Pernyataan kosong; tidak melakukan apa pun."` kepada pemanggil fungsi.

Line 133:
Kode:     if isinstance(node, ast.Break):
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `isinstance(node, ast.Break)` bernilai True.

Line 134:
Kode:         return "Menghentikan perulangan terdekat."
Penjelasan: Mengembalikan hasil ekspresi `"Menghentikan perulangan terdekat."` kepada pemanggil fungsi.

Line 135:
Kode:     if isinstance(node, ast.Continue):
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `isinstance(node, ast.Continue)` bernilai True.

Line 136:
Kode:         return "Melanjutkan ke iterasi berikutnya pada perulangan terdekat."
Penjelasan: Mengembalikan hasil ekspresi `"Melanjutkan ke iterasi berikutnya pada perulangan terdekat."` kepada pemanggil fungsi.

Line 137:
Kode:     if isinstance(node, ast.Expr):
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `isinstance(node, ast.Expr)` bernilai True.

Line 138:
Kode:         if isinstance(node.value, ast.Call):
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `isinstance(node.value, ast.Call)` bernilai True.

Line 139:
Kode:             return f"Memanggil `{segment(source, node.value)}` (hasilnya tidak disimpan; yang penting efeknya)."
Penjelasan: Mengembalikan hasil ekspresi `f"Memanggil `{segment(source, node.value)}` (hasilnya tidak disimpan; yang penting efeknya)."` kepada pemanggil fungsi.

Line 140:
Kode:         return f"Ekspresi `{segment(source, node.value)}`."
Penjelasan: Mengembalikan hasil ekspresi `f"Ekspresi `{segment(source, node.value)}`."` kepada pemanggil fungsi.

Line 141:
Kode:     return f"Pernyataan `{short(text.strip())}`."
Penjelasan: Mengembalikan hasil ekspresi `f"Pernyataan `{short(text.strip())}`."` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `describe_statement`, baris 84-141): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Penjelasan satu pernyataan berdasarkan jenis node AST-nya.

Line 142:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 143:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 144:
Kode: def analyse(source: str) -> Tuple[Dict[int, ast.stmt], Dict[int, str], Dict[int, ast.AST], Set[int], List[ast.AST]]:
Penjelasan: Mendefinisikan fungsi `analyse` dengan parameter: source: str dan tipe kembalian `Tuple[Dict[int, ast.stmt], Dict[int, str], Dict[int, ast.AST], Set[int], List[ast.AST]]`. Tujuan: Membangun peta baris -> node, docstring, dan daftar blok fungsi/class dari AST.

Line 145:
Kode:     """Membangun peta baris -> node, docstring, dan daftar blok fungsi/class dari AST."""
Penjelasan: Bagian docstring `analyse`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 146:
Kode:     tree = ast.parse(source)
Penjelasan: Menetapkan variabel `tree` dengan nilai `ast.parse(source)`.

Line 147:
Kode:     starts: Dict[int, ast.stmt] = {}
Penjelasan: Mendeklarasikan variabel `starts` bertipe `Dict[int, ast.stmt]` dengan nilai awal `{}`.

Line 148:
Kode:     docstring_lines: Dict[int, str] = {}
Penjelasan: Mendeklarasikan variabel `docstring_lines` bertipe `Dict[int, str]` dengan nilai awal `{}`.

Line 149:
Kode:     simple_spans: List[ast.stmt] = []
Penjelasan: Mendeklarasikan variabel `simple_spans` bertipe `List[ast.stmt]` dengan nilai awal `[]`.

Line 150:
Kode:     blocks: List[ast.AST] = []
Penjelasan: Mendeklarasikan variabel `blocks` bertipe `List[ast.AST]` dengan nilai awal `[]`.

Line 151:
Kode:     parents: Dict[ast.AST, ast.AST] = {}
Penjelasan: Mendeklarasikan variabel `parents` bertipe `Dict[ast.AST, ast.AST]` dengan nilai awal `{}`.

Line 152:
Kode:     for parent in ast.walk(tree):
Penjelasan: Perulangan for: variabel `parent` mengambil tiap elemen dari `ast.walk(tree)`, dan blok di bawahnya diulang untuk tiap elemen.

Line 153:
Kode:         for child in ast.iter_child_nodes(parent):
Penjelasan: Perulangan for: variabel `child` mengambil tiap elemen dari `ast.iter_child_nodes(parent)`, dan blok di bawahnya diulang untuk tiap elemen.

Line 154:
Kode:             parents[child] = parent
Penjelasan: Menetapkan variabel `parents[child]` dengan nilai `parent`.

Line 155:
Kode:     for node in ast.walk(tree):
Penjelasan: Perulangan for: variabel `node` mengambil tiap elemen dari `ast.walk(tree)`, dan blok di bawahnya diulang untuk tiap elemen.

Line 156:
Kode:         if not isinstance(node, ast.stmt):
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `not isinstance(node, ast.stmt)` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 157:
Kode:             continue
Penjelasan: Melanjutkan ke iterasi berikutnya pada perulangan terdekat.

Line 158:
Kode:         parent = parents.get(node)
Penjelasan: Menetapkan variabel `parent` dengan nilai `parents.get(node)`.

Line 159:
Kode:         is_doc = (isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant)
Penjelasan: Menetapkan variabel `is_doc` dengan nilai `isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) and isinstance(node.value.value, str) a...`. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 160:
Kode:                   and isinstance(node.value.value, str)
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 159 (`is_doc = (isinstance(node, ast.Expr) and isinstance(node....`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 161:
Kode:                   and isinstance(parent, (ast.Module, ast.FunctionDef, ast.ClassDef))
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 159 (`is_doc = (isinstance(node, ast.Expr) and isinstance(node....`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 162:
Kode:                   and parent.body and parent.body[0] is node)
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 159 (`is_doc = (isinstance(node, ast.Expr) and isinstance(node....`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 163:
Kode:         if is_doc:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `is_doc` bernilai True.

Line 164:
Kode:             owner = "modul" if isinstance(parent, ast.Module) else f"`{parent.name}`"
Penjelasan: Menetapkan variabel `owner` dengan nilai `"modul" if isinstance(parent, ast.Module) else f"`{parent.name}`"`.

Line 165:
Kode:             for line in range(node.lineno, node.end_lineno + 1):
Penjelasan: Perulangan for: variabel `line` mengambil tiap elemen dari `range(node.lineno, node.end_lineno + 1)`, dan blok di bawahnya diulang untuk tiap elemen.

Line 166:
Kode:                 docstring_lines[line] = owner
Penjelasan: Menetapkan variabel `docstring_lines[line]` dengan nilai `owner`.

Line 167:
Kode:             continue
Penjelasan: Melanjutkan ke iterasi berikutnya pada perulangan terdekat.

Line 168:
Kode:         starts.setdefault(node.lineno, node)
Penjelasan: Memanggil `starts.setdefault(node.lineno, node)` (hasilnya tidak disimpan; yang penting efeknya).

Line 169:
Kode:         if not isinstance(node, COMPOUND):
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `not isinstance(node, COMPOUND)` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 170:
Kode:             simple_spans.append(node)
Penjelasan: Memanggil `simple_spans.append(node)` (hasilnya tidak disimpan; yang penting efeknya).

Line 171:
Kode:         if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `isinstance(node, (ast.FunctionDef, ast.ClassDef))` bernilai True.

Line 172:
Kode:             blocks.append(node)
Penjelasan: Memanggil `blocks.append(node)` (hasilnya tidak disimpan; yang penting efeknya).

Line 173:
Kode:     return starts, docstring_lines, parents, set(), blocks + simple_spans
Penjelasan: Mengembalikan hasil ekspresi `starts, docstring_lines, parents, set(), blocks + simple_spans` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `analyse`, baris 144-173): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Membangun peta baris -> node, docstring, dan daftar blok fungsi/class dari AST.

Line 174:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 175:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 176:
Kode: def explain_file(relative: str) -> List[str]:
Penjelasan: Mendefinisikan fungsi `explain_file` dengan parameter: relative: str dan tipe kembalian `List[str]`. Tujuan: Membuat seluruh entri penjelasan untuk satu file Python.

Line 177:
Kode:     """Membuat seluruh entri penjelasan untuk satu file Python."""
Penjelasan: Bagian docstring `explain_file`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 178:
Kode:     path = ROOT / relative
Penjelasan: Menetapkan variabel `path` dengan nilai `ROOT / relative`.

Line 179:
Kode:     source = path.read_text(encoding="utf-8")
Penjelasan: Menetapkan variabel `source` dengan nilai `path.read_text(encoding="utf-8")`. File handling: membaca/menulis/menyiapkan file data (JSON atau CSV).

Line 180:
Kode:     lines = source.splitlines()
Penjelasan: Menetapkan variabel `lines` dengan nilai `source.splitlines()`.

Line 181:
Kode:     out = [f"File: {relative}", ""]
Penjelasan: Menetapkan variabel `out` dengan nilai `[f"File: {relative}", ""]`.

Line 182:
Kode:     if not lines:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `not lines` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 183:
Kode:         out += ["(File kosong: sengaja kosong agar folder `tests` dikenali sebagai package.)", ""]
Penjelasan: Memperbarui `out` dengan operasi `Add` terhadap `["(File kosong: sengaja kosong agar folder `tests` dikenali sebagai package.)", ""]`.

Line 184:
Kode:         return out
Penjelasan: Mengembalikan hasil ekspresi `out` kepada pemanggil fungsi.

Line 185:
Kode:     tree = ast.parse(source)
Penjelasan: Menetapkan variabel `tree` dengan nilai `ast.parse(source)`.

Line 186:
Kode:     starts, docstring_lines, parents, _, extra = analyse(source)
Penjelasan: Menetapkan variabel `(starts, docstring_lines, parents, _, extra)` dengan nilai `analyse(source)`.

Line 187:
Kode:     simple = [n for n in extra if not isinstance(n, (ast.FunctionDef, ast.ClassDef))]
Penjelasan: Menetapkan variabel `simple` dengan nilai `[n for n in extra if not isinstance(n, (ast.FunctionDef, ast.ClassDef))]`. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 188:
Kode:     block_ends = {n.end_lineno: n for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.ClassDef))}
Penjelasan: Menetapkan variabel `block_ends` dengan nilai `{n.end_lineno: n for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.ClassDef))}`.

Line 189:
Kode:     for number, raw in enumerate(lines, 1):
Penjelasan: Perulangan for: variabel `(number, raw)` mengambil tiap elemen dari `enumerate(lines, 1)`, dan blok di bawahnya diulang untuk tiap elemen.

Line 190:
Kode:         text = raw.rstrip()
Penjelasan: Menetapkan variabel `text` dengan nilai `raw.rstrip()`.

Line 191:
Kode:         stripped = text.strip()
Penjelasan: Menetapkan variabel `stripped` dengan nilai `text.strip()`.

Line 192:
Kode:         if not stripped:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `not stripped` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 193:
Kode:             note = "Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi."
Penjelasan: Menetapkan variabel `note` dengan nilai `"Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi."`.

Line 194:
Kode:         elif number in docstring_lines:
Penjelasan: Percabangan alternatif (elif): blok di bawahnya hanya dijalankan jika kondisi `number in docstring_lines` bernilai True.

Line 195:
Kode:             note = (f"Bagian docstring {docstring_lines[number]}: dokumentasi (bukan logika program) "
Penjelasan: Menetapkan variabel `note` dengan nilai `f"Bagian docstring {docstring_lines[number]}: dokumentasi (bukan logika program) " "yang menjelaskan tujuan...`.

Line 196:
Kode:                     "yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.")
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 195 (`note = (f"Bagian docstring {docstring_lines[number]}: dok...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 197:
Kode:         elif stripped.startswith("#"):
Penjelasan: Percabangan alternatif (elif): blok di bawahnya hanya dijalankan jika kondisi `stripped.startswith("#")` bernilai True.

Line 198:
Kode:             note = "Komentar: penjelasan untuk pembaca, tidak dieksekusi Python."
Penjelasan: Menetapkan variabel `note` dengan nilai `"Komentar: penjelasan untuk pembaca, tidak dieksekusi Python."`.

Line 199:
Kode:         elif number in starts:
Penjelasan: Percabangan alternatif (elif): blok di bawahnya hanya dijalankan jika kondisi `number in starts` bernilai True.

Line 200:
Kode:             node = starts[number]
Penjelasan: Menetapkan variabel `node` dengan nilai `starts[number]`.

Line 201:
Kode:             parent = parents.get(node)
Penjelasan: Menetapkan variabel `parent` dengan nilai `parents.get(node)`.

Line 202:
Kode:             note = describe_statement(node, source, text, isinstance(parent, ast.ClassDef),
Penjelasan: Menetapkan variabel `note` dengan nilai `describe_statement(node, source, text, isinstance(parent, ast.ClassDef), isinstance(parent, ast.Module))`.

Line 203:
Kode:                                       isinstance(parent, ast.Module))
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 202 (`note = describe_statement(node, source, text, isinstance(...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 204:
Kode:             extra_note = "" if isinstance(node, (ast.FunctionDef, ast.ClassDef)) else extra_notes(text)
Penjelasan: Menetapkan variabel `extra_note` dengan nilai `"" if isinstance(node, (ast.FunctionDef, ast.ClassDef)) else extra_notes(text)`.

Line 205:
Kode:             if extra_note:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `extra_note` bernilai True.

Line 206:
Kode:                 note += " " + extra_note
Penjelasan: Memperbarui `note` dengan operasi `Add` terhadap `" " + extra_note`.

Line 207:
Kode:         elif stripped.startswith("@"):
Penjelasan: Percabangan alternatif (elif): blok di bawahnya hanya dijalankan jika kondisi `stripped.startswith("@")` bernilai True.

Line 208:
Kode:             note = f"Dekorator `{stripped}`: memodifikasi class/fungsi di bawahnya (mis. membuat dataclass)."
Penjelasan: Menetapkan variabel `note` dengan nilai `f"Dekorator `{stripped}`: memodifikasi class/fungsi di bawahnya (mis. membuat dataclass)."`.

Line 209:
Kode:         elif stripped.startswith("else:"):
Penjelasan: Percabangan alternatif (elif): blok di bawahnya hanya dijalankan jika kondisi `stripped.startswith("else:")` bernilai True.

Line 210:
Kode:             note = "Cabang else: dijalankan bila semua kondisi if/elif/for di atasnya tidak terpenuhi."
Penjelasan: Menetapkan variabel `note` dengan nilai `"Cabang else: dijalankan bila semua kondisi if/elif/for di atasnya tidak terpenuhi."`.

Line 211:
Kode:         elif stripped.startswith("except"):
Penjelasan: Percabangan alternatif (elif): blok di bawahnya hanya dijalankan jika kondisi `stripped.startswith("except")` bernilai True.

Line 212:
Kode:             note = (f"Penangkap kesalahan `{short(stripped)}`: dijalankan bila blok try melempar exception "
Penjelasan: Menetapkan variabel `note` dengan nilai `f"Penangkap kesalahan `{short(stripped)}`: dijalankan bila blok try melempar exception " "yang sesuai, sehi...`.

Line 213:
Kode:                     "yang sesuai, sehingga program tidak berhenti mendadak.")
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 212 (`note = (f"Penangkap kesalahan `{short(stripped)}`: dijala...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 214:
Kode:         elif stripped.startswith("finally"):
Penjelasan: Percabangan alternatif (elif): blok di bawahnya hanya dijalankan jika kondisi `stripped.startswith("finally")` bernilai True.

Line 215:
Kode:             note = "Blok finally: selalu dijalankan setelah try/except."
Penjelasan: Menetapkan variabel `note` dengan nilai `"Blok finally: selalu dijalankan setelah try/except."`.

Line 216:
Kode:         else:
Penjelasan: Cabang else: dijalankan bila semua kondisi if/elif/for di atasnya tidak terpenuhi.

Line 217:
Kode:             owner = next((n for n in simple if n.lineno < number <= n.end_lineno), None)
Penjelasan: Menetapkan variabel `owner` dengan nilai `next((n for n in simple if n.lineno < number <= n.end_lineno), None)`.

Line 218:
Kode:             if owner is not None:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `owner is not None` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 219:
Kode:                 note = (f"Lanjutan dari pernyataan yang dimulai pada baris {owner.lineno} "
Penjelasan: Menetapkan variabel `note` dengan nilai `f"Lanjutan dari pernyataan yang dimulai pada baris {owner.lineno} " f"(`{short(lines[owner.lineno - 1].stri...`.

Line 220:
Kode:                         f"(`{short(lines[owner.lineno - 1].strip(), 60)}`): bagian ini adalah elemen/argumen/"
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 219 (`note = (f"Lanjutan dari pernyataan yang dimulai pada bari...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 221:
Kode:                         "ekspresi yang memperpanjang pernyataan tersebut.")
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 219 (`note = (f"Lanjutan dari pernyataan yang dimulai pada bari...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 222:
Kode:                 extra_note = extra_notes(text)
Penjelasan: Menetapkan variabel `extra_note` dengan nilai `extra_notes(text)`.

Line 223:
Kode:                 if extra_note:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `extra_note` bernilai True.

Line 224:
Kode:                     note += " " + extra_note
Penjelasan: Memperbarui `note` dengan operasi `Add` terhadap `" " + extra_note`.

Line 225:
Kode:             else:
Penjelasan: Cabang else: dijalankan bila semua kondisi if/elif/for di atasnya tidak terpenuhi.

Line 226:
Kode:                 header = next((n for n in ast.walk(tree) if isinstance(n, COMPOUND)
Penjelasan: Menetapkan variabel `header` dengan nilai `next((n for n in ast.walk(tree) if isinstance(n, COMPOUND) and n.lineno < number < n.body[0].lineno), None)`.

Line 227:
Kode:                                and n.lineno < number < n.body[0].lineno), None)
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 226 (`header = next((n for n in ast.walk(tree) if isinstance(n,...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 228:
Kode:                 if header is not None:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `header is not None` bernilai True. Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).

Line 229:
Kode:                     note = (f"Lanjutan header yang dimulai pada baris {header.lineno}: "
Penjelasan: Menetapkan variabel `note` dengan nilai `f"Lanjutan header yang dimulai pada baris {header.lineno}: " "bagian parameter/kondisi yang ditulis lebih d...`.

Line 230:
Kode:                             "bagian parameter/kondisi yang ditulis lebih dari satu baris.")
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 229 (`note = (f"Lanjutan header yang dimulai pada baris {header...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 231:
Kode:                 else:
Penjelasan: Cabang else: dijalankan bila semua kondisi if/elif/for di atasnya tidak terpenuhi.

Line 232:
Kode:                     note = "Lanjutan dari pernyataan di atasnya."
Penjelasan: Menetapkan variabel `note` dengan nilai `"Lanjutan dari pernyataan di atasnya."`.

Line 233:
Kode:         out += [f"Line {number}:", f"Kode: {text}", f"Penjelasan: {note}", ""]
Penjelasan: Memperbarui `out` dengan operasi `Add` terhadap `[f"Line {number}:", f"Kode: {text}", f"Penjelasan: {note}", ""]`.

Line 234:
Kode:         if number in block_ends:
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `number in block_ends` bernilai True.

Line 235:
Kode:             block = block_ends[number]
Penjelasan: Menetapkan variabel `block` dengan nilai `block_ends[number]`.

Line 236:
Kode:             kind = "class" if isinstance(block, ast.ClassDef) else "fungsi"
Penjelasan: Menetapkan variabel `kind` dengan nilai `"class" if isinstance(block, ast.ClassDef) else "fungsi"`.

Line 237:
Kode:             purpose = first_sentence(ast.get_docstring(block))
Penjelasan: Menetapkan variabel `purpose` dengan nilai `first_sentence(ast.get_docstring(block))`.

Line 238:
Kode:             out += [(f"Hubungan antarbaris ({kind} `{block.name}`, baris {block.lineno}-{block.end_lineno}): "
Penjelasan: Memperbarui `out` dengan operasi `Add` terhadap `[(f"Hubungan antarbaris ({kind} `{block.name}`, baris {block.lineno}-{block.end_lineno}): " f"baris pertama...`.

Line 239:
Kode:                      f"baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan "
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 238 (`out += [(f"Hubungan antarbaris ({kind} `{block.name}`, ba...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 240:
Kode:                      f"dari atas ke bawah, lalu return/raise menentukan keluaran."
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 238 (`out += [(f"Hubungan antarbaris ({kind} `{block.name}`, ba...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 241:
Kode:                      + (f" Tujuan blok: {purpose}" if purpose else "")), ""]
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 238 (`out += [(f"Hubungan antarbaris ({kind} `{block.name}`, ba...`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 242:
Kode:     return out
Penjelasan: Mengembalikan hasil ekspresi `out` kepada pemanggil fungsi.

Hubungan antarbaris (fungsi `explain_file`, baris 176-242): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Membuat seluruh entri penjelasan untuk satu file Python.

Line 243:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 244:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 245:
Kode: def main() -> None:
Penjelasan: Mendefinisikan fungsi `main` dengan parameter: (tanpa parameter) dan tipe kembalian `None`. Tujuan: Menyusun seluruh panduan dan menulisnya ke docs/LINE_BY_LINE_GUIDE.md.

Line 246:
Kode:     """Menyusun seluruh panduan dan menulisnya ke docs/LINE_BY_LINE_GUIDE.md."""
Penjelasan: Bagian docstring `main`: dokumentasi (bukan logika program) yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.

Line 247:
Kode:     parts = [
Penjelasan: Menetapkan variabel `parts` dengan nilai `[ "# Line-by-Line Guide", "", "Panduan ini dibuat OTOMATIS oleh `tools/generate_line_guide.py` dari source ...`.

Line 248:
Kode:         "# Line-by-Line Guide", "",
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 247 (`parts = [`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 249:
Kode:         "Panduan ini dibuat OTOMATIS oleh `tools/generate_line_guide.py` dari source code final, sehingga",
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 247 (`parts = [`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 250:
Kode:         "nomor baris selalu cocok. **Jalankan ulang generator setiap kali source code berubah.**", "",
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 247 (`parts = [`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 251:
Kode:         "Cara membaca: setiap entri berisi nomor baris, kode asli, dan penjelasan. Penjelasan disusun dari",
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 247 (`parts = [`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 252:
Kode:         "struktur program (AST): jenis pernyataan, nama variabel/fungsi, parameter, ekspresi, serta tujuan",
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 247 (`parts = [`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 253:
Kode:         "fungsi yang diambil dari docstring-nya. Setelah setiap fungsi/class ada paragraf *Hubungan antarbaris*.", "",
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 247 (`parts = [`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 254:
Kode:         "Perintah: `python tools/generate_line_guide.py`", "",
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 247 (`parts = [`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 255:
Kode:     ]
Penjelasan: Lanjutan dari pernyataan yang dimulai pada baris 247 (`parts = [`): bagian ini adalah elemen/argumen/ekspresi yang memperpanjang pernyataan tersebut.

Line 256:
Kode:     for relative in SOURCE_FILES:
Penjelasan: Perulangan for: variabel `relative` mengambil tiap elemen dari `SOURCE_FILES`, dan blok di bawahnya diulang untuk tiap elemen.

Line 257:
Kode:         parts += [f"## {relative}", "", FENCE + "text"]
Penjelasan: Memperbarui `parts` dengan operasi `Add` terhadap `[f"## {relative}", "", FENCE + "text"]`.

Line 258:
Kode:         parts += explain_file(relative)
Penjelasan: Memperbarui `parts` dengan operasi `Add` terhadap `explain_file(relative)`.

Line 259:
Kode:         parts += [FENCE, ""]
Penjelasan: Memperbarui `parts` dengan operasi `Add` terhadap `[FENCE, ""]`.

Line 260:
Kode:     OUTPUT.write_text("\n".join(parts), encoding="utf-8")
Penjelasan: Memanggil `OUTPUT.write_text("\n".join(parts), encoding="utf-8")` (hasilnya tidak disimpan; yang penting efeknya). File handling: membaca/menulis/menyiapkan file data (JSON atau CSV).

Line 261:
Kode:     total = sum(len((ROOT / f).read_text(encoding="utf-8").splitlines()) for f in SOURCE_FILES)
Penjelasan: Menetapkan variabel `total` dengan nilai `sum(len((ROOT / f).read_text(encoding="utf-8").splitlines()) for f in SOURCE_FILES)`. File handling: membaca/menulis/menyiapkan file data (JSON atau CSV).

Line 262:
Kode:     print(f"Ditulis: {OUTPUT} ({total} baris kode dijelaskan)")
Penjelasan: Memanggil `print(f"Ditulis: {OUTPUT} ({total} baris kode dijelaskan)")` (hasilnya tidak disimpan; yang penting efeknya).

Hubungan antarbaris (fungsi `main`, baris 245-262): baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan dari atas ke bawah, lalu return/raise menentukan keluaran. Tujuan blok: Menyusun seluruh panduan dan menulisnya ke docs/LINE_BY_LINE_GUIDE.md.

Line 263:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 264:
Kode: 
Penjelasan: Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi.

Line 265:
Kode: if __name__ == "__main__":
Penjelasan: Percabangan (if): blok di bawahnya hanya dijalankan jika kondisi `__name__ == "__main__"` bernilai True.

Line 266:
Kode:     main()
Penjelasan: Memanggil `main()` (hasilnya tidak disimpan; yang penting efeknya).

~~~~
