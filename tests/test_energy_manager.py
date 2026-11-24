"""Unit test kebijakan energi, batas penggunaan, kalkulasi kWh, dan simulasi riset."""

import os
import sys
import tempfile
import unittest
from itertools import product
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import research
from appliances import ApplianceManager
from config import default_config
from energy_manager import (Context, EnergyPolicy, compute_savings, device_energy_kwh, energy_kwh,
                            enforce_policy, evaluate_device, nonessential_allowed, percent_change,
                            request_turn_on, total_energy_kwh, usage_flags)

HOME_OK = Context(occupied=True, energy_saving_mode=False, lamp_on=True)


def make() -> ApplianceManager:
    """Manager baru dari konfigurasi default (deterministik)."""
    return ApplianceManager(default_config().devices)


class TestStrategy1(unittest.TestCase):
    """Strategy 1: occupied AND NOT energy_saving_mode."""

    def test_formula_all_combinations(self) -> None:
        policy = EnergyPolicy()
        for occupied, saving in product([False, True], repeat=2):
            ctx = Context(occupied, saving, True)
            self.assertIs(nonessential_allowed(ctx, policy), occupied and not saving)

    def test_disabled_strategy_always_allows(self) -> None:
        self.assertTrue(nonessential_allowed(Context(False, True, False), EnergyPolicy(shutdown_enabled=False)))

    def test_nonessential_shutdown_when_unoccupied_or_saving(self) -> None:
        for ctx in (Context(False, False, True), Context(True, True, True)):
            manager = make()
            policy = EnergyPolicy()
            for name in ("Television", "Decorative Lighting"):
                manager.turn_on(name)
            turned_off = enforce_policy(manager, ctx, policy)
            self.assertEqual(len(turned_off), 2)
            self.assertFalse(manager.find("Television").is_on)

    def test_essential_never_shut_down(self) -> None:
        manager = make()
        manager.turn_on("Refrigerator")
        enforce_policy(manager, Context(False, True, False), EnergyPolicy())
        self.assertTrue(manager.find("Refrigerator").is_on)
        decision = evaluate_device(manager.find("Refrigerator"), Context(False, True, False), EnergyPolicy(), False)
        self.assertTrue(decision.allowed)

    def test_essential_exempt_from_usage_limits(self) -> None:
        manager = make()
        manager.turn_on("Refrigerator")
        manager.advance_minutes(5000)
        self.assertTrue(evaluate_device(manager.find("Refrigerator"), HOME_OK, EnergyPolicy(), False).allowed)

    def test_conditional_rules(self) -> None:
        manager = make()
        fan = manager.find("Fan")
        self.assertTrue(evaluate_device(fan, Context(True, False, False), EnergyPolicy(), True).allowed)
        self.assertFalse(evaluate_device(fan, Context(False, False, True), EnergyPolicy(), True).allowed)
        lamp = manager.find("Main Lighting")
        self.assertTrue(evaluate_device(lamp, Context(True, False, True), EnergyPolicy(), True).allowed)
        self.assertFalse(evaluate_device(lamp, Context(True, False, False), EnergyPolicy(), True).allowed)

    def test_request_turn_on_respects_policy(self) -> None:
        manager = make()
        denied = request_turn_on(manager, "Television", Context(True, True, True), EnergyPolicy())
        self.assertFalse(denied.allowed)
        self.assertFalse(manager.find("Television").is_on)
        allowed = request_turn_on(manager, "Television", HOME_OK, EnergyPolicy())
        self.assertTrue(allowed.allowed)
        self.assertTrue(manager.find("Television").is_on)


class TestStrategy2(unittest.TestCase):
    """Strategy 2: durasi, frekuensi, dan inactivity timeout (waktu simulasi, tanpa jam nyata)."""

    def test_duration_limit_shuts_down_tv(self) -> None:
        manager, policy = make(), EnergyPolicy()
        request_turn_on(manager, "Television", HOME_OK, policy)
        manager.advance_minutes(239)
        manager.touch("Television")
        self.assertTrue(evaluate_device(manager.find("Television"), HOME_OK, policy, False).allowed)
        manager.advance_minutes(1)
        manager.touch("Television")
        self.assertFalse(evaluate_device(manager.find("Television"), HOME_OK, policy, False).allowed)
        enforce_policy(manager, HOME_OK, policy)
        self.assertFalse(manager.find("Television").is_on)

    def test_duration_limit_blocks_reactivation(self) -> None:
        manager, policy = make(), EnergyPolicy()
        request_turn_on(manager, "Television", HOME_OK, policy)
        manager.advance_minutes(240)
        manager.turn_off("Television")
        decision = request_turn_on(manager, "Television", HOME_OK, policy)
        self.assertFalse(decision.allowed)
        self.assertIn("durasi", decision.reason)
        manager.reset_day()
        self.assertTrue(request_turn_on(manager, "Television", HOME_OK, policy).allowed)

    def test_frequency_limit_blocks_activation_not_running_device(self) -> None:
        manager, policy = make(), EnergyPolicy()
        for _ in range(6):
            self.assertTrue(request_turn_on(manager, "Television", HOME_OK, policy).allowed)
            manager.turn_off("Television")
        denied = request_turn_on(manager, "Television", HOME_OK, policy)
        self.assertFalse(denied.allowed)
        self.assertIn("frekuensi", denied.reason)
        # perangkat yang sedang ON pada aktivasi terakhir yang sah tidak dimatikan karena frekuensi
        manager.reset_day()
        for _ in range(5):
            request_turn_on(manager, "Television", HOME_OK, policy)
            manager.turn_off("Television")
        self.assertTrue(request_turn_on(manager, "Television", HOME_OK, policy).allowed)
        self.assertEqual(manager.find("Television").activations_today, 6)
        self.assertTrue(evaluate_device(manager.find("Television"), HOME_OK, policy, False).allowed)

    def test_inactivity_timeout(self) -> None:
        manager, policy = make(), EnergyPolicy()
        request_turn_on(manager, "Decorative Lighting", HOME_OK, policy)
        manager.advance_minutes(59)
        self.assertTrue(evaluate_device(manager.find("Decorative Lighting"), HOME_OK, policy, False).allowed)
        manager.advance_minutes(1)
        decision = evaluate_device(manager.find("Decorative Lighting"), HOME_OK, policy, False)
        self.assertFalse(decision.allowed)
        self.assertIn("inactivity", decision.reason)

    def test_touch_resets_inactivity(self) -> None:
        manager, policy = make(), EnergyPolicy()
        request_turn_on(manager, "Decorative Lighting", HOME_OK, policy)
        manager.advance_minutes(59)
        manager.touch("Decorative Lighting")
        manager.advance_minutes(59)
        self.assertTrue(evaluate_device(manager.find("Decorative Lighting"), HOME_OK, policy, False).allowed)

    def test_usage_flags_are_booleans(self) -> None:
        manager = make()
        flags = usage_flags(manager.find("Television"), activation=True)
        self.assertTrue(all(isinstance(f, bool) for f in flags))
        self.assertEqual(flags, (False, False, False))

    def test_limits_can_be_disabled(self) -> None:
        manager = make()
        manager.turn_on("Television")
        manager.advance_minutes(1000)
        self.assertTrue(evaluate_device(manager.find("Television"), HOME_OK,
                                        EnergyPolicy(limits_enabled=False), False).allowed)


class TestEnergyCalculation(unittest.TestCase):
    """Rumus kWh = W x jam / 1000."""

    def test_formula(self) -> None:
        self.assertAlmostEqual(energy_kwh(150, 24), 3.6)
        self.assertAlmostEqual(energy_kwh(80, 1.5), 0.12)
        self.assertEqual(energy_kwh(100, 0), 0.0)

    def test_negative_rejected(self) -> None:
        with self.assertRaises(ValueError):
            energy_kwh(-1, 1)
        with self.assertRaises(ValueError):
            energy_kwh(1, -1)

    def test_off_device_zero_and_essential_counted(self) -> None:
        manager = make()
        manager.turn_on("Refrigerator")
        manager.advance_minutes(60)
        self.assertEqual(device_energy_kwh(manager.find("Television")), 0.0)
        self.assertAlmostEqual(total_energy_kwh(manager), 0.15)

    def test_savings(self) -> None:
        saving, percent = compute_savings(5.0, 4.0)
        self.assertAlmostEqual(saving, 1.0)
        self.assertAlmostEqual(percent, 20.0)
        self.assertAlmostEqual(percent_change(5.0, 4.0), -20.0)
        self.assertEqual(compute_savings(0.0, 0.0), (0.0, 0.0))
        with self.assertRaises(ValueError):
            compute_savings(4.0, 5.0)


class TestResearch(unittest.TestCase):
    """Eksperimen harus deterministik dan konsisten."""

    def test_experiment_1_accuracy_100(self) -> None:
        results = research.run_experiment_1()
        self.assertEqual(sum(r[1] for r in results), 22)
        self.assertTrue(all(r[3] == 100.0 for r in results))

    def test_experiment_2_eight_cases_all_pass(self) -> None:
        rows = research.run_experiment_2()
        self.assertEqual(len(rows), 8)
        self.assertTrue(all(r[3] == r[4] for r in rows))

    def test_experiment_3_ordering_and_nonnegative_savings(self) -> None:
        a, b, c = research.run_experiment_3()
        self.assertGreaterEqual(a.total_kwh, b.total_kwh)
        self.assertGreaterEqual(b.total_kwh, c.total_kwh)
        self.assertGreater(a.total_kwh, c.total_kwh)
        for result in (b, c):
            saving, percent = compute_savings(a.total_kwh, result.total_kwh)
            self.assertGreaterEqual(saving, 0)
            self.assertGreaterEqual(percent, 0)

    def test_experiment_3_essential_always_full_day(self) -> None:
        for result in research.run_experiment_3():
            fridge = [row for row in result.rows if row[0] == "Refrigerator"][0]
            self.assertEqual(fridge[1], 1440)

    def test_experiment_3_is_deterministic(self) -> None:
        first = [r.total_kwh for r in research.run_experiment_3()]
        second = [r.total_kwh for r in research.run_experiment_3()]
        self.assertEqual(first, second)

    def test_csv_written(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "out.csv"
            research.run_all(csv_path=path)
            lines = path.read_text(encoding="utf-8").splitlines()
            self.assertEqual(lines[0], "experiment,case,item,metric,value,unit,data_type")
            self.assertGreater(len(lines), 50)


if __name__ == "__main__":
    unittest.main()
