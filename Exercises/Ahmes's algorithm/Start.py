from Library.InputCheck import *     # Import the custom library for checking the input

# Base config
config = {
    "number": [5, 7],   # The stock numbers
    "visible": True,    # Writing on the screen
    "save": []          # Path for writing to file
}


# Is the method where the user choose what type of configuration to use
def Start() -> dir:
    start = InputCheckBool("Do you want to use the standard config?\n" +            # Decides if use the standard configuration
                          "Y) Yes;\n" +
                          "N) No;\n",
                          ["Y", "N"],
                          "")
    if(not start):
        AskStart()
        AskEnd()
        print()
    return config


# Is the method used to set the start configuration
def AskStart():
    start = InputCheckBool("Select if you want to use the standard number " +       # Decides if use the standard numbers
                        str(config["number"])+ ", type for:\n" +
                          "Y) Yes;\n" +
                          "N) No;\n",
                          ["Y", "N"],
                          "")
    if(not start):                                                                  # If the user don't want to use the standard numbers
        config["number"][0] = InputCheckNumber(                                     # Decides the first player number
            "Insert the first number:\n")
        config["number"][1] = InputCheckNumber(                                     # Decides the seconf player number
            "Insert the second number:\n")
    return


# Is the method used to set the end configuration
def AskEnd():
    config["visible"] = InputCheckBool("Select if you want to watch the process or not, type for:\n" +              # Decides if watching the process
                                      "Y) Yes;\n" +
                                      "N) No;\n",
                                      ["Y", "N"],
                                      "")

    start = InputCheckBool("Select if you want to save the process or not, type for:\n" +                           # Decides if saving the process
                          "Y) Yes;\n" +
                          "N) No;\n",
                          ["Y", "N"],
                          "")
    if(start):
        path = InputCheckPath("Tell me the path where to save records")                                             # Decides where saving the process
        start = InputCheckFile("Tell me the file name, the file extension (.txt) will be added automatically")      # Decides the file name
        path += start[0]
        config["save"] = [path, start[1]]                                                                           # Set the file's path
    return
