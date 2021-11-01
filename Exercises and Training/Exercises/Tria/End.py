# Final method use by Main.py, it use to write the result
def End(winner: str):
    Ending(winner)
    return


# Method use for writening the result
def Ending(winner: str):

    if(winner != " "):
        print("The winner is " + winner)    # Print the winner
    else:
        print("there is no winner!")        # Print the draw
    return
