"""Function for implementing the Conway's Game of Life exercise on Exercism.org"""

#: Relative neighbor offsets in (horizontal, vertical) order.
DIRECTIONS: list[tuple[int, int]] = [
    (-1, -1),  # top left (hor, ver)
    (0, -1),  # top (hor, ver)
    (1, -1),  # top right (hor, ver)
    (1, 0),  # right (hor, ver)
    (1, 1),  # bottom right (hor, ver)
    (0, 1),  # bottom (hor, ver)
    (-1, 1),  # bottom left (hor, ver)
    (-1, 0),  # left (hor, ver)
]


def tick(matrix: list[list[int]]) -> list[list[int]]:
    """Advance the Game of Life by one tick.

    :param matrix: Current board state of dead (0) and live (1) cells.
    :return: The next board state after applying the rules.
    """
    output: list[list[int]] = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    for ver, row in enumerate(matrix):
        for hor, _ in enumerate(row):
            alive_count = _get_alive_count(matrix, ver, hor)
            # Any live cell with two or three live neighbors lives on.
            # Any dead cell with exactly three live neighbors becomes a live cell.
            # All other cells die or stay dead.
            if (2 == alive_count and matrix[ver][hor]) or alive_count == 3:
                output[ver][hor] = 1
    return output


def _get_alive_count(matrix: list[list[int]], ver: int, hor: int) -> int:
    """Count live neighbors for a given cell.

    :param matrix: Current board state.
    :param ver: Cell row index.
    :param hor: Cell column index.
    :return: Number of live neighbors around the cell.
    """
    count: int = 0
    for d_hor, d_ver in DIRECTIONS:
        new_ver, new_hor = ver + d_ver, hor + d_hor
        if not (0 <= new_hor < len(matrix[ver])) or not (0 <= new_ver < len(matrix)):
            continue
        if matrix[new_ver][new_hor]:
            count += 1
    return count
