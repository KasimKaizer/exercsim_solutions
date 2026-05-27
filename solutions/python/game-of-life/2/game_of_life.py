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
            alive_count = sum(
                matrix[ver + d_ver][hor + d_hor]
                for d_hor, d_ver in DIRECTIONS
                if (0 <= hor + d_hor < len(matrix[ver]))
                and (0 <= ver + d_ver < len(matrix))
            )
            if (2 == alive_count and matrix[ver][hor]) or alive_count == 3:
                output[ver][hor] = 1
    return output
