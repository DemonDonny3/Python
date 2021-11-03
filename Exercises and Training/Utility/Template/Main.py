from Start import Start
from Core import Core
from End import End


# Main of the body
def Main():
    End(Core(Start()))      # result = Start()
                            # win = Core(result)
                            # End(win)
    return


Main()                      # Start of the program
