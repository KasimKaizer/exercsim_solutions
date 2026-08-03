"""Function for implementing the Eliud's Eggs exercise on Exercism.org"""


def egg_count(remaining_value: int) -> int:
    """Count the eggs represented by the set bits in a display value.

    :param remaining_value: Decimal value whose set bits represent eggs.
    :return: Number of set bits in ``remaining_value``.
    """
    total: int = 0
    while remaining_value > 0:
        remaining_value = remaining_value & (remaining_value - 1)
        total += 1
    return total


# Alternative implementation
# def egg_count(remaining_value: int) -> int:
#     total: int = 0
#     while remaining_value > 0:
#         total += remaining_value & 1
#         remaining_value >>= 1
#     return total
