"""Grains"""


def square(number):
    """
    Calculate the number of of grains on a given square on the chessboard.

    :param number: int - The square number
    :returns: int - The total number of grains on the given square.
    :raises: ValueError - If the provided number is less than 1 or greater then 64.
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 1 << (number - 1)


def total():
    """
    Calculate the total number of grains on the chessboard.

    :returns: int - Total grains on the chessboard.
    """
    return (1 << 64) - 1
