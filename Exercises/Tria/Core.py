# Custom utility maid by Riccardo Donadel
from Utility.Library.InputChek import *
import random

# Game's table
table = [[["001", "002", "003"],
          ["004", "000", "006"],
          ["007", "008", "009"]],

         [["011", "012", "013"],
          ["014", "000", "016"],
          ["017", "018", "019"]],

         [["021", "022", "023"],
          ["024", "000", "026"],
          ["027", "028", "029"]]
         ]

# List of free position
freePosition = [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29]


# The method that contain the logic of the solution
# Params:
# config: Configuration maid by Start.py
def Core(config:  dict) -> str:
    result = Game(config)
    return result


# Params:
# config: Configuration maid by Start.py
def Game(config:  dict) -> str:
    char = config["players"][0]
    end = " "

    print(Record(config["level"]))

    if(config["save"]):
        file = open(config["save"][0], config["save"][1])

    while (freePosition != [] and end == " "):
        if(len(freePosition) % 2 == 1 and config["autoPlay"]):              # Check if the auto play is set
            position = random.choice(freePosition)
            print(position)
        else:
            position = InputChekNumberList("Select the position:\n",        # Take the next move
                                           freePosition,
                                           "This position is not free")

        level = position / 10 - 0.5
        row = (position % 10 -1) / 3
        cell = (position % 10 - 1) % 3
        table[round(level)][int(row)][int(cell)] = char

        char = config["players"][int((len(freePosition) +1) % 2)]                 # Switch to the other player
        freePosition.remove(position)                                       # Remove the position occuped from the available

        result = ""
        if (config["visible"] or config["save"]):                            # If is set to write o save, it create a unique string
            result = Record(config["level"])

        if(config["visible"]):                                              # If is set to write on screen
            print(result)

        if(config["save"]):                                                 # If is set to write on file
            file.write(result)

        end = Check()                                                       # Chek if the game is finish

    if(config["save"]):
        file.close()

    return end

def Record(level:  int) -> str:
    result = ""
    for j in range(level):
        result += "\t" * j
        result += table[j][0][0]
        result += "\t" * (level - j)
        result += table[j][0][1]
        result += "\t" * (level - j)
        result += table[j][0][2]
        result += "\n"

    for l in range(3):
        result += table[l][1][0] + "\t"
    result += "\t"
    for l in range(3):
        result += table[l][1][2] + "\t"
    result += "\n"

    j = level -1
    while (j >= 0):
        result += "\t" * j
        result += table[j][2][0]
        result += "\t" * (level - j)
        result += table[j][2][1]
        result += "\t" * (level - j)
        result += table[j][2][2]
        result += "\n"
        j -= 1

    result += "\n"
    return result


# Check() checks for every chance of winning
# Return:
# ""        = Game not finish
# playerChar= There is a winner
def Check() -> str:
    for i in range(len(table) - 1):
        for l in range(3):
            result = Test(table[i][l][0], table[i][l][1], table[i][l][2])    # Row chek
            if result:
                return result

            result = Test(table[i][0][l], table[i][1][l], table[i][2][l])    # Column chek
            if result:
                return result
            l += 1

    for j in range(3):
        if j != 1:
            result = Test(table[0][j][1], table[1][j][1], table[2][j][1])    # Row chek
            if result:
                return result
            result = Test(table[0][1][j], table[1][1][j], table[2][1][j])    # Row chek
            if result:
                return result

    return " "


# Test () actually tests the completion of three aligned points
# Params:
# item1: an element of the table to be checked
# item2: an element of the table to be checked
# item3: an element of the table to be checked
def Test(item1: str, item2: str, item3: str) -> str:
    if(item1 == item2 == item3):
        return item1
    return ""
