from Start import *
from Core import *
from End import *


# Main of the body
def Main():
    End(Core(Start()))      # result = Start()
                            # win = Core(result)
                            # End(win)
    return


Main()
