

# Final method use by Main.py, it use to write the result
def End(winner: str):
    AskEnd(winner)
    return


# Method use for writening the result
def AskEnd(winner: str):

    if(winner != " "):
        print("The winner is " + winner)    # Print the winner
    else:
        print("there is no winner!")        # Print the draw
    return
