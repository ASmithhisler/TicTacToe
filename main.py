from art import logo
lines = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
letters = ["A", "B", "C"]

print(logo)

players = []

player1 = ""
while player1 != "X" and player1 != "O":
    player1 = input("Choose 'x' or 'o': ").upper()
players.append(player1)

if player1 == "X":
    player2 = "O"
else:
    player2 = "X"
players.append(player2)

retry = True
while retry == True:
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
        for r in range(0, 3):
            for c in range(0, 3):
                board += f" {lines[c][r]} "
                if c < 2:
                    board += "|"
            board += "\n"
            if r < 2:
                board += "-----------\n"
        print(board)

