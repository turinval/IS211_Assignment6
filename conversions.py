"""conversions.py

Holds standalone temperature conversion functions.
"""


def convertCelsiusToKelvin(celsius: float) -> float:
    """Converts a Celsius temperature to Kelvin."""
    return float(celsius + 273.15)


def convertCelsiusToFahrenheit(celsius: float) -> float:
    """Converts a Celsius temperature to Fahrenheit."""
    return float((celsius * 9.0 / 5.0) + 32.0)


def convertFahrenheitToCelsius(fahrenheit: float) -> float:
    """Converts a Fahrenheit temperature to Celsius."""
    return float((fahrenheit - 32.0) * 5.0 / 9.0)


def convertFahrenheitToKelvin(fahrenheit: float) -> float:
    """Converts a Fahrenheit temperature to Kelvin."""
    return float(((fahrenheit - 32.0) * 5.0 / 9.0) + 273.15)


def convertKelvinToCelsius(kelvin: float) -> float:
    """Converts a Kelvin temperature to Celsius."""
    return float(kelvin - 273.15)


def convertKelvinToFahrenheit(kelvin: float) -> float:
    """Converts a Kelvin temperature to Fahrenheit."""
    return float(((kelvin - 273.15) * 9.0 / 5.0) + 32.0)
