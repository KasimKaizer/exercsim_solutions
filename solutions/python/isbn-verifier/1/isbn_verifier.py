"""Function for implementing the ISBN Verifier exercise on Exercism.org"""


def is_valid(isbn: str) -> bool:
    """Determine whether an ISBN-10 string is valid.

    The function accepts ISBN-10 strings that may include hyphens. It validates
    format (10 characters after hyphen removal, numeric digits with an optional
    trailing ``X``) and checksum correctness.

    :param isbn: The ISBN-10 candidate, optionally containing hyphens.
    :type isbn: str
    :return: ``True`` if the ISBN-10 is well-formed and checksum-valid;
        otherwise ``False``.
    :rtype: bool
    """

    isbn = isbn.replace("-", "")
    if len(isbn) != 10:
        return False
    if not isbn.removesuffix("X").isdigit():
        return False
    return (
        sum(
            (10 if char == "X" else int(char)) * (10 - idx)
            for idx, char in enumerate(isbn)
        )
        % 11
        == 0
    )
