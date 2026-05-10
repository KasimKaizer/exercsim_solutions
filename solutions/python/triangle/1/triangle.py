"""Functions for implementing the Triangle exercise on Exercism.org"""


def equilateral(sides):
    """Determine if a triangle is equilateral.

    An equilateral triangle has all three sides the same length.

    :param sides: A list or tuple of three numbers representing the side lengths.
    :return: True if the triangle is equilateral, False otherwise.
    """
    if not is_triangle(sides):
        return False
    return sides[0] == sides[1] == sides[2]


def isosceles(sides):
    """Determine if a triangle is isosceles.

    An isosceles triangle has at least two sides the same length.

    :param sides: A list or tuple of three numbers representing the side lengths.
    :return: True if the triangle is isosceles, False otherwise.
    """
    if not is_triangle(sides):
        return False
    return (sides[0] == sides[1]) or (sides[1] == sides[2]) or (sides[2] == sides[0])


def scalene(sides):
    """Determine if a triangle is scalene.

    A scalene triangle has all sides of different lengths.

    :param sides: A list or tuple of three numbers representing the side lengths.
    :return: True if the triangle is scalene, False otherwise.
    """
    if not is_triangle(sides):
        return False
    return (sides[0] != sides[1]) and (sides[0] != sides[2]) and (sides[1] != sides[2])


def is_triangle(sides):
    """Check if the given sides form a valid triangle.

    For a shape to be a triangle, all sides must have length > 0, and the sum of
    the lengths of any two sides must be greater than or equal to the length of the third side.

    :param sides: A list or tuple of three numbers representing the side lengths.
    :return: True if the sides form a valid triangle, False otherwise.
    """
    for side in sides:
        if side <= 0:
            return False
    return (
        (sides[0] + sides[1] >= sides[2])
        and (sides[1] + sides[2] >= sides[0])
        and (sides[2] + sides[0] >= sides[1])
    )
