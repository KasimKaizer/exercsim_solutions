"""Function for implementing the Sublist exercise on Exercism.org"""


# This exercise stub and the test suite contain several enumerated constants.
# Enumerated constants can be done with a NAME assigned to an arbitrary,
# but unique value. An integer is traditionally used because it’s memory
# efficient.
# It is a common practice to export both constants and functions that work with
# those constants (ex. the constants in the os, subprocess and re modules).
# You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type

# Possible sublist categories.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two) -> int:
    """Classify the relationship between two lists.

    :param list_one: The first list to compare.
    :type list_one: list
    :param list_two: The second list to compare.
    :type list_two: list
    :returns: One of ``SUBLIST``, ``SUPERLIST``, ``EQUAL``, or ``UNEQUAL``.
    :rtype: int
    """
    if list_one == list_two:
        return EQUAL

    smaller = list_one if len(list_one) <= len(list_two) else list_two
    larger = list_two if smaller == list_one else list_one

    if _is_sublist(larger, smaller):
        return SUBLIST if list_one == smaller else SUPERLIST

    return UNEQUAL


def _is_sublist(larger, smaller) -> bool:
    """Check whether ``smaller`` is a contiguous sublist of ``larger``.

    This uses the Knuth–Morris–Pratt (KMP) algorithm for linear-time complexity.

    :param larger: The list to search within.
    :type larger: list
    :param smaller: The candidate sublist to match.
    :type smaller: list
    :returns: ``True`` if ``smaller`` appears in ``larger``; otherwise ``False``.
    :rtype: bool
    """
    if len(smaller) == 0:
        return True

    lps = [0] * len(smaller)
    prev_lps, idx = 0, 1
    while idx < len(smaller):
        if smaller[idx] == smaller[prev_lps]:
            lps[idx] = prev_lps + 1
            prev_lps, idx = prev_lps + 1, idx + 1
        elif prev_lps == 0:
            lps[idx] = 0
            idx += 1
        else:
            prev_lps = lps[prev_lps - 1]

    sml_idx, lrg_idx = 0, 0
    while lrg_idx < len(larger):
        if larger[lrg_idx] == smaller[sml_idx]:
            lrg_idx, sml_idx = lrg_idx + 1, sml_idx + 1
        else:
            if sml_idx == 0:
                lrg_idx += 1
            else:
                sml_idx = lps[sml_idx - 1]
        if sml_idx == len(smaller):
            return True

    return False
