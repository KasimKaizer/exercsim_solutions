def steps(number: int) -> int:
    """
    Calculate the number of steps required to reach 1 using the Collatz Conjecture.

    :param number: int - The starting positive integer.
    :returns: int - The number of steps taken to reach 1.
    :raises: ValueError - If the provided number is 0 or negative.
    """
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    count: int = 0
    while number != 1:
        count = count + 1
        if (number % 2) == 0:
            number //= 2
        else:
            number = (number * 3) + 1
    return count
