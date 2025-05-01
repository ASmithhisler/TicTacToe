from art import logo
lines = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
letters = ["A", "B", "C"]

print(logo)

retry = True
while retry:
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

    x_won = False
    o_won = False

    game_is_on = True
    while game_is_on:
        for player in players:
            invalid = True
            while invalid:
                position = input(f"{player}, type a position: ").upper()
                if len(position) == 2 and position[0] in letters:
                    char = position[0]
                    for i in range(len(letters)):
                        if char == letters[i]:
                            char = i

                    num = position[1]
                    try:
                        if lines[int(num) - 1][int(char)] == " ":
                            invalid = False
                            if player == "X":
                                lines[int(num) - 1][int(char)] = "X"
                            if player == "O":
                                lines[int(num) - 1][int(char)] = "O"
                        else:
                            print("That position is already occupied.\n")
                    except ValueError:
                        print("That position is invalid.\n")
                    except IndexError:
                        print("That position is out of range.\n")
                else:
                    print("That position is invalid.\n")

            board = ""
            for c in range(0, 3):
                for r in range(0, 3):
                    board += f" {lines[r][c]} "
                    if r < 2:
                        board += "|"
                board += "\n"
                if c < 2:
                    board += "-----------\n"
            print(board)

            for c in range(0, 3):
                rX = 0; cX = 0
                rO = 0; cO = 0
                for r in range(0, 3):
                    if lines[r][c] == "X":
                        rX += 1
                    if lines[c][r] == "X":
                        cX += 1
                    if rX == 3 or cX == 3:
                        x_won = True
                    if lines[r][c] == "O":
                        rO += 1
                    if lines[c][r] == "O":
                        cO += 1
                    if rO == 3 or cO == 3:
                        o_won = True

            if x_won or o_won:
                break

        if x_won or o_won:
            game_is_on = False
            if x_won:
                print(f"X, you won!")
            if o_won:
                print(f"O, you won!")
            restart = input("Type 'y' to go again: ")
            if restart != "y":
                retry = False
                print("Thanks for playing!")
            print()
