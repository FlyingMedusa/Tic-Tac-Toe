
def anti_duplicate(board, pos):
    row, col = pos.split("-")
    col = col.upper()
    col_dict = {"A": 0, "B": 1, "C": 2}
    if board[int(row)][col_dict[col]] != ' . ':
        return False
    else:
        return True


def checking_users_input(board):
    num_index = "012"
    al_index = "ABC"

    while True:

        pos = input("mark position: ")
        if len(pos) == 3 and pos[0] in num_index and pos[1] == "-" and pos[2].upper() in al_index and anti_duplicate(board, pos):
            break
        elif len(pos) == 3 and pos[0] in num_index and pos[1] == "-" and pos[2].upper() in al_index:
            print('This position is already taken - choose another one!')
        else:
            print('Invalid input. Remember to and to give a cluster of:\n'
                  '  an index number of a row\n  a hyphen\n  an index letter of a column\n')

    return pos


def run_again():
    while True:
        answer = input('Do you want to run again? (y/n): ')
        if answer in ('y', 'n'):
            break
        print('Invalid input.')

    return answer
