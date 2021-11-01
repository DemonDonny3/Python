# Custom utility maid by Riccardo Donadel
from Utility.Library.InputChek import *
import random

# Game's table
table = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

# List of free position
freePosition = [1, 2, 3, 4, 5, 6, 7, 8, 9]


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
        if(len(freePosition) % 2 == 0 and config["autoPlay"]):              # Check if the auto play is set
            position = random.choice(freePosition)
            print(position)
        else:
            position = InputChekNumberList("Select the position:\n",        # Take the next move
                                           freePosition,
                                           "This position is not free")

        column = int(position / 3 - 0.1)                                          # Write in the table the move
        row = position % 3 -1
        table[column][row] = char

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

    for i in range(3):
        result = Test(table[i][0], table[i][1], table[i][2])    # Row chek
        if result:
            return result

        result = Test(table[0][i], table[1][i], table[2][i])    # Column chek
        if result:
            return result

    result = Test(table[0][0], table[1][1], table[2][2])        # Left's diagonal
    if result:
        return result

    result = Test(table[0][2], table[1][1], table[2][0])        # Right's iagonal
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
