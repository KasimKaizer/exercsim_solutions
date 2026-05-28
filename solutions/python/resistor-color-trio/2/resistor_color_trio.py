"""Function for implementing the Resistor Color Trio exercise on Exercism.org"""

#: Mapping of resistor color names to their digit values.
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

#: List of unit prefixes corresponding to the order of magnitude.
PREFIX = ["", "kilo", "mega", "giga"]


def label(colors: list[str]) -> str:
    """Return the human-readable resistance label for a color trio.

    :param colors: Resistor colors in order (first, second, multiplier).
    :return: Formatted resistance label with the largest suitable unit.
    """
    ohms: int = (COLORS[colors[0]] * 10 + COLORS[colors[1]]) * 10 ** COLORS[colors[2]]
    count: int = 0
    while ohms >= 1000 and ohms % 1000 == 0:
        ohms //= 1000
        count += 1
    return f"{ohms} {PREFIX[count]}ohms"
