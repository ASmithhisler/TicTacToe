from art import logo
lines = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
letters = ["A", "B", "C"]

print(logo)

player = input("Type 'x' or 'o': ").lower()
position = input("Type a position: ").upper()

char = position[0]
for i in range(len(letters)):
    if char == letters[i]:
        char = i

num = position[1]
if player == "x":
    lines[int(num) - 1][int(char)] = "X"
if player == "o":
    lines[int(num) - 1][int(char)] = "O"

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
