"""Functions for implementing the Resistor Color exercise on Exercism.org"""

#: Ordered list of resistor colors.
COLORS_LIST: list[str] = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]


def color_code(color: str) -> int:
    """Return the numeric code for a resistor color.

    :param color: The color name to look up.
    :returns: The integer code associated with the color.
    :raises ValueError: If ``color`` is not a valid resistor color.
    """
    return COLORS_LIST.index(color)


def colors() -> list[str]:
    """Return the list of valid resistor colors in order.

    :returns: Ordered list of color names.
    """
    return COLORS_LIST
