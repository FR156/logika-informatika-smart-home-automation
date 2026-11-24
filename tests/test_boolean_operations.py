"""Unit test enam operator Boolean, tabel kebenaran, dan validasi masukan."""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from boolean_operations import (boolean_and, boolean_nand, boolean_nor, boolean_not, boolean_or,
                                boolean_xor, evaluate_operator, format_truth_table,
                                operator_arity, reference_result, truth_table)

# Tabel kebenaran yang ditulis manual (urutan: 00, 01, 10, 11).
EXPECTED = {
    "AND": [False, False, False, True],
    "OR": [False, True, True, True],
    "XOR": [False, True, True, False],
    "NAND": [True, True, True, False],
    "NOR": [True, False, False, False],
}


class TestBooleanOperations(unittest.TestCase):
    """Menguji seluruh kombinasi masukan setiap operator."""

    FUNCS = {"AND": boolean_and, "OR": boolean_or, "XOR": boolean_xor,
             "NAND": boolean_nand, "NOR": boolean_nor}

    def test_binary_operators_match_manual_tables(self) -> None:
        pairs = [(False, False), (False, True), (True, False), (True, True)]
        for name, func in self.FUNCS.items():
            for pair, expected in zip(pairs, EXPECTED[name]):
                with self.subTest(op=name, inputs=pair):
                    self.assertIs(func(*pair), expected)

    def test_not(self) -> None:
        self.assertIs(boolean_not(True), False)
        self.assertIs(boolean_not(False), True)

    def test_results_are_real_bool(self) -> None:
        self.assertIs(boolean_and(True, True), True)
        self.assertIsInstance(boolean_or(False, False), bool)

    def test_evaluate_operator_by_name(self) -> None:
        self.assertIs(evaluate_operator("xor", True, False), True)
        self.assertIs(evaluate_operator("NOT", True), False)

    def test_reference_matches_functions(self) -> None:
        for name in list(EXPECTED) + ["NOT"]:
            for inputs, output in truth_table(name):
                self.assertEqual(output, reference_result(name, inputs))

    def test_invalid_operator_and_arity(self) -> None:
        with self.assertRaises(ValueError):
            operator_arity("IMPLIES")
        with self.assertRaises(ValueError):
            evaluate_operator("AND", True)
        with self.assertRaises(ValueError):
            evaluate_operator("NOT", True, False)

    def test_truth_table_format(self) -> None:
        text = format_truth_table("NAND")
        self.assertIn("A B | NAND", text)
        self.assertEqual(len(truth_table("NOT")), 2)
        self.assertEqual(len(truth_table("NOR")), 4)


if __name__ == "__main__":
    unittest.main()
