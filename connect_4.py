board = [' ' for _ in range(42)]
marks = ('X', 'O')

score_X = {
    "wins": 0,
    "loses": 0,
    "draws": 0
}

def check_win():
    winning_combinations = [
     # Horizontal
    [0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6],
    [7, 8, 9,10], [8, 9,10,11], [9,10,11,12], [10,11,12,13],
    [14,15,16,17], [15,16,17,18], [16,17,18,19], [17,18,19,20],
    [21,22,23,24], [22,23,24,25], [23,24,25,26], [24,25,26,27],
    [28,29,30,31], [29,30,31,32], [30,31,32,33], [31,32,33,34],
    [35,36,37,38], [36,37,38,39], [37,38,39,40], [38,39,40,41],

    # Vertical
    [0, 7,14,21], [7,14,21,28], [14,21,28,35],
    [1, 8,15,22], [8,15,22,29], [15,22,29,36],
    [2, 9,16,23], [9,16,23,30], [16,23,30,37],
    [3,10,17,24], [10,17,24,31], [17,24,31,38],
    [4,11,18,25], [11,18,25,32], [18,25,32,39],
    [5,12,19,26], [12,19,26,33], [19,26,33,40],
    [6,13,20,27], [13,20,27,34], [20,27,34,41],

    # Diagonal Up (↗)
    [0, 8,16,24], [1, 9,17,25], [2,10,18,26], [3,11,19,27],
    [7,15,23,31], [8,16,24,32], [9,17,25,33], [10,18,26,34],
    [14,22,30,38], [15,23,31,39], [16,24,32,40], [17,25,33,41],

    # Diagonal Down (↘)
    [21,15,9,3], [22,16,10,4], [23,17,11,5], [24,18,12,6],
    [28,22,16,10], [29,23,17,11], [30,24,18,12], [31,25,19,13],
    [35,29,23,17], [36,30,24,18], [37,31,25,19], [38,32,26,20]
    ]

    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] == board[combination[3]] != ' ':
            return board[combination[0]]

    return None


def print_board():
    print()
    for row in range(6):
        for col in range(7):
            print(f"| {board[row * 7 + col]}", end=" ")
        print("|")
    print("-" * 29)
    print("  1   2   3   4   5   6   7 ")


def set_mark(position: int, mark: str):
    for i in range(5, -1, -1):
        idx = i * 7 + position
        if board[idx] == ' ':
            board[idx] = mark
            return True
    print("Column is full. Choose another one.")
    return False





def play(mark: str):
    while True:
        try:
            position = int(input(f"Enter column (1-7) for {mark}: ")) - 1
            if 0 <= position < 7:
                if set_mark(position, mark):
                    break
            else:
                print("Invalid input. Choose a column between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def print_score():
    print()
    print("=============================")
    print("Player | Wins | Loses | Draws")
    print("=============================")
    print(f"X      | {score_X['wins']}    | {score_X['loses']}     | {score_X['draws']}")
    print("=============================")
    print(f"O      | {score_X['loses']}    | {score_X['wins']}     | {score_X['draws']}")
    print("=============================")
    print()


print("Welcome to Connect Four!")
while True:
    board = [' ' for _ in range(42)]

    user_input = input("Do you want to play a game? (y/N): ").lower()
    while not user_input in "yn":
        print("Invalid answer.")
        user_input = input("Do you want to play a game? (y/N): ").lower()

    if user_input == "n":
        print("Thanks for playing!")
        break

    print()

    player_turn = 0
    turns = 0
    winner = None

    print_board()
    
    while winner == None and turns < 42:
        play(marks[abs(player_turn)])
        print_board()
        winner = check_win()

        player_turn = abs(player_turn) - 1
        turns += 1

    if not winner:
        print("It's a Draw!")
        score_X["draws"] += 1
    else:
        print(f"Congratulations {winner}, you won!")
        if winner == "X":
            score_X["wins"] += 1
        else:
            score_X["loses"] += 1
    
    print_score()