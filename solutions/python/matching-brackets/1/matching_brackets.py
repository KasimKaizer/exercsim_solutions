"""Function for implementing the Matching Brackets exercise on Exercism.org"""

#: Maps each opening bracket to its closing bracket.
BRACKET_MAP: dict[str, str] = {"[": "]", "(": ")", "{": "}"}


def is_paired(input_string: str) -> bool:
    """Check whether every bracket in the input is correctly paired.

    Non-bracket characters are ignored. Brackets must close in the reverse
    order that they were opened.

    :param input_string: Text to scan for bracket pairs.
    :return: ``True`` when all brackets are paired and correctly nested;
        otherwise, ``False``.
    """
    exp_closer_brackets: list[str] = []
    for char in input_string:
        if char not in ("[", "]", "(", ")", "{", "}"):
            continue

        if char in BRACKET_MAP:
            exp_closer_brackets.append(BRACKET_MAP[char])
            continue

        if not exp_closer_brackets or exp_closer_brackets.pop() != char:
            return False

    return not exp_closer_brackets
