from random import randrange
import time

def display_board(board):
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")


def enter_move(board):
    ok = False
    while not ok:
        move = input("Enter your move: ")
        ok = move.isdigit() and 1 <= int(move) <= 9
        if not ok:
            print("Bad move - repeat your input!")
            continue

        move = int(move) - 1
        row = move // 3
        col = move % 3
        sign = board[row][col]
        ok = sign not in ['O', 'X']
        if not ok:
            print("Field already occupied - repeat your input!")
            continue

    board[row][col] = 'O'


def make_list_of_free_fields(board):
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['O', 'X']:
                free.append((row, col))
    return free


def victory_for(board, sgn):
    if sgn == "X":
        who = 'me'
    elif sgn == "O":
        who = 'you'
    else:
        who = None

    # Check rows and columns
    for rc in range(3):
        if all(board[rc][c] == sgn for c in range(3)):
            return who
        if all(board[r][rc] == sgn for r in range(3)):
            return who

    # Check diagonals
    if all(board[i][i] == sgn for i in range(3)) or all(board[i][2 - i] == sgn for i in range(3)):
        return who

    return None


def draw_move(board):
    free = make_list_of_free_fields(board)
    cnt = len(free)
    if cnt > 0:
        this = randrange(cnt)
        row, col = free[this]
        board[row][col] = 'X'


def play_game():
    board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
    board[1][1] = 'X'  # Computer starts in the center

    victor = None
    display_board(board)

    while True:
        # --- Player move ---
        enter_move(board)
        display_board(board)
        victor = victory_for(board, 'O')
        if victor is not None:
            break

        free = make_list_of_free_fields(board)
        if not free:
            break

        # --- Computer move ---
        print("Computer's turn...")
        time.sleep(1)  # small delay for realism
        draw_move(board)
        display_board(board)
        victor = victory_for(board, 'X')
        if victor is not None:
            break

        free = make_list_of_free_fields(board)
        if not free:
            break

    # --- Game over ---
    if victor == 'you':
        print("You won!")
    elif victor == 'me':
        print("I won!")
    else:
        print("It's a tie!")

# --- Main loop (replay feature) ---
while True:
    play_game()
    again = input("Play again? (y/n): ").strip().lower()
    if again != 'y':
        print("Thanks for playing! Goodbye.")
        break
    print("\nStarting a new game...\n")
