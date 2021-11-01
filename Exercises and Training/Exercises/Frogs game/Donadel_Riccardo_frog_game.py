# Check the input based on the list given in input
def InputChek(message, check):
    while (True):
        try:
            string = input(message).lower()
            for i in string:
                if i not in check:
                    raise
            break
        except:
            print("This is a not accetable string, you can tiper onliy:")
            for i in check:
                print(i)
            print("!")
    return string


# Method that ask how to start: where to take the start,
# if you want to see  the process or if you want to save it and where.
def AskStart():
    param = {
        "frogs": "",
        "recursive": False,
        "visible": True,
        "write": ""
    }
    start = InputChek("Select a method for input the data, type for:\n" +
                      "1) Input from console;\n" +
                      "2) Input from file;\n", ["1", "2"])
    if(start == "1"):
        frogs = InputChek("Select the start situation, you can type only:\n" +
                          "\" \" to introduce a space;\n" +
                          "\"g\" to introduce a green frog;\n" +
                          "\"r\" to introduce a red frog;\n", [" ", "g", "r"])
    else:
        path = input("Tell me the path for the start file")
        file = open(path, "r")
        frogs = InputChek(file.read())
    param["frogs"] = frogs

    start = InputChek("Select whether to solve the game with a recursive method or not, type for:\n" +
                      "1) non-recursive method;\n" +
                      "2) recursive method;\n", ["1", "2"])
    param["recursive"] = start

    start = InputChek("Select if you want to watch the process or not, type for:\n" +
                      "1) Yes;\n" +
                      "2) No;\n", ["1", "2"])
    if(start == "2"):
        param["visible"] = False

    start = InputChek("Select if you want to save the process or not, type for:\n" +
                      "1) Yes;\n" +
                      "2) No;\n", ["1", "2"])
    if(start == "1"):
        path = input("Tell me the path where to save records")
        path += input("Tell me the file 's name")
        param["write"] = start
    return param


def AskEnd():
    start = InputChek("Select a method for input the final data, type for:\n" +
                      "1) Input from console;\n" +
                      "2) Input from file;\n", ["1", "2"])
    if(start == "1"):
        frogs = InputChek("Select the end situation, you can type only:\n" +
                          "\" \" to introduce a space;\n" +
                          "\"g\" to introduce a green frog;\n" +
                          "\"r\" to introduce a red frog;\n", [" ", "g", "r"])
    else:
        path = input("Tell me the path for the end file")
        file = open(path, "r")
        frogs = InputChek(file.read())
    return frogs


def Swap(frogs, x1, x2):
    result = ""
    swap = frogs[x1]
    for char in range(len(frogs)):
        if(char != x1 and char != x2):
            result += frogs[char]
        else:
            if(char == x1):
                result += frogs[x2]
            else:
                result += frogs[x1]
    return result


def NonRecursiveMethod(frogs, visible, write, end):
    history = [frogs]

    while (frogs != end):
        print(frogs)
        space = frogs.find(" ")
        if(space == 0):
            frogs = Swap(frogs, space, 1)
        else:
            if(space == len(frogs)-1 and frogs[space - 1] == "r"):
                frogs = Swap(frogs, space, space-2)
            else:
                if(frogs[space-1] != frogs[space+1]):
                    if(space == 1 and frogs[0] == "r"):
                        frogs = Swap(frogs, space, space+2)
                    else:
                        if(space+2 != len(frogs)):
                            frogs = Swap(frogs, space, space-1)
                        else:
                            frogs = Swap(frogs, space, space+1)
                else:
                    # se sono uguali
                    if(frogs[space - 1] == "g"):
                        if(space == len(frogs)-2):
                            frogs = Swap(frogs, space, space-1)
                        else:
                            frogs = Swap(frogs, space, space+2)
                    else:
                        if(frogs[0] == "r"):
                            frogs = Swap(frogs, space, space+2)
                        else:
                            frogs = Swap(frogs, space, space-2)
        history.append(frogs)

    if(visible and write != ""):
        file = open(write, "w")
        for element in history:
            print(element)
            file.write(frogs + "\n")
    else:
        if(visible):
            for element in history:
                print(element)
        if(write != ""):
            file = open(write, "w")
            for element in history:
                file.write(frogs + "\n")

    if "file" in locals():
        file.close()
    return


def RecursiveMethod(frogs, visible, write, end):
    if (frogs != end):
        return frogs
    else:
        NonRecursiveMethod(frogs, visible, write, end)


# Main of the program
def Core():
    startConf = AskStart()
    endConf = AskEnd()
    if(startConf["recursive"] == 1):
        NonRecursiveMethod(startConf["frogs"], startConf["visible"],
                           startConf["write"], endConf)
    else:
        NonRecursiveMethod(startConf["frogs"], startConf["visible"],
                           startConf["write"], endConf)
    return


# Start
Core()
