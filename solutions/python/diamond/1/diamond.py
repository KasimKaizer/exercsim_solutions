def rows(letter: str) -> list[str]:
    """Generate the diamond rows from ``A`` up to the requested letter.

    :param letter: The uppercase letter that determines the diamond's widest row.
    :return: The full diamond as a list of rows.
    """
    output: list[str] = []
    length: int = ord(letter) - ord("A") + 1

    for lett_num in range(ord("A"), ord("A") + length):
        output.append(_row(chr(lett_num), length))

    output.extend(output[-2::-1])
    return output


def _row(letter: str, length: int) -> str:
    """Build a single horizontally row for the diamond.

    :param letter: The letter to place in the row.
    :param length: The width of the left half of the row, including the center.
    :return: A complete diamond row for the given letter with appropriate spacing.
    """
    output: list[str] = [" "] * length
    idx: int = length - (ord(letter) - ord("A")) - 1
    output[idx] = letter
    output.extend(output[-2::-1])
    return "".join(output)
