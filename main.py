from art import logo
letters = ["A", "B", "C"]
numbers = [0, 1, 2]


def check_position(position, char, num):
    if len(position) == 2:
        if char not in numbers:
            print("That letter is invalid.\n")
            return True
        try:
            if lines[int(num) - 1][char] == " ":
                return False
            else:
                print("That position is already occupied.\n")
        except ValueError:
            print("That number is invalid.\n")
        except IndexError:
            print("That position is out of range.\n")
    else:
        print("That position is invalid.\n")
    return True


def update_board(lines):
    board = ""
    for c in range(0, 3):
        for r in range(0, 3):
            board += f" {lines[r][c]} "
            if r < 2:
                board += "|"
        board += "\n"
        if c < 2:
            board += "-----------\n"
    return board


def check_for_row(lines):
    for c in range(0, 3):
        hor_x = 0
        ver_x = 0

        hor_o = 0
        ver_o = 0
        for r in range(0, 3):
            if lines[r][c] == "X":
                hor_x += 1
            if lines[c][r] == "X":
                ver_x += 1
            if hor_x == 3 or ver_x == 3:
                return True, "X"

            if lines[r][c] == "O":
                hor_o += 1
            if lines[c][r] == "O":
                ver_o += 1
            if hor_o == 3 or ver_o == 3:
                return True, "O"
    return False, ""


def check_for_diagonal(lines, inv_lines):
    pos_x = 0
    neg_x = 0

    pos_o = 0
    neg_o = 0
    for d in range(0, 3):
        if lines[d][d] == "X":
            neg_x += 1
        if inv_lines[d][d] == "X":
            pos_x += 1
        if pos_x == 3 or neg_x == 3:
            return True, "X"

        if lines[d][d] == "O":
            neg_o += 1
        if inv_lines[d][d] == "O":
            pos_o += 1
        if pos_o == 3 or neg_o == 3:
            return True, "O"
    return False, ""


def check_for_tie(occupied_squares):
    for c in range(0, 3):
        for r in range(0, 3):
            if lines[r][c] == "X" or lines[r][c] == "O":
                occupied_squares += 1
            if occupied_squares == 9:
                return True
    return False


print(logo)

retry = True
while retry:
    lines = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    players = []

    player1 = ""
    while player1 != "X" and player1 != "O":
        player1 = input("Choose 'x' or 'o': ").upper()

    if player1 == "X":
        player2 = "O"
        players.append(player1)
        players.append(player2)
    else:
        player2 = "X"
        players.append(player2)
        players.append(player1)

    won = [None, ""]
    tie = False

    game_is_on = True
    while game_is_on:
        for player in players:
            invalid = True
            while invalid:
                position = input(f"{player}, type a position: ").upper()

                char = position[0]
                for i in range(len(letters)):
                    if char == letters[i]:
                        char = i

                num = position[1]

                invalid = check_position(position, char, num)
                if invalid:
                    continue

                if player == "X":
                    lines[int(num) - 1][char] = "X"
                if player == "O":
                    lines[int(num) - 1][char] = "O"

            print(update_board(lines))

            won = check_for_row(lines)
            if won[0] == False:
                inv_lines = [lines[2], lines[1], lines[0]]
                won = check_for_diagonal(lines, inv_lines)

            occupied_squares = 0
            tie = check_for_tie(occupied_squares)

            if won[0] or tie:
                game_is_on = False
                if won[1] == "X":
                    print("X, you won!")
                if won[1] == "O":
                    print("O, you won!")
                if tie:
                    print("It was a tie!")
                restart = input("Type 'y' to go again: ")
                if restart != "y":
                    retry = False
                    print("Thanks for playing!")
                print()
                break
