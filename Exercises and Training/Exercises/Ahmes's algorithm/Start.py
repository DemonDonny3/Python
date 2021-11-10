from Utility.Library.InputCheck import *     # Import the custom library for checking the input

#
config = {
    "number": [5, 7],
    "visible": True,
    "save": []
}


def Start() -> dir:
    start = InputCheckBool("Do you want to use the standard config?\n" +
                          "Y) Yes;\n" +
                          "N) No;\n",
                          ["Y", "N"],
                          "")
    if(not start):
        AskStart()
        AskEnd()
        print()
    return config


# Method use for taking the initial config
def AskStart():
    start = InputCheckList("Select if you want to use the standard character" +         # Decides if use the standard charater for the players
                        str(config["number"])+ ", type for:\n" +
                          "Y) Yes;\n" +
                          "N) No;\n",
                          ["Y", "N"],
                          "")
    if(start == "N"):                                                                   # If the players don't want to use the standard character
        config["number"][0] = InputCheckNumber(                                        # Decides the first player character
            "Insert the first number:\n")
        config["number"][1] = InputCheckNumber(                                        # Decides the seconf player character
            "Insert the second number:\n")
    return


# Method use for taking the initial config
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
