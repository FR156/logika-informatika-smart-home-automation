"""Unit test logika alarm (8 kombinasi) dan diagnostik sensor."""

import os
import sys
import unittest
from itertools import product

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from security import evaluate_security
from sensors import (SensorState, diagnostics_incomplete, door_mismatch, no_activity, parse_bool)


class TestSecurity(unittest.TestCase):
    """Menguji rumus alarm_active = security_mode AND (door_open OR motion_detected)."""

    def test_all_eight_combinations(self) -> None:
        for mode, door, motion in product([False, True], repeat=3):
            expected = mode and (door or motion)
            with self.subTest(mode=mode, door=door, motion=motion):
                self.assertIs(evaluate_security(mode, door, motion).alarm_active, expected)

    def test_mode_off_never_alarms(self) -> None:
        result = evaluate_security(False, True, True)
        self.assertFalse(result.alarm_active)
        self.assertIn("mode keamanan OFF", result.reason)

    def test_reasons(self) -> None:
        self.assertIn("pintu terbuka", evaluate_security(True, True, False).reason)
        self.assertIn("gerakan terdeteksi", evaluate_security(True, False, True).reason)
        self.assertIn("tidak ada gerakan", evaluate_security(True, False, False).reason)

    def test_xor_door_mismatch_and_nor(self) -> None:
        self.assertTrue(door_mismatch(SensorState(door_open=True, door_open_redundant=False)))
        self.assertFalse(door_mismatch(SensorState(door_open=True, door_open_redundant=True)))
        self.assertTrue(no_activity(SensorState()))
        self.assertFalse(no_activity(SensorState(motion_detected=True)))

    def test_nand_diagnostics(self) -> None:
        self.assertFalse(diagnostics_incomplete(SensorState()))
        self.assertTrue(diagnostics_incomplete(SensorState(motion_sensor_online=False)))
        self.assertTrue(diagnostics_incomplete(SensorState(door_open=True)))

    def test_parse_bool_validation(self) -> None:
        self.assertIs(parse_bool(" YES "), True)
        self.assertIs(parse_bool("closed"), False)
        self.assertIsNone(parse_bool("mungkin"))
        self.assertIsNone(parse_bool(""))


if __name__ == "__main__":
    unittest.main()
