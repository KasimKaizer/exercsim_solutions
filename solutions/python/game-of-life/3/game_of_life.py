"""Function for implementing the Conway's Game of Life exercise on Exercism.org"""


def tick(matrix: list[list[int]]) -> list[list[int]]:
    """Advance the Game of Life by one tick.

    :param matrix: Current board state of dead (0) and live (1) cells.
    :return: The next board state after applying the rules.
    """
    if not matrix or not matrix[0]:
        return []

    rows, cols = len(matrix), len(matrix[0])
    output: list[list[int]] = [[0] * cols for _ in range(rows)]
    for cur_row, row in enumerate(matrix):
        for cur_col, _ in enumerate(row):
            alive_count: int = sum(
                matrix[new_row][new_col]
                for new_row in range(cur_row - 1, cur_row + 2)
                for new_col in range(cur_col - 1, cur_col + 2)
                if 0 <= new_row < rows
                and 0 <= new_col < cols
                and (new_row != cur_row or new_col != cur_col)
            )
            if alive_count == 2 and matrix[cur_row][cur_col] or alive_count == 3:
                output[cur_row][cur_col] = 1
    return output
