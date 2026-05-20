"""Function for implementing the Perfect Numbers exercise on Exercism.org"""


def classify(number: int) -> str:
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    aliquot_sum: int = 0
    fac: int = 1
    while fac * fac <= number:
        if number % fac == 0:
            if fac != number:
                aliquot_sum += fac
            other_num = number // fac
            if other_num != number and other_num != fac:
                aliquot_sum += other_num
        fac += 1
    return (
        "perfect"
        if aliquot_sum == number
        else "abundant"
        if aliquot_sum > number
        else "deficient"
    )
