from Library.InputCheck import *    # Import the custom library for checking the input

from Start import Start                     # Is where the data is set to carry out the process
from Core import Core                       # Is where the process takes place
from End import End                         # Is where the final stages of the process are performed


# Main of the body
def Main():
    iterations = InputCheckNumberAndString(                         # Are asked how many times to run the code
        "How many times do I have to run the program:\n" +
        "1) Write a number N and the program will be executed N times;\n" +
        "2) type E to run the code in endless mode (Will be asked to terminate at the end of all iterations);\n",
        ["e"],
        "This is neither a number nor an accepted character"
        )

    run = bool(iterations)                                          # Verify that the input is different from 0 otherwise it does not even execute the cosice
    cycles = iterations                                             # Save the number of iterations in loops
    while(run):
        End(Core(Start()))                                          # Start() => Core(result) => End(result)

        if(iterations < 0):                                         # If the number is negative, the program is in endless mode
            run = InputCheckBool(                                   # At the end of each iteration, Aare asked whether to terminate the program
                "Do you want to continue?\n" +
                "Y) Yes;\n" +
                "N) No;\n",
                ["Y", "N"],
                "")
        else:                                                       # If the number is positive, the program has a limited number of cycles
            cycles -= 1                                             # With each interaction the number of cycles to be carried out decreases
            end = bool(cycles)                                      # Check that if the value is zero I end the cycle
    return


Main()          # Start of the program
