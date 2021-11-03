from Utility.Library.InputCheck import *


config = {
    "frogs": "gggg rrrr",
    "recursive": True,
    "visible": True,
    "save": []
}

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
    start = InputCheck("Select a method for input the data, type for:\n" +
                      "1) Input from console;\n" +
                      "2) Input from file;\n", ["1", "2"])
    if(start == "1"):
        frogs = InputCheck("Select the start situation, you can type only:\n" +
                          "\" \" to introduce a space;\n" +
                          "\"g\" to introduce a green frog;\n" +
                          "\"r\" to introduce a red frog;\n", [" ", "g", "r"])
    else:
        path = input("Tell me the path for the start file")
        file = open(path, "r")
        frogs = InputCheck(file.read())
    param["frogs"] = frogs

    start = InputCheck("Select whether to solve the game with a recursive method or not, type for:\n" +
                      "1) non-recursive method;\n" +
                      "2) recursive method;\n", ["1", "2"])
    param["recursive"] = start

    return 


def AskEnd():
    start = InputCheck("Select a method for input the final data, type for:\n" +
                      "1) Input from console;\n" +
                      "2) Input from file;\n", ["1", "2"])
    if(start == "1"):
        frogs = InputCheck("Select the end situation, you can type only:\n" +
                          "\" \" to introduce a space;\n" +
                          "\"g\" to introduce a green frog;\n" +
                          "\"r\" to introduce a red frog;\n", [" ", "g", "r"])
    else:
        path = input("Tell me the path for the end file")
        file = open(path, "r")
        frogs = InputCheck(file.read())
    return frogs



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