from Utility.Library.InputCheck import *

config = {
    "caracter": ["-", " "],      # Character used foe deawing the wave
    "level": 3,
    "orientation": "1",
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

    start = InputCheckNumber("Input the level of the wave\n")
    config["level"] = start

    start = InputCheckList("Select if you want vertical o orizzontal orientation, type for:\n" +
                          "1) Right;\n" +
                          "2) Bottom;\n" +
                          "3) Left;\n" +
                          "4) Top;\n",
                          ["1", "2", "3", "4"],
                          "")
    config["orientation"] = start

    start = InputCheckList("Select if you want to use the standard character " + str(config["caracter"]) + ", type for:\n" +    # Decides if use the standard charater for the players
                          "Y) Yes;\n" +
                          "N) No;\n",
                          ["Y", "N"],
                          "")
    if(start == "N"):                                                                                                       # If the players don't want to use the standard character
        config["players"][0] = InputCheckLength(                                                                            # Decides the first player character
            "Insert the caracter for the wave:\n", [], 1)
        config["players"][1] = InputCheckLength(                                                                            # Decides the seconf player character
            "Insert the caracter for the background:\n", [config["caracter"][0]], 1)
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