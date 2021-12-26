from Start import Start     # Is where the data is set to carry out the process
from Core import Core       # Is where the process takes place
from End import End         # Is where the final stages of the process are performed


# Main of the body
def Main():
    End(Core(Start()))      # result = Start()
                            # win = Core(result)
                            # End(win)
    return


Main()                      # Start of the program
