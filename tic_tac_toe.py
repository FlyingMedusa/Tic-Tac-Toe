import ttt_main_module as tm
import ttt_secondary_module as ts

print("Hint for beginners:\nBoard settings:")
print("\t0-A\t0-B\t0-C\n\t1-A\t1-B\t1-C\n\t2-A\t2-B\t2-C\n")

while True:

    board = [
        [' . ', ' . ', ' . '],
        [' . ', ' . ', ' . '],
        [' . ', ' . ', ' . ']
    ]

    tm.show(board)

    move_counter = 0
    x = True
    while move_counter < 9:
        board = tm.move(tm.current_player(x), board)
        tm.show(board)
        if tm.is_winner(board):
            break
        move_counter += 1
        x = not x

    if x:
        winner = "X"
    else:
        winner = "O"

    print("Congratulations to the player", winner + "!")

    answer = ts.run_again()
    if answer == 'y':
        print("\n-----New game-----\n")
        continue
    else:
        print('Goodbye!')
        break
