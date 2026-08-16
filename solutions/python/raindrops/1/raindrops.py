"""Function for implementing the Raindrops exercise on Exercism.org"""


def convert(number: int) -> str:
    """
    Convert a number to a string, the contents of which depend on the number's factors.

    If the number has 3 as a factor, add 'Pling' to output.
    If the number has 5 as a factor, add 'Plang' to output.
    If the number has 7 as a factor, add 'Plong' to output.
    If the number does not have 3, 5, or 7 as a factor, just return the number as a string.

    :param number: The number to convert.
    :type number: int
    :return: The converted string.
    :rtype: str
    """

    output = ""
    if number % 3 == 0:
        output += "Pling"
    if number % 5 == 0:
        output += "Plang"
    if number % 7 == 0:
        output += "Plong"
    return output or str(number)
