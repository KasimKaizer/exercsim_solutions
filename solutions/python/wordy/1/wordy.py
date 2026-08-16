"""Function for implementing the Wordy exercise on Exercism.org"""

from typing import Callable

#: Mapping of recognized operation keywords to their two-operand callables.
_OPERATIONS: dict[str, Callable[[int, int], int]] = {
    "plus": lambda num1, num2: num1 + num2,
    "minus": lambda num1, num2: num1 - num2,
    "multiplied": lambda num1, num2: num1 * num2,
    "divided": lambda num1, num2: num1 // num2,
}


def answer(question: str) -> int:
    """Parse and evaluate a wordy math question.

    Evaluates operations left-to-right.

    :param question: A natural-language math question
        (e.g. ``"What is 5 plus 3?"``).
    :returns: The integer result of the evaluated expression.
    :raises ValueError: If the question contains a syntax error or an
        unknown operation.
    """
    question_list: list[str] = (
        question.removeprefix("What is").removesuffix("?").replace("by", "").split()
    )

    # handle cases where no number or modifier is provided.
    if not question_list or not _is_int(question_list[0]):
        raise ValueError("syntax error")

    output: int = int(question_list[0])

    for idx in range(1, len(question_list), 2):
        # validate operand.
        if question_list[idx] not in _OPERATIONS:
            raise (
                ValueError("syntax error")
                if _is_int(question_list[idx])
                else ValueError("unknown operation")
            )
        # validate the next number.
        if idx + 1 >= len(question_list) or not _is_int(question_list[idx + 1]):
            raise ValueError("syntax error")

        output = _OPERATIONS[question_list[idx]](output, int(question_list[idx + 1]))

    return output


def _is_int(val: str) -> bool:
    """Check whether *val* represents an integer, optionally negative.

    :param val: The string to test.
    :returns: ``True`` if *val* is a integer, ``False`` otherwise.
    """
    return val.removeprefix("-").isnumeric()
