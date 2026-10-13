"""tests.py

Comprehensive test suite for conversions.py and conversions_refactored.py.
"""

import unittest
import conversions
import conversions_refactored


class TestConversions(unittest.TestCase):
    """Tests for individual functions in conversions.py (Parts I-III)."""

    def test_convertCelsiusToKelvin(self):
        cases = [
            (0.0, 273.15),
            (100.0, 373.15),
            (-273.15, 0.0),
            (300.0, 573.15),
            (25.0, 298.15),
        ]
        for c, expected in cases:
            result = conversions.convertCelsiusToKelvin(c)
            print(f"[TEST] convertCelsiusToKelvin: {c}°C -> {result:.2f} K (Expected: {expected:.2f} K)")
            self.assertAlmostEqual(result, expected, places=2)

    def test_convertCelsiusToFahrenheit(self):
        cases = [
            (0.0, 32.0),
            (100.0, 212.0),
            (-40.0, -40.0),
            (300.0, 572.0),
            (37.0, 98.6),
        ]
        for c, expected in cases:
            result = conversions.convertCelsiusToFahrenheit(c)
            print(f"[TEST] convertCelsiusToFahrenheit: {c}°C -> {result:.2f}°F (Expected: {expected:.2f}°F)")
            self.assertAlmostEqual(result, expected, places=2)

    def test_convertFahrenheitToCelsius(self):
        cases = [
            (32.0, 0.0),
            (212.0, 100.0),
            (-40.0, -40.0),
            (572.0, 300.0),
            (98.6, 37.0),
        ]
        for f, expected in cases:
            result = conversions.convertFahrenheitToCelsius(f)
            print(f"[TEST] convertFahrenheitToCelsius: {f}°F -> {result:.2f}°C (Expected: {expected:.2f}°C)")
            self.assertAlmostEqual(result, expected, places=2)

    def test_convertFahrenheitToKelvin(self):
        cases = [
            (32.0, 273.15),
            (212.0, 373.15),
            (-459.67, 0.0),
            (572.0, 573.15),
            (68.0, 293.15),
        ]
        for f, expected in cases:
            result = conversions.convertFahrenheitToKelvin(f)
            print(f"[TEST] convertFahrenheitToKelvin: {f}°F -> {result:.2f} K (Expected: {expected:.2f} K)")
            self.assertAlmostEqual(result, expected, places=2)

    def test_convertKelvinToCelsius(self):
        cases = [
            (273.15, 0.0),
            (373.15, 100.0),
            (0.0, -273.15),
            (573.15, 300.0),
            (298.15, 25.0),
        ]
        for k, expected in cases:
            result = conversions.convertKelvinToCelsius(k)
            print(f"[TEST] convertKelvinToCelsius: {k} K -> {result:.2f}°C (Expected: {expected:.2f}°C)")
            self.assertAlmostEqual(result, expected, places=2)

    def test_convertKelvinToFahrenheit(self):
        cases = [
            (273.15, 32.0),
            (373.15, 212.0),
            (0.0, -459.67),
            (573.15, 572.0),
            (293.15, 68.0),
        ]
        for k, expected in cases:
            result = conversions.convertKelvinToFahrenheit(k)
            print(f"[TEST] convertKelvinToFahrenheit: {k} K -> {result:.2f}°F (Expected: {expected:.2f}°F)")
            self.assertAlmostEqual(result, expected, places=2)


class TestConversionsRefactored(unittest.TestCase):
    """Tests for conversions_refactored.py (Part IV)."""

    def test_temperature_conversions(self):
        cases = [
            ("Celsius", "Fahrenheit", 300.0, 572.0),
            ("Celsius", "Kelvin", 300.0, 573.15),
            ("Fahrenheit", "Celsius", 212.0, 100.0),
            ("Fahrenheit", "Kelvin", 32.0, 273.15),
            ("Kelvin", "Celsius", 373.15, 100.0),
            ("Kelvin", "Fahrenheit", 273.15, 32.0),
        ]
        for from_u, to_u, val, expected in cases:
            res = conversions_refactored.convert(from_u, to_u, val)
            print(f"[REFACTORED TEMP] {val} {from_u} -> {res} {to_u} (Expected: {expected})")
            self.assertAlmostEqual(res, expected, places=2)

    def test_distance_conversions(self):
        cases = [
            ("Miles", "Yards", 1.0, 1760.0),
            ("Miles", "Meters", 1.0, 1609.34),
            ("Yards", "Miles", 1760.0, 1.0),
            ("Yards", "Meters", 100.0, 91.44),
            ("Meters", "Miles", 1609.344, 1.0),
            ("Meters", "Yards", 10.0, 10.94),
        ]
        for from_u, to_u, val, expected in cases:
            res = conversions_refactored.convert(from_u, to_u, val)
            print(f"[REFACTORED DIST] {val} {from_u} -> {res} {to_u} (Expected: {expected})")
            self.assertAlmostEqual(res, expected, places=2)

    def test_same_unit_conversion(self):
        units = ["Celsius", "Fahrenheit", "Kelvin", "Miles", "Yards", "Meters"]
        for unit in units:
            val = 42.0
            res = conversions_refactored.convert(unit, unit, val)
            print(f"[REFACTORED SAME] {val} {unit} -> {res} {unit}")
            self.assertEqual(res, val)

    def test_incompatible_units_raise_exception(self):
        incompatible_pairs = [
            ("Celsius", "Meters", 100.0),
            ("Miles", "Fahrenheit", 5.0),
            ("Kelvin", "Yards", 300.0),
            ("Yards", "Celsius", 50.0),
        ]
        for from_u, to_u, val in incompatible_pairs:
            print(f"[REFACTORED INCOMPATIBLE] Testing {from_u} -> {to_u} raises ConversionNotPossible")
            with self.assertRaises(conversions_refactored.ConversionNotPossible):
                conversions_refactored.convert(from_u, to_u, val)


if __name__ == "__main__":
    unittest.main()
