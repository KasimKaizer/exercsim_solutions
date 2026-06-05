"""Function for implementing the Atbash Cipher exercise on Exercism.org"""


def encode(plain_text: str) -> str:
    """Encode plaintext using the Atbash cipher.

    :param plain_text: The text to encode.
    :return: The encoded text grouped in blocks of five characters.
    """
    return atbash(plain_text, spaces=True)


def decode(ciphered_text: str) -> str:
    """Decode Atbash cipher text.

    :param ciphered_text: The text to decode.
    :return: The decoded plaintext without spacing.
    """
    return atbash(ciphered_text, spaces=False)


def atbash(text: str, spaces: bool) -> str:
    """Apply the Atbash transform to text.

    :param text: The input text to transform.
    :param spaces: Whether to insert spaces every five characters.
    :return: The transformed text.
    """
    output: list[str] = []
    count: int = 0
    for char in text:
        if not char.isalnum():
            continue  # skip non alpha numerical characters

        # add a space after every 5 characters.
        if spaces and count == 5:
            output.append(" ")
            count = 0
        count += 1

        # add numbers as is to the output.
        if char.isnumeric():
            output.append(char)
            continue

        # convert alpha characters.
        new_pos: int = 25 - ord(char.lower()) + ord("a")
        output.append(chr(ord("a") + new_pos))

    return "".join(output)
