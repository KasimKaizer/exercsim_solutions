"""Function for implementing the Isogram exercise on Exercism.org"""


def is_isogram(string: str) -> bool:
    """
    Determine if a word or phrase is an isogram.

    An isogram (also known as a "nonpattern word") is a word or phrase without a repeating letter,
    however spaces and hyphens are allowed to appear multiple times.

    :param string: The word or phrase to check.
    :type string: str
    :return: True if the string is an isogram, False otherwise.
    :rtype: bool
    """

    seen = set()
    for char in string.lower():
        if char in seen and char.isalpha():
            return False
        seen.add(char)
    return True
