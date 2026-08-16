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
    x_count: int = sum(row.count("X") for row in board)
    o_count: int = sum(row.count("O") for row in board)
    won: dict[str, bool] = {"X": False, "O": False}
    # horizontal win condition
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != " ":
            won[board[row][0]] = True

    # vertical win condition
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            won[board[0][col]] = True

    # diagonal win condition
    if (
        board[0][0] == board[1][1] == board[2][2]
        or board[0][2] == board[1][1] == board[2][0]
    ) and board[1][1] != " ":
        won[board[1][1]] = True

    # check if x went twice
    if x_count > o_count + 1:
        raise ValueError("Wrong turn order: X went twice")
    # check if O started
    if o_count > x_count:
        raise ValueError("Wrong turn order: O started")
    # check is they played after someone won
    if (won["X"] and (o_count == x_count)) or (won["O"] and (x_count > o_count)):
        raise ValueError(
            "Impossible board: game should have ended after the game was won"
        )
    return (
        "win"
        if won["X"] or won["O"]
        else "draw"
        if o_count + x_count == 9
        else "ongoing"
    )
