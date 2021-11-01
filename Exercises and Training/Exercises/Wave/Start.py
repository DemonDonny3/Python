from Utility.Library.InputChek import *

config = {
    "caracter": ["-", " "],      # Character used foe deawing the wave
    "level": 0,
    "orientation": "",
    "visible": True,
    "save": []
}

def Start():
    result = AskStart()
    return result


# Method use for taking the initial config
def AskStart():

    start = InputChekNumber("Input the level of the wave\n")
    config["level"] = start

    start = InputChekList("Select if you want vertical o orizzontal orientation, type for:\n" +
                          "1) Right;\n" +
                          "2) Bottom;\n" +
                          "3) Left;\n" +
                          "4) Top;\n",
                          ["1", "2", "3", "4"],
                          "")
    config["orientation"] = start

    start = InputChekList("Select if you want to use the standard character " + str(config["caracter"]) + ", type for:\n" +      # Decides if use the standard charater for the players
                          "Y) Yes;\n" +
                          "N) No;\n",
                          ["Y", "N"],
                          "")
    if(start == "N"):                                                                                                       # If the players don't want to use the standard character
        config["players"][0] = InputChekLength(                                                                             # Decides the first player character
            "Insert the caracter for the wave:\n", [], 1)
        config["players"][1] = InputChekLength(                                                                             # Decides the seconf player character
            "Insert the caracter for the background:\n", [config["caracter"][0]], 1)

    start = InputChekList("Select if you want to watch the process or not, type for:\n" +
                          "Y) Yes;\n" +
                          "N) No;\n",
                          ["Y", "N"],
                          "")
    if(start == "N"):
        config["visible"] = False

    start = InputChekList("Select if you want to save the process or not, type for:\n" +
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
