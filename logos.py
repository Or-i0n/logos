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
           [0, 0, 2, 2, 2, 2, 0, 0]],

    "js": [[0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 2, 2],
           [1, 1, 1, 1, 1, 1, 2, 2],
           [1, 1, 2, 2, 2, 2, 2, 2],
           [1, 1, 2, 2, 2, 2, 2, 2],
           [0, 0, 2, 2, 3, 2, 0, 0],
           [0, 0, 2, 2, 2, 2, 0, 0]],

    "chars": {
                "py": ["#", "L", "@"]

    }
}


def print_logo(lang_name):
    """Prints logos of programming languages."""
    chars = logos.get("chars").get(lang_name)
    logo = logos.get(lang_name)

    for i in range(8):
        for j in range(8):
            cell_val = logo[i][j]
            if cell_val != 0:
                print(chars[cell_val - 1], end=" ")
            else:
                print(" ", end=" ")
        print()


print_logo("py")
