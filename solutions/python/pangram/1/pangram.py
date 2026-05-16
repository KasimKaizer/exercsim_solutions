"""Function for implementing the Pangram exercise on Exercism.org"""


def is_pangram(sentence: str) -> bool:
    """
    Determine if a sentence is a pangram.

    A pangram is a sentence using every letter of the alphabet at least once.

    :param sentence: The string to be evaluated.
    :type sentence: str
    :return: True if the sentence contains every letter of the alphabet, False otherwise.
    :rtype: bool
    """

    return (
        True
        if len(set(char for char in sentence.lower() if char.isalpha())) == 26
        else False
    )
