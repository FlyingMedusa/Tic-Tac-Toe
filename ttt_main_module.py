import ttt_secondary_module as ts

def show(board):
    print("   A   B   C")
    for id, row in enumerate(board):
        joined_rows = " ".join(row)
        print(id, joined_rows)
    print()


def move(player, board):
    print("Player", player + ",")
    get_position = ts.checking_users_input(board)
    columns = ["A", "B", "C"]
    row, col = get_position.split("-")
    col_index = columns.index(col.upper())
    board[int(row)][col_index] = " " + player + " "

    return board


def current_player(player_x):

    return "X" if player_x else "O"


def is_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] != " . ":
            return True

    for j in range(3):
        if board[0][j] == board[1][j] and board[0][j] == board[2][j] and board[0][j] != " . ":
            return True

    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != " . ":
        return True
    elif board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2] != " . ":
        return True
    else:
        return False
