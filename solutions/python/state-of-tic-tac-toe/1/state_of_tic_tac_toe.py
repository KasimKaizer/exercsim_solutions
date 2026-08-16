"""Function for implementing the State of Tic-Tac-Toe exercise on Exercism.org"""


def gamestate(board: list[str]) -> str:
    """Return the state of a tic-tac-toe game.

    :param board: A three-by-three board whose cells contain ``"X"``, ``"O"``,
        or a space.
    :return: ``"win"`` if either player has won, ``"draw"`` if the board is
        full without a winner, or ``"ongoing"`` otherwise.
    :raises ValueError: If the move order is invalid, a move was made after a
        player won.
    """
    seen: set[tuple[int, int]] = set()
    number_of_moves: dict[str, int] = {"X": 0, "O": 0}
    won: dict[str, bool] = {"X": False, "O": False}

    for cur_row in range(3):
        for cur_col in range(3):
            # skip empty spaces
            if board[cur_row][cur_col] == " ":
                continue

            # add whichever player is seen (X or O)
            number_of_moves[board[cur_row][cur_col]] += 1
            for new_row in range(cur_row - 1, cur_row + 2):
                for new_col in range(cur_col - 1, cur_col + 2):
                    # invalid position
                    if not (0 <= new_row < 3 and 0 <= new_col < 3) or (
                        new_row == cur_row and new_col == cur_col
                    ):
                        continue

                    # not possible for win position
                    if (
                        (
                            board[new_row][new_col] != board[cur_row][cur_col]
                        )  # not the same player
                        or (new_row, new_col) in seen  # already checked position
                        or 1 not in (new_row, new_col)  # not middle position
                    ):
                        continue

                    # third row
                    third_row = 2 * new_row - cur_row
                    third_col = 2 * new_col - cur_col

                    # check if the next winning position from here is the same
                    if (
                        not (0 <= third_row < 3 and 0 <= third_col < 3)
                        or board[third_row][third_col] != board[cur_row][cur_col]
                    ):
                        continue

                    won[board[cur_row][cur_col]] = True
            seen.add((cur_row, cur_col))

    # check if x went twice
    if number_of_moves["X"] > number_of_moves["O"] + 1:
        raise ValueError("Wrong turn order: X went twice")
    # check if O started
    if number_of_moves["O"] > number_of_moves["X"]:
        raise ValueError("Wrong turn order: O started")
    # check is they played after someone won
    if (won["X"] and (number_of_moves["O"] == number_of_moves["X"])) or (
        won["O"] and (number_of_moves["X"] > number_of_moves["O"])
    ):
        raise ValueError(
            "Impossible board: game should have ended after the game was won"
        )
    # check if the game is won
    if won["X"] or won["O"]:
        return "win"
    # check if the game is a draw
    if number_of_moves["O"] + number_of_moves["X"] == 9:
        return "draw"
    return "ongoing"
