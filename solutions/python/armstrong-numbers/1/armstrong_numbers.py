"""Armstrong Numbers"""


def is_armstrong_number(number):
    """Determine if a number is an Armstrong number.

    An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.

    :param number: int - The number to check.
    :return: bool - True if the number is an Armstrong number, False if it's not.
    """
    str_number = str(number)
    total = 0
    for c in str_number:
        total += int(c) ** len(str_number)
    return total == number
