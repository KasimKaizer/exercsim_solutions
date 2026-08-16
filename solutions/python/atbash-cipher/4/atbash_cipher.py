"""Function for implementing the Atbash Cipher exercise on Exercism.org"""

#: Translation table mapping each letter to its corresponding letter in the reversed alphabet.
_ATBASH_TRANSLATE = str.maketrans(
    "abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba"
)


def encode(plain_text: str) -> str:
    """Encode plaintext using the Atbash cipher.

    :param plain_text: The text to encode.
    :return: The encoded text grouped in blocks of five characters.
    """
    translated_text = "".join(
        char
        for char in plain_text.lower().translate(_ATBASH_TRANSLATE)
        if char.isalnum()
    )
    return " ".join(
        translated_text[idx : idx + 5] for idx in range(0, len(translated_text), 5)
    )


def decode(ciphered_text: str) -> str:
    """Decode Atbash cipher text.

    :param ciphered_text: The text to decode.
    :return: The decoded plaintext without spacing.
    """
    return ciphered_text.replace(" ", "").translate(_ATBASH_TRANSLATE)
