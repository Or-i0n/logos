# Program to print logos using ascii or emojis
# Version: 1.0-20191021

logos = {
    "py": [[0, 0, 1, 1, 1, 1, 0, 0],
           [0, 0, 1, 3, 1, 1, 0, 0],
           [1, 1, 1, 1, 1, 1, 2, 2],
           [1, 1, 1, 1, 1, 1, 2, 2],
           [1, 1, 2, 2, 2, 2, 2, 2],
           [1, 1, 2, 2, 2, 2, 2, 2],
           [0, 0, 2, 2, 3, 2, 0, 0],
           [0, 0, 2, 2, 2, 2, 0, 0]]
}

chars = "#", "L", "@"
pylogo = logos.get("py")

for i in range(8):
    for j in range(8):
        cell_val = pylogo[i][j]
        if cell_val != 0:
            print(chars[cell_val - 1], end=" ")
        else:
            print(" ", end=" ")
    print()
