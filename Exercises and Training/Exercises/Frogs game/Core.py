def Core(config:  dict) -> str:
    if(config["recursive"] == 1):
        NonRecursiveMethod(config)
    else:
        NonRecursiveMethod(config)
    return

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