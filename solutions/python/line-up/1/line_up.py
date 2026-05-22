"""Function for implementing the Line Up exercise on Exercism.org"""


def line_up(name: str, number: int) -> str:
    """Return a personalized greeting with the customer's ordinal position.

    :param name: Customer name to include in the greeting.
    :param number: Customer position in the queue.
    :return: Formatted greeting with the ordinal suffix.
    """
    end: str = "th"

    if number % 10 == 1 and number % 100 != 11:
        end = "st"

    if number % 10 == 2 and number % 100 != 12:
        end = "nd"

    if number % 10 == 3 and number % 100 != 13:
        end = "rd"

    return f"{name}, you are the {number}{end} customer we serve today. Thank you!"
