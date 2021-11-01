from Utility.Library.InputChek import *


config = {
    "visible": True,
    "save": []
}

def Start():
    result = AskStart()
    return result


# Method use for taking the initial config
def AskStart() -> dict:

    start = InputChekList("Select if you want to watch the process or not, type for:\n" +
                          "Y) Yes;\n" +
                          "N) No;\n",
                          ["Y", "N"])
    if(start == "N"):
        config["visible"] = False

    start = InputChekList("Select if you want to save the process or not, type for:\n" +
                          "Y) Yes;\n" +
                          "N) No;\n",
                          ["Y", "N"])
    if(start == "Y"):
        path = InputCheckPath("Tell me the path where to save records")
        start = InputCheckFile("Tell me the file name, the file extension (.txt) will be added automatically")
        path += start[0]
        config["save"] = [path, start[1]]
    return config
