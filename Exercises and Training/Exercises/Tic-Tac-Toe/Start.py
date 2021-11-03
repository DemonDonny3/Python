# Custom utility maid by Riccardo Donadel
from Utility.Library.InputCheck import *


# Configuration for the program
config = {
    "players": ["X", "O"],      # Players's characters
    "autoPlay": True,           # Switch fro plaing with pc or other player
    "visible": True,            # Difficult mode, you can't see the game table
    "save": []                  # File path where to save the match
}


# The first method use by Main.py, is use to thek the start
def Start() -> dir:
    start = InputCheckBool("Do you want to use the standard config?\n" +
                          "Y) Yes;\n" +
                          "N) No;\n",
                          ["Y", "N"])
    if(start):
        AskStart()
        AskEnd()
        print()
    return config


# Method use for taking the initial config
def AskStart() -> dict:
    start = InputCheckList("Select if you want to use the standard character" +                      # Decides if use the standard charater for the players
                        str(config["players"])+ ", type for:\n" +
                          "Y) Yes;\n" +
                          "N) No;\n",
                          ["Y", "N"],
                          "")
    if(start == "N"):                                                                               # If the players don't want to use the standard character
        config["players"][0] = InputCheckLength(                                                     # Decides the first player character
            "Insert the caracter for the first:\n", [], 1)
        config["players"][1] = InputCheckLength(                                                     # Decides the seconf player character
            "Insert the caracter for the second:\n", [config["players"][0]], 1)
    return


def AskEnd():
    config["visible"] = InputCheckBool("Select if you want to watch the process or not, type for:\n" +
                                      "Y) Yes;\n" +
                                      "N) No;\n",
                                      ["Y", "N"])

    start = InputCheckBool("Select if you want to save the process or not, type for:\n" +
                          "Y) Yes;\n" +
                          "N) No;\n",
                          ["Y", "N"])
    if(start):
        path = InputCheckPath("Tell me the path where to save records")
        start = InputCheckFile("Tell me the file name, the file extension (.txt) will be added automatically")
        path += start[0]
        config["save"] = [path, start[1]]
    return