"""Function for implementing the Line Up exercise on Exercism.org"""


def line_up(name: str, number: int) -> str:
    """Return a personalized greeting with the customer's ordinal position.

    :param name: Customer name to include in the greeting.
    :param number: Customer position in the queue.
    :return: Formatted greeting with the ordinal suffix.
    """
    last: int = number % 10
    last_two: int = number % 100

    suffix: str = "th"
    if last_two in {11, 12, 13}:
        suffix = "th"
    elif last == 1:
        suffix = "st"
    elif last == 2:
        suffix = "nd"
    elif last == 3:
        suffix = "rd"

    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"
