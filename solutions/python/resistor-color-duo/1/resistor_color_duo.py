"""Function for implementing the Resistor Color Duo exercise on Exercism.org"""

#: Mapping of resistor color names to their digit values.
COLOR_CODES: dict[str, int] = {
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


def value(colors: list[str]) -> int:
    """Compute the two-digit resistor value from the first two colors.

    :param colors: Color names in order; only the first two are used.
    :return: Two-digit resistor value.
    """
    return COLOR_CODES[colors[0]] * 10 + COLOR_CODES[colors[1]]


# its 2 am and I am sleepy as f, IDK what came over me to overcomplicate this so fing much,
# but I do feel extremely stupid for not going with the simplest option in the starting.
# def value(colors: list[str]) -> int:
#     return sum(
#         COLOR_CODES[color] * (10**idx) for idx, color in enumerate(colors[1::-1])
#     )
