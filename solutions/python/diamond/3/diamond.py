"""Functions for implementing the Diamond exercise on Exercism.org"""

import string


def rows(letter: str) -> list[str]:
    """Generate the diamond rows from ``A`` up to the requested letter.

    :param letter: A single uppercase letter that determines the diamond's widest row.
    :raises ValueError: If ``letter`` is not a single uppercase alphabetic character.
    :return: The full diamond as a list of rows.
    """
    if len(letter) != 1 or letter not in string.ascii_uppercase:
        raise ValueError("Invalid Input")

    output: list[str] = []
    length: int = ord(letter) - ord("A") + 1

    for idx, let in enumerate(string.ascii_uppercase[:length]):
        output.append(_row(let, idx, length))

    _mirror(output)
    return output


def _row(letter: str, idx: int, length: int) -> str:
    """Build a single horizontal row for the diamond.

    :param letter: The letter to place in the row.
    :param idx: The zero-based alphabet position of ``letter`` (``A`` is 0).
    :param length: The width of the left half of the row, including the center.
    :return: A complete diamond row for the given letter with appropriate spacing.
    """
    output: list[str] = [" "] * length
    array_idx: int = length - idx - 1
    output[array_idx] = letter
    _mirror(output)
    return "".join(output)


def _mirror(mirrored_item: list[str]) -> None:
    """Reflect a sequence in place so that it becomes symmetric.

    The list is extended with its own contents reversed, excluding the final
    element so the original last item becomes the shared center.

    :param mirrored_item: The list to mirror; modified in place.
    """
    mirrored_item.extend(mirrored_item[-2::-1])
