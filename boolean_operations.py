"""Modul operator Boolean.

Tujuan file:
    Menyediakan enam operator Boolean (AND, OR, NOT, XOR, NAND, NOR) sebagai
    fungsi terpisah, ditambah utilitas tabel kebenaran dan nilai referensi
    aritmetika 0/1 yang dipakai untuk validasi pada mini research.

Semua modul lain WAJIB memakai fungsi di sini untuk keputusan logika sistem,
sehingga seluruh logika Boolean proyek berada di satu tempat.
"""

from itertools import product
from typing import Callable, Dict, List, Tuple

OPERATOR_NAMES: Tuple[str, ...] = ("AND", "OR", "NOT", "XOR", "NAND", "NOR")


def boolean_and(a: bool, b: bool) -> bool:
    """AND: TRUE hanya jika kedua masukan TRUE.

    Rumus: A AND B. Dipakai pada syarat alarm dan lampu otomatis.
    """
    return bool(a and b)


def boolean_or(a: bool, b: bool) -> bool:
    """OR: TRUE jika minimal satu masukan TRUE.

    Rumus: A OR B. Dipakai untuk mendeteksi aktivitas pintu ATAU gerak.
    """
    return bool(a or b)


def boolean_not(a: bool) -> bool:
    """NOT: membalik nilai masukan (TRUE menjadi FALSE dan sebaliknya)."""
    return not a


def boolean_xor(a: bool, b: bool) -> bool:
    """XOR: TRUE jika kedua masukan BERBEDA.

    Definisi: (A AND NOT B) OR (NOT A AND B), yang setara dengan A != B untuk bool.
    Dipakai membandingkan dua sensor pintu redundan.
    """
    return bool(a) != bool(b)


def boolean_nand(a: bool, b: bool) -> bool:
    """NAND: kebalikan AND; FALSE hanya jika kedua masukan TRUE."""
    return not (a and b)


def boolean_nor(a: bool, b: bool) -> bool:
    """NOR: kebalikan OR; TRUE hanya jika kedua masukan FALSE."""
    return not (a or b)


BINARY_OPERATORS: Dict[str, Callable[[bool, bool], bool]] = {
    "AND": boolean_and,
    "OR": boolean_or,
    "XOR": boolean_xor,
    "NAND": boolean_nand,
    "NOR": boolean_nor,
}


def operator_arity(name: str) -> int:
    """Mengembalikan jumlah masukan operator (1 untuk NOT, 2 untuk lainnya).

    Raises:
        ValueError: jika nama operator tidak dikenal.
    """
    key = name.strip().upper()
    if key == "NOT":
        return 1
    if key in BINARY_OPERATORS:
        return 2
    raise ValueError(f"Operator tidak dikenal: {name!r}")


def evaluate_operator(name: str, *inputs: bool) -> bool:
    """Menjalankan operator berdasarkan nama.

    Args:
        name: nama operator (AND, OR, NOT, XOR, NAND, NOR).
        *inputs: nilai bool; jumlahnya harus sesuai arity operator.

    Raises:
        ValueError: nama tidak dikenal atau jumlah masukan salah.
    """
    key = name.strip().upper()
    if len(inputs) != operator_arity(key):
        raise ValueError(f"Operator {key} membutuhkan {operator_arity(key)} masukan.")
    if key == "NOT":
        return boolean_not(inputs[0])
    return BINARY_OPERATORS[key](inputs[0], inputs[1])


def reference_result(name: str, inputs: Tuple[bool, ...]) -> bool:
    """Nilai referensi independen memakai aritmetika bilangan bulat 0/1.

    Dipakai sebagai 'jawaban benar' pada validasi, sengaja TIDAK memakai
    operator Python and/or/not agar validasi tidak membandingkan kode dengan dirinya sendiri.
    """
    key = name.strip().upper()
    bits = [int(x) for x in inputs]
    if key == "NOT":
        return (1 - bits[0]) == 1
    a, b = bits
    table = {
        "AND": a * b,
        "OR": min(1, a + b),
        "XOR": (a + b) % 2,
        "NAND": 1 - a * b,
        "NOR": 1 - min(1, a + b),
    }
    return table[key] == 1


def input_combinations(name: str) -> List[Tuple[bool, ...]]:
    """Seluruh kombinasi masukan operator, urut dari (False, ...) ke (True, ...)."""
    return list(product([False, True], repeat=operator_arity(name)))


def truth_table(name: str) -> List[Tuple[Tuple[bool, ...], bool]]:
    """Tabel kebenaran operator: daftar pasangan (masukan, keluaran)."""
    return [(inputs, evaluate_operator(name, *inputs)) for inputs in input_combinations(name)]


def format_truth_table(name: str) -> str:
    """Membuat teks tabel kebenaran (1 = TRUE, 0 = FALSE) untuk dicetak di terminal."""
    key = name.strip().upper()
    heads = ["A"] if operator_arity(key) == 1 else ["A", "B"]
    lines = [" ".join(heads) + f" | {key}", "-" * (2 * len(heads) + 3 + len(key))]
    for inputs, output in truth_table(key):
        lines.append(" ".join(str(int(x)) for x in inputs) + f" | {int(output)}")
    return "\n".join(lines)
