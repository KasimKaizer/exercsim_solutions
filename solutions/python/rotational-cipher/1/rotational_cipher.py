"""Function for implementing the Rotational Cipher exercise on Exercism.org"""


def rotate(text: str, key: int) -> str:
    """Rotate alphabetic characters in ``text`` by ``key`` positions.

    Non-alphabetic characters are preserved as-is. Uppercase and lowercase
    letters remain in their original case.

    :param text: Input text to transform.
    :type text: str
    :param key: Rotation amount (0-25).
    :type key: int
    :return: The rotated text.
    :rtype: str
    """
    builder = []
    for char in text:
        if char.isupper():
            builder.append(chr(((ord(char) - ord("A") + key) % 26) + ord("A")))
        elif char.islower():
            builder.append(chr(((ord(char) - ord("a") + key) % 26) + ord("a")))
        else:
            builder.append(char)
    return "".join(builder)
