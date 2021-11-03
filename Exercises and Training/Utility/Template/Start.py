from Utility.Library.InputCheck import *     # Import the custom library for checking the input

#
config = {
    "visible": True,
    "save": []
}


def Start() -> dir:
    start = InputCheckBool("Do you want to use the standard config?\n" +
                          "Y) Yes;\n" +
                          "N) No;\n",
                          ["Y", "N"],
                          "")
    if(start):
        AskStart()
        AskEnd()
        print()
    return config


# Method use for taking the initial config
def AskStart():
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
