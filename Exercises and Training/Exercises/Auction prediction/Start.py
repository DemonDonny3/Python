from Utility.Library.InputChek import *


config = {
    "participants": 0,
    "iterations": 0,
    "max": 0,
    "min": 0,
    "relationship": 1,
    "visible": True,
    "save": ["result.txt", "w"]
}

def Start():
    result = AskStart()
    return result


# Method use for taking the initial config
def AskStart():

    start = InputChekNumber("Input of the number of participants:\n")
    config["participants"] = start

    start = InputChekNumber("Input of the number of iterations:\n")
    config["iterations"] = start

    start = InputChekNumber("Input the maximum for the offer:\n")
    config["max"] = start

    start = InputChekNumber("Input the minimum for the offer:\n")
    config["min"] = start

    start = InputChekNumber("Input the the relationship between average and forecast: 1 / ")
    config["relationship"] = start

    start = InputChekList("Select if you want to watch the process or not, type for:\n" +
                          "Y) Yes;\n" +
                          "N) No;\n",
                          ["Y", "N"],
                          "")
    if(start == "N"):
        config["visible"] = False

    start = InputChekList("Select if you want to save the process in a specific folder, type for:\n" +
                          "Y) Yes;\n" +
                          "N) No;\n",
                          ["Y", "N"],
                          "")
    if(start == "Y"):
        path = InputCheckPath("Tell me the path where to save records")
        start = InputCheckFile("Tell me the file name, the file extension (.txt) will be added automatically")
        path += start[0]
        config["save"] = [path, start[1]]
    return config
