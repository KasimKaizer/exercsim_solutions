"""Functions for implementing the All Your Base exercise on Exercism.org"""


def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:
    """Convert a list of digits between bases.

    :param input_base: Base of the input digits.
    :param digits: Digits representing a number in ``input_base``.
    :param output_base: Base to convert the number into.
    :returns: Digits representing the same value in ``output_base``.
    :raises ValueError: If ``input_base`` or ``output_base`` is less than 2.
    """
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    return _base_ten_to_other(_to_base_ten(digits, input_base), output_base)


def _to_base_ten(digits: list[int], base: int) -> int:
    """Convert a list of digits in a given base to base 10.

    :param digits: Digits representing a number in ``base``.
    :param base: Base of the input digits.
    :returns: The base-10 integer value.
    :raises ValueError: If any digit is negative or not less than ``base``.
    """
    output: int = 0
    for idx, num in enumerate(digits):
        if num < 0 or num >= base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        output += num * (base ** (len(digits) - idx - 1))
    return output


def _base_ten_to_other(num: int, base: int) -> list[int]:
    """Convert a base-10 integer to a list of digits in another base.

    :param num: Base-10 integer to convert.
    :param base: Target base.
    :returns: Digits representing ``num`` in ``base``.
    """
    output: list[int] = []
    while num > 0:
        output.insert(0, num % base)
        num = num // base
    return output or [0]
