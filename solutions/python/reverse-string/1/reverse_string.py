"""Function for implementing the Reverse String exercise on Exercism.org"""


def reverse(text: str) -> str:
    """Reverse the characters in a string.

    :param text: Input string to reverse.
    :return: The reversed string.
    """
    output: list[str] = []
    for i in range(len(text) - 1, -1, -1):
        output.append(text[i])
    return "".join(output)
