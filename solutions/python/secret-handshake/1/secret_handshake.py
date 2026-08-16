"""Function for implementing the Secret Handshake exercise on Exercism.org"""

#: Ordered list of handshake actions. The index of each action is its bit
#: position, so the action at index ``i`` is selected when bit ``1 << i`` is set.
GREETINGS: list[str] = [
    "wink",
    "double blink",
    "close your eyes",
    "jump",
]

#: Bit flag that reverses the order of the selected actions.
REVERSE: int = 1 << len(GREETINGS)


def commands(binary_str: str) -> list[str]:
    """Convert a binary handshake code into its sequence of actions.

    Each low-order bit selects the action at the matching index in
    ``GREETINGS``, read from the right-most digit moving left. If the
    ``REVERSE`` bit (one above the action bits) is set, the resulting
    sequence of actions is reversed.

    :param binary_str: Binary string whose bits select handshake actions.
    :returns: The ordered list of handshake actions.
    """
    num: int = int(binary_str, 2)
    output: list[str] = [
        action for idx, action in enumerate(GREETINGS) if num & (1 << idx)
    ]
    return output[::-1] if num & REVERSE else output
