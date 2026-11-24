"""Unit test klasifikasi perangkat, pencarian, waktu simulasi, dan validasi konfigurasi."""

import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from appliances import ApplianceManager
from config import (CATEGORY_CONDITIONAL, CATEGORY_ESSENTIAL, CATEGORY_NON_ESSENTIAL, AppConfig,
                    DeviceSpec, UsageLimits, default_config, load_config, save_config,
                    validate_config, validate_device_spec)


class TestAppliances(unittest.TestCase):
    """Menguji ApplianceManager dan config."""

    def setUp(self) -> None:
        self.manager = ApplianceManager(default_config().devices)

    def test_default_classification(self) -> None:
        cats = {d.spec.name: d.spec.category for d in self.manager.devices}
        self.assertEqual(cats["Refrigerator"], CATEGORY_ESSENTIAL)
        self.assertEqual(cats["Main Lighting"], CATEGORY_CONDITIONAL)
        self.assertEqual(cats["Fan"], CATEGORY_CONDITIONAL)
        self.assertEqual(cats["Television"], CATEGORY_NON_ESSENTIAL)
        self.assertEqual(cats["Decorative Lighting"], CATEGORY_NON_ESSENTIAL)

    def test_default_power_values(self) -> None:
        power = {d.spec.name: d.spec.power_w for d in self.manager.devices}
        self.assertEqual(power, {"Refrigerator": 150.0, "Main Lighting": 12.0, "Fan": 45.0,
                                 "Television": 80.0, "Decorative Lighting": 20.0})

    def test_find_by_name_and_number(self) -> None:
        self.assertEqual(self.manager.find("television").spec.name, "Television")
        self.assertEqual(self.manager.find("1").spec.name, "Refrigerator")
        with self.assertRaises(ValueError):
            self.manager.find("99")
        with self.assertRaises(ValueError):
            self.manager.find("Oven")

    def test_turn_on_off_and_counters(self) -> None:
        self.assertTrue(self.manager.turn_on("Fan"))
        self.assertFalse(self.manager.turn_on("Fan"))
        self.assertEqual(self.manager.find("Fan").activations_today, 1)
        self.manager.advance_minutes(30)
        fan = self.manager.find("Fan")
        self.assertEqual((fan.minutes_today, fan.idle_minutes), (30, 30))
        self.manager.touch("Fan")
        self.assertEqual(fan.idle_minutes, 0)
        self.assertTrue(self.manager.turn_off("Fan"))
        self.assertFalse(self.manager.turn_off("Fan"))

    def test_off_device_does_not_accumulate_time(self) -> None:
        self.manager.advance_minutes(100)
        self.assertEqual(self.manager.find("Television").minutes_today, 0)

    def test_invalid_minutes(self) -> None:
        for bad in (-1, 1.5, True):
            with self.assertRaises(ValueError):
                self.manager.advance_minutes(bad)

    def test_duplicate_names_rejected(self) -> None:
        spec = DeviceSpec("X", CATEGORY_ESSENTIAL, 1.0)
        with self.assertRaises(ValueError):
            ApplianceManager([spec, spec])

    def test_reset_day(self) -> None:
        self.manager.turn_on("Fan")
        self.manager.advance_minutes(10)
        self.manager.reset_day()
        fan = self.manager.find("Fan")
        self.assertEqual((fan.minutes_today, fan.activations_today, fan.idle_minutes), (0, 0, 0))

    def test_config_validation(self) -> None:
        with self.assertRaises(ValueError):
            validate_device_spec(DeviceSpec("A", "Unknown", 1.0))
        with self.assertRaises(ValueError):
            validate_device_spec(DeviceSpec("A", CATEGORY_ESSENTIAL, -5.0))
        with self.assertRaises(ValueError):
            validate_device_spec(DeviceSpec("A", CATEGORY_NON_ESSENTIAL, 5.0, limits=UsageLimits(0, None, None)))
        with self.assertRaises(ValueError):
            validate_config(AppConfig([DeviceSpec("A", CATEGORY_ESSENTIAL, 1.0),
                                       DeviceSpec("a", CATEGORY_ESSENTIAL, 1.0)]))

    def test_config_roundtrip_and_bad_json(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "config.json"
            self.assertEqual(len(load_config(path).devices), 5)   # file tidak ada -> default
            save_config(default_config(), path)
            self.assertEqual(load_config(path).devices, default_config().devices)
            path.write_text("{bukan json", encoding="utf-8")
            with self.assertRaises(ValueError):
                load_config(path)
            path.write_text("{}", encoding="utf-8")
            with self.assertRaises(ValueError):
                load_config(path)


if __name__ == "__main__":
    unittest.main()
