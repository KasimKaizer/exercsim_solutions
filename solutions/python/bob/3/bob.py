"""Function for implementing the Bob exercise on Exercism.org"""


def response(hey_bob: str) -> str:
    """
    Determine Bob's conversational response based on the input remark.

    Bob is a lackadaisical teenager who answers based on the tone of the remark:
    - If you ask him a question, he answers "Sure."
    - If you yell at him (all uppercase), he answers "Whoa, chill out!"
    - If you yell a question at him, he answers "Calm down, I know what I'm doing!"
    - If you address him without actually saying anything, he answers "Fine. Be that way!"
    - For anything else, he answers "Whatever."

    :param hey_bob: The remark addressed to Bob.
    :return: Bob's response string.
    """

    hey_bob = hey_bob.rstrip()
    if hey_bob == "":
        return "Fine. Be that way!"

    is_question = hey_bob.endswith("?")
    is_yelling = hey_bob.isupper()

    if is_question and is_yelling:
        return "Calm down, I know what I'm doing!"

    if is_question:
        return "Sure."

    if is_yelling:
        return "Whoa, chill out!"

    return "Whatever."
