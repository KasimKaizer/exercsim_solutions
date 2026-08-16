"""Function for implementing the Darts exercise on Exercism.org"""

from math import sqrt


def score(x: float, y: float) -> int:
    """Calculate the dartboard score for a throw.

    The score is determined by the distance from the center of the board.

    :param x: The x-coordinate of the dart throw.
    :param y: The y-coordinate of the dart throw.
    :returns: The score for the throw based on distance from the center.
    :rtype: int
    """
    dist_from_center: float = sqrt(pow(x, 2) + pow(y, 2))
    return (
        0
        if dist_from_center > 10
        else 1
        if dist_from_center > 5
        else 5
        if dist_from_center > 1
        else 10
    )
