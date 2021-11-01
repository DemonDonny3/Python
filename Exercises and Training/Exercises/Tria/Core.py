# Custom utility maid by Riccardo Donadel
from Utility.Library.InputChek import *
import random

# Game's table
table = [[["01", "02", "03"],
          ["04", "  ", "05"],
          ["06", "07", "08"]],

         [["11", "12", "13"],
          ["14", "  ", "15"],
          ["16", "17", "18"]],

         [["21", "22", "23"],
          ["24", "  ", "25"],
          ["26", "27", "28"]]
        ]

# List of free position
freePosition = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29]


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
    end = ""

    for j in table:
        print(j)

    if(config["save"]):
        file = open(config["save"][0], config["save"][1])

    while not end:
        if(len(freePosition) % 2 == 1 and config["autoPlay"]):              # Check if the auto play is set
            position = random.choice(freePosition)
            print(position)
        else:
            position = InputChekNumberList("Select the position:\n",        # Take the next move
                                           freePosition,
                                           "This position is not free")

        level = str(position)[1]
        column = str(position)[0] / 3
        row = str(position)[0] % 3
        table[int(level)][int(column)][int(row)] = char

        char = config["players"][len(freePosition) % 2]                     # Switch to the other player
        freePosition.remove(position)                                       # Remove the position occuped from the available

        result = ""
        if(config["visible"] or config["save"]):                            # If is set to write o save, it create a unique string
            for i in table:
                result += "["
                for l in i:
                    result += "[" + str(l) + "]"
                result += "]\n"

        if(config["visible"]):                                              # If is set to write on screen
            print(result)

        if(config["save"]):                                                 # If is set to write on file
            file.write(result)

        end = Check()                                                       # Chek if the game is finish

    if(config["save"]):
        file.close()

    return end


# Check() checks for every chance of winning
# Return:
# ""        = Game not finish
# " "       = Draw
# playerChar= There is a winner
def Check() -> str:
    result = ""

    for i in table:
        for l in range(3):
            result = Test(table[i][l][0], table[i][l][1], table[i][l][2])    # Row chek
            if result:
                return result

            result = Test(table[i][0][l], table[i][1][l], table[i][2][l])    # Column chek
            if result:
                return result

    for j in range(3):
        if j != 1:
            result = Test(table[0][j][1], table[1][j][1], table[2][j][1])    # Row chek
            if result:
                return result
            result = Test(table[0][1][j], table[1][1][j], table[2][1][j])    # Row chek
            if result:
                return result

    if freePosition == []:
        result = " "

    return result


# Test () actually tests the completion of three aligned points
# Params:
# item1: an element of the table to be checked
# item2: an element of the table to be checked
# item3: an element of the table to be checked
def Test(item1: str, item2: str, item3: str) -> str:
    if(item1 == item2 == item3):
        return item1
    return ""
