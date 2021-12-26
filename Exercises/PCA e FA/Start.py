from Library.InputCheck import *     # Import the custom library for checking the input

# Base config
config = {
    "visible": True,    # Writing on the screen
    "save": []          # Path for writing to file
}


# Is the method where the user choose what type of configuration to use
def Start() -> dir:
    start = InputCheckBool(                                                     # Asked if use the basic configuration or a custom one
        "Do you want to use the standard config?\n" + str(config) + "\n" +
        "Y) Yes;\n" +
        "N) No;\n",
        ["Y", "N"],
        "")

    if(not start):                                                              # If not using the standard configuration
        AskStart()                                                              # Data is requested for computation
        AskEnd()                                                                # Data is provided to save the processing
        print()                                                                 # A blank line is written to separate the input from the process
    return config


# Method use for taking the initial config
def AskStart():
    return


# Method use for taking the initial config
def AskEnd():
    config["visible"] = InputCheckBool(                                                                             # Decides to write the process on console
        "Select if you want to watch the process or not, type for:\n" +
        "Y) Yes;\n" +
        "N) No;\n",
        ["Y", "N"],
        "")

    start = InputCheckBool(                                                                                         # Decides to write the process on file
        "Select if you want to save the process or not, type for:\n" +
        "Y) Yes;\n" +
        "N) No;\n",
        ["Y", "N"],
        "")
    if(start):
        path = InputCheckPath("Tell me the path where to save records")                                             # Decides where saving the process
        start = InputCheckFile("Tell me the file name, the file extension (.txt) will be added automatically")      # Decides the file name
        path += start[0]                                                                                            # Add the file name to the path
        config["save"] = [path, start[1]]                                                                           # Set the file's path
    return
