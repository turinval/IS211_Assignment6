"""conversions_refactored.py

Refactored conversion system handling temperature and distance conversions.
"""


class ConversionNotPossible(Exception):
    """Raised when attempting to convert between incompatible unit types."""

    pass


def convert(fromUnit: str, toUnit: str, value: float) -> float:
    """Converts a value from one unit to another.

    Supported Temperature: 'Celsius', 'Fahrenheit', 'Kelvin' Supported Distance:
    'Meters', 'Yards', 'Miles'
    """
    from_u = fromUnit.strip().title()
    to_u = toUnit.strip().title()
    val = float(value)

    # Rule 3: Converting from one unit to itself returns the same value
    if from_u == to_u:
        # Check that the unit itself is recognized
        known_units = {
            "Celsius",
            "Fahrenheit",
            "Kelvin",
            "Meters",
            "Yards",
            "Miles",
        }
        if from_u in known_units:
            return round(val, 2)
        raise ConversionNotPossible(f"Unknown unit: {fromUnit}")

    temp_units = {"Celsius", "Fahrenheit", "Kelvin"}
    dist_units = {"Meters", "Yards", "Miles"}

    # Incompatible unit check
    if (from_u in temp_units and to_u not in temp_units) or (
        from_u in dist_units and to_u not in dist_units
    ):
        raise ConversionNotPossible(
            f"Cannot convert between {fromUnit} and {toUnit}."
        )

    # 1. Temperature conversions (canonical base: Celsius)
    if from_u in temp_units and to_u in temp_units:
        # Convert from source to Celsius base
        if from_u == "Celsius":
            celsius_val = val
        elif from_u == "Fahrenheit":
            celsius_val = (val - 32.0) * 5.0 / 9.0
        elif from_u == "Kelvin":
            celsius_val = val - 273.15

        # Convert Celsius base to target unit
        if to_u == "Celsius":
            return round(celsius_val, 2)
        elif to_u == "Fahrenheit":
            return round((celsius_val * 9.0 / 5.0) + 32.0, 2)
        elif to_u == "Kelvin":
            return round(celsius_val + 273.15, 2)

    # 2. Distance conversions (canonical base: Meters)
    # Conversion rates: 1 Yard = 0.9144 Meters, 1 Mile = 1609.344 Meters
    if from_u in dist_units and to_u in dist_units:
        # Convert from source to Meters base
        if from_u == "Meters":
            meters_val = val
        elif from_u == "Yards":
            meters_val = val * 0.9144
        elif from_u == "Miles":
            meters_val = val * 1609.344

        # Convert Meters base to target unit
        if to_u == "Meters":
            return round(meters_val, 2)
        elif to_u == "Yards":
            return round(meters_val / 0.9144, 2)
        elif to_u == "Miles":
            return round(meters_val / 1609.344, 2)

    raise ConversionNotPossible(
        f"Conversion from {fromUnit} to {toUnit} is not supported."
    )
