from Library.InputCheck import *        # Import the custom library for checking the input
from Library.AskForEnd  import *        # Import the custom library for ask how to end the program
from StartConfig        import config   # Import the start config


'''
Name:   Start
Access: public
Description:
    Method where the user choose what type of configuration to use
Parameters:
Returns:
    config      dictionary
'''
def Start() -> dir:
    start = InputCheckBool(                                                     # Asked if use the basic configuration or a custom one
        "Do you want to use the standard config?\n" + str(config) + "\n" +
        "Y) Yes;\n" +
        "N) No;\n",
        ["Y", "N"],
        "")

    if(not start):                                                              # If not using the standard configuration
        AskStart()                                                              # Data is requested for computation
        AskEnd(config)                                                          # Data is provided to save the processing
        print()                                                                 # A blank line is written to separate the input from the process
    return config


'''
Name:   AskStart
Access: public
Description:
    Method use for taking the initial config
Parameters:
Returns:
    None
'''
def AskStart() -> None:
    return
