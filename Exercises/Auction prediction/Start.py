from Utility.Library.InputCheck import *


config = {
    "participants": 20,
    "iterations": 100,
    "max": 1000,
    "min": 0,
    "relationship": 3,
    "visible": True,
    "save": ["result.txt", "w"]
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
def AskStart():

    start = InputCheckNumber("Input of the number of participants:\n")
    config["participants"] = start

    start = InputCheckNumber("Input of the number of iterations:\n")
    config["iterations"] = start

    start = InputCheckNumber("Input the maximum for the offer:\n")
    config["max"] = start

    start = InputCheckNumber("Input the minimum for the offer:\n")
    config["min"] = start

    start = InputCheckNumber("Input the the relationship between average and forecast: 1 / ")
    config["relationship"] = start
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