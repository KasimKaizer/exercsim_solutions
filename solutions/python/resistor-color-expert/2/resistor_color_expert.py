"""Function for implementing the Resistor Color Expert exercise on Exercism.org"""

#: Mapping resistor color to their digit values.
COLORS: dict[str, int] = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}

#: Magnitude prefixes.
MAGNITUDE: list[str] = ["", "kilo", "mega", "giga"]

#: Mapping resistor color to their tolerance percentages.
TOLERANCE: dict[str, float] = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10,
}


def resistor_label(colors: list[str]) -> str:
    """Return a human-readable label for a resistor based on color bands.

    The last color is treated as the tolerance band, the second-to-last as the
    multiplier band, and any preceding colors as significant digits.

    :param colors: Resistor color bands in order from first to last.
    :returns: Formatted label such as ``"4.7 kiloohms ±5%"``.
    """
    if not colors or not colors[0] or colors == ["black"]:
        return "0 ohms"  # One band resistors only have the color black.

    number: float = (
        sum(COLORS[color] * 10**idx for idx, color in enumerate(colors[-3::-1]))
        * 10 ** COLORS[colors[-2]]
    )

    magni_count: int = 0
    while number >= 1000:
        number /= 1000
        magni_count += 1

    return f"{number:g} {MAGNITUDE[magni_count]}ohms ±{TOLERANCE[colors[-1]]}%"
