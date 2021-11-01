def Core(config:  dict) -> str:
    temp = vertical_wave(config["level"], config["caracter"][0])
    left = Format(temp, config["level"], config["caracter"][1])

    if(config["orientation"] == "1"):
        i = 0
        while(i != len(left)):
            left[i] = left[i][::-1]
            i += 1
        WriteVertical(config, left, 0, config["level"]-1)
    if(config["orientation"] == "2"):
        WriteOrizontal(config, left, config["level"]-1, -1)  # ok
    if(config["orientation"] == "3"):
        WriteVertical(config, left, 0, config["level"]-1)  # ok
    if(config["orientation"] == "4"):
        WriteOrizontal(config, left, 0, config["level"])  # ok
    return

# Recursive method use for eleborating the way
def vertical_wave(num: int, character: str) -> str:
    if num == 1:
        return character
    return vertical_wave(num - 1, character) + "\n" + character * num + "\n" + vertical_wave(num - 1, character)


# Method use for changing the way orentation from vertical to orizontal
def Format(str: str, length: int, character: str) -> str:
    i = 0
    result = str.split("\n")
    while(i != len(result)):
        while(len(result[i]) != length):
            result[i] += character
        i += 1
    return result


def WriteVertical(config, wave, start, end):
    if(config["save"]):
        file = open(config["save"][0], config["save"][1])

    if(config["visible"] or config["save"]):
        if(config["visible"]):
            for s in wave:
                print(s)
        if(config["save"]):
            for s in wave:
                file.save(s + "\n")

        if "file" in locals():
            file.close()
    return


def WriteOrizontal(config, wave, start, end):
    if(config["save"]):
        file = open(config["save"][0], config["save"][1])

    if(config["visible"] or config["save"]):
        while(start != end):
            if(config["visible"]):
                for s in wave:
                    print(s[start], end='')
                print()
            if(config["save"]):
                for s in wave:
                    file.save(s)
                file.save("\n")
            if(start < end):
                start += 1
            else:
                start -= 1

        if "file" in locals():
            file.close()
    return