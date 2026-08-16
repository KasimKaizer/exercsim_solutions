"""Functions for implementing the Leap exercise on Exercism.org"""


def leap_year(year):
    """Determine if a given year is a leap year.

    A leap year in the Gregorian calendar occurs:
    - On every year that is evenly divisible by 4
    - Except every year that is evenly divisible by 100
    - Unless the year is also evenly divisible by 400

    :param year: The year to check.
    :returns: True if the year is a leap year, False otherwise.
    """
    return (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))
