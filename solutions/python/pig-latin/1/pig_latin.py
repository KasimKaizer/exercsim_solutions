"""Function for implementing the Pig Latin exercise on Exercism.org"""

import re


def translate(text: str) -> str:
    """
    Translates a given text into Pig Latin.

    :param text: A string containing one or more words to be translated.
    :type text: str
    :return: The translated Pig Latin string.
    :rtype: str
    """
    return " ".join(translate_word(word) for word in text.split())


def translate_word(word: str) -> str:
    """
    Translates a single word into Pig Latin based on specific rules.

    :param word: A single word string to be translated.
    :type word: str
    :return: The translated Pig Latin word.
    :rtype: str
    """
    # rule 1: begins with vowel or "xr" or "yt".
    if word.startswith(("a", "e", "i", "o", "u", "xr", "yt")):
        return word + "ay"

    # rule 3: begins with zero or more consonants followed by "qu".
    if "qu" in word:
        pos = word.find("qu")
        if not re.search(r"[aeiou]", word[:pos]):
            return word[pos + 2 :] + word[: pos + 2] + "ay"

    # rule 4: begins with one or more consonants followed by "y".
    if not word.startswith("y") and "y" in word:
        pos = word.find("y")
        if not re.search(r"[aeiou]", word[:pos]):
            return word[pos:] + word[:pos] + "ay"

    # rule 2: begins with consonant.
    match = re.search(r"[aeiou]", word)
    if match:
        pos = match.start()
        return word[pos:] + word[:pos] + "ay"
    return word
