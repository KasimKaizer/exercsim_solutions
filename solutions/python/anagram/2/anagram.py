"""Function for implementing the Anagram exercise on Exercism.org"""


def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    """Find all candidates that are anagrams of the given word.

    A candidate is an anagram if it contains the same letters as ``word``
    (case-insensitive) but is not identical to ``word`` itself.

    :param word: The target word to compare against.
    :param candidates: The words to test for being anagrams of ``word``.
    :return: The candidates that are anagrams of ``word``.
    """
    word_casefolded = word.casefold()
    word_signature = sorted(word_casefolded)
    return [
        candidate
        for candidate in candidates
        if len(candidate_casefolded := candidate.casefold()) == len(word_casefolded)
        and candidate_casefolded != word_casefolded
        and sorted(candidate_casefolded) == word_signature
    ]
