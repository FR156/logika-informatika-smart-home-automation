"""Pembuat docs/LINE_BY_LINE_GUIDE.md secara otomatis dari source code final.

Tujuan file:
    Menjamin nomor baris pada panduan SELALU sama dengan source code. Setiap
    baris dibaca memakai modul `ast` (Standard Library) sehingga penjelasan
    mengacu pada struktur program yang sebenarnya (import, fungsi, parameter,
    return, kondisi, loop, ekspresi Boolean, file handling, exception, dll.).

Cara pakai (jalankan dari folder proyek, ulangi setiap kali kode berubah):
    python tools/generate_line_guide.py
"""

import ast
import re
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "docs" / "LINE_BY_LINE_GUIDE.md"
FENCE = "~~~~"
COMPOUND = (ast.FunctionDef, ast.ClassDef, ast.If, ast.For, ast.While, ast.Try, ast.With)

SOURCE_FILES = [
    "boolean_operations.py", "config.py", "sensors.py", "security.py", "lighting.py",
    "appliances.py", "energy_manager.py", "research.py", "main.py",
    "tests/test_boolean_operations.py", "tests/test_security.py", "tests/test_lighting.py",
    "tests/test_appliances.py", "tests/test_energy_manager.py",
    "tools/generate_line_guide.py",
]

BOOLEAN_FUNCTIONS = {
    "boolean_and(": "AND", "boolean_or(": "OR", "boolean_not(": "NOT",
    "boolean_xor(": "XOR", "boolean_nand(": "NAND", "boolean_nor(": "NOR",
}


def short(text: str, limit: int = 110) -> str:
    """Memendekkan teks panjang agar penjelasan tetap terbaca."""
    text = " ".join(text.split())
    return text if len(text) <= limit else text[: limit - 3] + "..."


def segment(source: str, node: Optional[ast.AST]) -> str:
    """Mengambil potongan kode sumber suatu node (string kosong bila tidak ada)."""
    if node is None:
        return ""
    return short(ast.get_source_segment(source, node) or "")


def first_sentence(doc: Optional[str]) -> str:
    """Kalimat/baris pertama sebuah docstring."""
    if not doc:
        return ""
    return doc.strip().splitlines()[0].strip()


def extra_notes(code: str) -> str:
    """Catatan tambahan: ekspresi Boolean, file handling, dan exception handling."""
    notes = []
    code = re.sub(r"(\"[^\"]*\"|'[^']*')", '""', code)   # abaikan isi string literal
    ops = [name for token, name in BOOLEAN_FUNCTIONS.items() if token in code]
    if ops:
        notes.append(f"Ekspresi Boolean: memakai operator {', '.join(ops)} dari boolean_operations.py.")
    if any(f" {word} " in f" {code} " for word in ("and", "or")) or " not " in f" {code} " \
            or code.strip().startswith("not "):
        notes.append("Ekspresi Boolean: memakai operator Python and/or/not (padanan AND/OR/NOT).")
    if any(token in code for token in ("read_text", "write_text", "open(", "csv.writer", "writerow",
                                       "json.loads", "json.dumps", "mkdir")):
        notes.append("File handling: membaca/menulis/menyiapkan file data (JSON atau CSV).")
    if code.strip().startswith(("raise ", "except")) or code.strip() == "try:":
        notes.append("Exception handling: menangani atau melaporkan kesalahan agar program tidak berhenti mendadak.")
    return " ".join(notes)


def describe_function(node: ast.FunctionDef, source: str) -> str:
    """Penjelasan baris `def`."""
    args = ast.unparse(node.args) or "(tanpa parameter)"
    returns = f" dan tipe kembalian `{ast.unparse(node.returns)}`" if node.returns else ""
    purpose = first_sentence(ast.get_docstring(node))
    text = f"Mendefinisikan fungsi `{node.name}` dengan parameter: {args}{returns}."
    return text + (f" Tujuan: {purpose}" if purpose else "")


def describe_statement(node: ast.stmt, source: str, text: str, in_class: bool, at_module: bool) -> str:
    """Penjelasan satu pernyataan berdasarkan jenis node AST-nya."""
    if isinstance(node, ast.Import):
        return "Mengimpor modul: " + ", ".join(a.name for a in node.names) + "."
    if isinstance(node, ast.ImportFrom):
        names = ", ".join(a.name for a in node.names)
        return f"Mengimpor {names} dari modul `{node.module}`."
    if isinstance(node, ast.FunctionDef):
        return describe_function(node, source)
    if isinstance(node, ast.ClassDef):
        bases = ", ".join(ast.unparse(b) for b in node.bases)
        decorators = ", ".join("@" + ast.unparse(d) for d in node.decorator_list)
        purpose = first_sentence(ast.get_docstring(node))
        extra = (f" turunan {bases}" if bases else "") + (f" dengan dekorator {decorators}" if decorators else "")
        return f"Mendefinisikan class `{node.name}`{extra}." + (f" Tujuan: {purpose}" if purpose else "")
    if isinstance(node, ast.Return):
        value = segment(source, node.value)
        return f"Mengembalikan hasil ekspresi `{value}` kepada pemanggil fungsi." if value else \
            "Keluar dari fungsi tanpa nilai (None)."
    if isinstance(node, ast.AnnAssign):
        target = ast.unparse(node.target)
        kind = "atribut class" if in_class else "variabel"
        default = f" dengan nilai awal `{segment(source, node.value)}`" if node.value else ""
        return f"Mendeklarasikan {kind} `{target}` bertipe `{ast.unparse(node.annotation)}`{default}."
    if isinstance(node, ast.Assign):
        targets = ", ".join(ast.unparse(t) for t in node.targets)
        kind = "konstanta/variabel modul" if at_module else "variabel"
        return f"Menetapkan {kind} `{targets}` dengan nilai `{segment(source, node.value)}`."
    if isinstance(node, ast.AugAssign):
        return f"Memperbarui `{ast.unparse(node.target)}` dengan operasi `{type(node.op).__name__}` terhadap `{segment(source, node.value)}`."
    if isinstance(node, ast.If):
        kind = "Percabangan alternatif (elif)" if text.lstrip().startswith("elif") else "Percabangan (if)"
        return f"{kind}: blok di bawahnya hanya dijalankan jika kondisi `{segment(source, node.test)}` bernilai True."
    if isinstance(node, ast.For):
        return (f"Perulangan for: variabel `{ast.unparse(node.target)}` mengambil tiap elemen dari "
                f"`{segment(source, node.iter)}`, dan blok di bawahnya diulang untuk tiap elemen.")
    if isinstance(node, ast.While):
        return f"Perulangan while: blok di bawahnya diulang selama `{segment(source, node.test)}` bernilai True."
    if isinstance(node, ast.Try):
        return "Awal blok try: kode di bawahnya dijalankan dan kesalahan yang mungkin muncul ditangkap oleh blok except."
    if isinstance(node, ast.With):
        items = ", ".join(ast.unparse(i) for i in node.items)
        return f"Blok with: membuka konteks `{items}` dan menutupnya otomatis setelah blok selesai."
    if isinstance(node, ast.Raise):
        return f"Melempar exception `{segment(source, node.exc)}` untuk melaporkan kondisi tidak valid."
    if isinstance(node, ast.Assert):
        return f"Memastikan kondisi `{segment(source, node.test)}` benar."
    if isinstance(node, ast.Pass):
        return "Pernyataan kosong; tidak melakukan apa pun."
    if isinstance(node, ast.Break):
        return "Menghentikan perulangan terdekat."
    if isinstance(node, ast.Continue):
        return "Melanjutkan ke iterasi berikutnya pada perulangan terdekat."
    if isinstance(node, ast.Expr):
        if isinstance(node.value, ast.Call):
            return f"Memanggil `{segment(source, node.value)}` (hasilnya tidak disimpan; yang penting efeknya)."
        return f"Ekspresi `{segment(source, node.value)}`."
    return f"Pernyataan `{short(text.strip())}`."


def analyse(source: str) -> Tuple[Dict[int, ast.stmt], Dict[int, str], Dict[int, ast.AST], Set[int], List[ast.AST]]:
    """Membangun peta baris -> node, docstring, dan daftar blok fungsi/class dari AST."""
    tree = ast.parse(source)
    starts: Dict[int, ast.stmt] = {}
    docstring_lines: Dict[int, str] = {}
    simple_spans: List[ast.stmt] = []
    blocks: List[ast.AST] = []
    parents: Dict[ast.AST, ast.AST] = {}
    for parent in ast.walk(tree):
        for child in ast.iter_child_nodes(parent):
            parents[child] = parent
    for node in ast.walk(tree):
        if not isinstance(node, ast.stmt):
            continue
        parent = parents.get(node)
        is_doc = (isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant)
                  and isinstance(node.value.value, str)
                  and isinstance(parent, (ast.Module, ast.FunctionDef, ast.ClassDef))
                  and parent.body and parent.body[0] is node)
        if is_doc:
            owner = "modul" if isinstance(parent, ast.Module) else f"`{parent.name}`"
            for line in range(node.lineno, node.end_lineno + 1):
                docstring_lines[line] = owner
            continue
        starts.setdefault(node.lineno, node)
        if not isinstance(node, COMPOUND):
            simple_spans.append(node)
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            blocks.append(node)
    return starts, docstring_lines, parents, set(), blocks + simple_spans


def explain_file(relative: str) -> List[str]:
    """Membuat seluruh entri penjelasan untuk satu file Python."""
    path = ROOT / relative
    source = path.read_text(encoding="utf-8")
    lines = source.splitlines()
    out = [f"File: {relative}", ""]
    if not lines:
        out += ["(File kosong: sengaja kosong agar folder `tests` dikenali sebagai package.)", ""]
        return out
    tree = ast.parse(source)
    starts, docstring_lines, parents, _, extra = analyse(source)
    simple = [n for n in extra if not isinstance(n, (ast.FunctionDef, ast.ClassDef))]
    block_ends = {n.end_lineno: n for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.ClassDef))}
    for number, raw in enumerate(lines, 1):
        text = raw.rstrip()
        stripped = text.strip()
        if not stripped:
            note = "Baris kosong: pemisah visual antarbagian agar kode mudah dibaca; tidak menjalankan instruksi."
        elif number in docstring_lines:
            note = (f"Bagian docstring {docstring_lines[number]}: dokumentasi (bukan logika program) "
                    "yang menjelaskan tujuan, parameter, nilai kembalian, atau rumus.")
        elif stripped.startswith("#"):
            note = "Komentar: penjelasan untuk pembaca, tidak dieksekusi Python."
        elif number in starts:
            node = starts[number]
            parent = parents.get(node)
            note = describe_statement(node, source, text, isinstance(parent, ast.ClassDef),
                                      isinstance(parent, ast.Module))
            extra_note = "" if isinstance(node, (ast.FunctionDef, ast.ClassDef)) else extra_notes(text)
            if extra_note:
                note += " " + extra_note
        elif stripped.startswith("@"):
            note = f"Dekorator `{stripped}`: memodifikasi class/fungsi di bawahnya (mis. membuat dataclass)."
        elif stripped.startswith("else:"):
            note = "Cabang else: dijalankan bila semua kondisi if/elif/for di atasnya tidak terpenuhi."
        elif stripped.startswith("except"):
            note = (f"Penangkap kesalahan `{short(stripped)}`: dijalankan bila blok try melempar exception "
                    "yang sesuai, sehingga program tidak berhenti mendadak.")
        elif stripped.startswith("finally"):
            note = "Blok finally: selalu dijalankan setelah try/except."
        else:
            owner = next((n for n in simple if n.lineno < number <= n.end_lineno), None)
            if owner is not None:
                note = (f"Lanjutan dari pernyataan yang dimulai pada baris {owner.lineno} "
                        f"(`{short(lines[owner.lineno - 1].strip(), 60)}`): bagian ini adalah elemen/argumen/"
                        "ekspresi yang memperpanjang pernyataan tersebut.")
                extra_note = extra_notes(text)
                if extra_note:
                    note += " " + extra_note
            else:
                header = next((n for n in ast.walk(tree) if isinstance(n, COMPOUND)
                               and n.lineno < number < n.body[0].lineno), None)
                if header is not None:
                    note = (f"Lanjutan header yang dimulai pada baris {header.lineno}: "
                            "bagian parameter/kondisi yang ditulis lebih dari satu baris.")
                else:
                    note = "Lanjutan dari pernyataan di atasnya."
        out += [f"Line {number}:", f"Kode: {text}", f"Penjelasan: {note}", ""]
        if number in block_ends:
            block = block_ends[number]
            kind = "class" if isinstance(block, ast.ClassDef) else "fungsi"
            purpose = first_sentence(ast.get_docstring(block))
            out += [(f"Hubungan antarbaris ({kind} `{block.name}`, baris {block.lineno}-{block.end_lineno}): "
                     f"baris pertama menetapkan nama dan parameter, baris-baris badan dijalankan berurutan "
                     f"dari atas ke bawah, lalu return/raise menentukan keluaran."
                     + (f" Tujuan blok: {purpose}" if purpose else "")), ""]
    return out


def main() -> None:
    """Menyusun seluruh panduan dan menulisnya ke docs/LINE_BY_LINE_GUIDE.md."""
    parts = [
        "# Line-by-Line Guide", "",
        "Panduan ini dibuat OTOMATIS oleh `tools/generate_line_guide.py` dari source code final, sehingga",
        "nomor baris selalu cocok. **Jalankan ulang generator setiap kali source code berubah.**", "",
        "Cara membaca: setiap entri berisi nomor baris, kode asli, dan penjelasan. Penjelasan disusun dari",
        "struktur program (AST): jenis pernyataan, nama variabel/fungsi, parameter, ekspresi, serta tujuan",
        "fungsi yang diambil dari docstring-nya. Setelah setiap fungsi/class ada paragraf *Hubungan antarbaris*.", "",
        "Perintah: `python tools/generate_line_guide.py`", "",
    ]
    for relative in SOURCE_FILES:
        parts += [f"## {relative}", "", FENCE + "text"]
        parts += explain_file(relative)
        parts += [FENCE, ""]
    OUTPUT.write_text("\n".join(parts), encoding="utf-8")
    total = sum(len((ROOT / f).read_text(encoding="utf-8").splitlines()) for f in SOURCE_FILES)
    print(f"Ditulis: {OUTPUT} ({total} baris kode dijelaskan)")


if __name__ == "__main__":
    main()
