"""Unit test tiga mode pencahayaan dan prioritas manual override."""

import os
import sys
import unittest
from itertools import product

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lighting import LightingMode, evaluate_lighting, parse_lighting_mode


class TestLighting(unittest.TestCase):
    """Menguji AUTO (occupied AND dark), ON, dan OFF."""

    def test_auto_follows_boolean(self) -> None:
        for occupied, dark in product([False, True], repeat=2):
            result = evaluate_lighting(LightingMode.AUTO, occupied, dark)
            self.assertIs(result.lamp_on, occupied and dark)

    def test_on_always_on(self) -> None:
        for occupied, dark in product([False, True], repeat=2):
            self.assertTrue(evaluate_lighting(LightingMode.ON, occupied, dark).lamp_on)

    def test_off_always_off(self) -> None:
        for occupied, dark in product([False, True], repeat=2):
            self.assertFalse(evaluate_lighting(LightingMode.OFF, occupied, dark).lamp_on)

    def test_override_has_priority_over_auto_decision(self) -> None:
        result = evaluate_lighting(LightingMode.OFF, True, True)
        self.assertTrue(result.auto_decision)
        self.assertFalse(result.lamp_on)

    def test_reason_texts(self) -> None:
        self.assertIn("tidak ditempati", evaluate_lighting(LightingMode.AUTO, False, True).reason)
        self.assertIn("tidak gelap", evaluate_lighting(LightingMode.AUTO, True, False).reason)

    def test_parse_mode(self) -> None:
        self.assertIs(parse_lighting_mode("auto"), LightingMode.AUTO)
        self.assertIs(parse_lighting_mode("2"), LightingMode.ON)
        self.assertIs(parse_lighting_mode("OFF"), LightingMode.OFF)
        self.assertIsNone(parse_lighting_mode("dim"))


if __name__ == "__main__":
    unittest.main()
