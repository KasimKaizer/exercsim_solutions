"""Function for implementing the Wordy exercise on Exercism.org"""

import operator
from typing import Callable, Iterator

#: Mapping of recognized operation keywords to their two-operand callables.
_OPERATIONS: dict[str, Callable[[int, int], int]] = {
    "plus": operator.add,
    "minus": operator.sub,
    "multiplied": operator.mul,
    "divided": operator.floordiv,
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
        question.removeprefix("What is").removesuffix("?").replace(" by ", " ").split()
    )

    # handle cases where no number or modifier is provided.
    if not question_list:
        raise ValueError("syntax error")

    itr_tokens: Iterator[str] = iter(question_list)
    try:
        output: int = int(next(itr_tokens))
    except ValueError as exc:
        raise ValueError("syntax error") from exc

    for operation in itr_tokens:
        # validate operand.
        if operation not in _OPERATIONS:
            if operation.removeprefix("-").isdigit():
                raise ValueError("syntax error")
            raise ValueError("unknown operation")

        # validate the next number.
        try:
            next_num = int(next(itr_tokens))
        except (ValueError, StopIteration) as exc:
            raise ValueError("syntax error") from exc

        output = _OPERATIONS[operation](output, next_num)

    return output
