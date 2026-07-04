"""Functions for implementing the Binary Search exercise on Exercism.org"""


def find(search_list: list[int], value: int) -> int:
    """Search for a value in a sorted list using binary search.

    :param search_list: Sorted list of integers to search.
    :param value: Integer value to locate.
    :returns: Index of ``value`` in ``search_list``.
    :raises ValueError: If ``value`` is not present in ``search_list``.
    """
    if not len(search_list):
        raise ValueError("value not in array")
    start: int = 0
    end: int = len(search_list)
    while start != end:
        middle: int = start + ((end - start) // 2)
        if search_list[middle] > value:
            end = middle
        elif search_list[middle] < value:
            start = middle + 1
        else:
            return middle

    if search_list[-1] == value:
        return len(search_list) - 1
    else:
        raise ValueError("value not in array")
