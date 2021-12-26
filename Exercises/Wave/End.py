def End(result: list):
    Ending(result[0], result[1])
    return


# Method use for taking the initial config
def Ending(config: dir, wave: str):
    if(config["visible"] or config["save"]):
        if(config["orientation"] == "1"):
            for i in range(len(wave)):
                wave[i] = wave[i][::-1]
            result = WriteVertical(config, wave)
        if(config["orientation"] == "2"):
            result = WriteOrizontal(config, wave, config["level"]-1, -1)
        if(config["orientation"] == "3"):
            result = WriteVertical(config, wave)
        if(config["orientation"] == "4"):
            result = WriteOrizontal(config, wave, 0, config["level"])
    
        if(config["visible"]):
            print(result)
        if(config["save"]):
            file = open(config["save"][0], config["save"][1])
            file.write(result)
            file.close()
    
    return 

def WriteVertical(config, wave):
    result = ""
    for s in wave:
        result += s + "\n"
    return result


def WriteOrizontal(config, wave, start, end):
    result = ""
    while(start != end):
        for s in wave:
            result += s[start]
        result += "\n"
        if(start < end):
            start += 1
        else:
            start -= 1
    return result