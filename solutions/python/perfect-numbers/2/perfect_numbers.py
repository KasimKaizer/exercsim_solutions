"""Function for implementing the Perfect Numbers exercise on Exercism.org"""

from math import isqrt


def classify(number: int) -> str:
    """Classify a positive integer as perfect, abundant, or deficient.

    :param number: Positive integer to classify.
    :type number: int
    :return: One of "perfect", "abundant", or "deficient".
    :rtype: str
    :raises ValueError: If ``number`` is not a positive integer.
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    ali_sum: int = __aliquot_sum(number)
    return (
        "perfect"
        if ali_sum == number
        else "abundant"
        if ali_sum > number
        else "deficient"
    )


def __aliquot_sum(num: int) -> int:
    """Compute the aliquot sum of a positive integer.

    The aliquot sum is the sum of all positive divisors of ``num`` excluding
    the number itself.

    :param num: Positive integer to evaluate.
    :type num: int
    :return: Sum of proper divisors of ``num``.
    :rtype: int
    """
    if num == 1:
        return 0

    aliquot_sum: int = 1
    for fac in range(2, isqrt(num) + 1):
        if num % fac != 0:
            continue

        aliquot_sum += fac
        other_num = num // fac
        if other_num != fac:
            aliquot_sum += other_num
    return aliquot_sum
