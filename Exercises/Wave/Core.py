def Core(config:  dict) -> list:
    temp = RecursiveSolution(config["level"], config["caracter"][0])
    result = Format(temp, config["level"], config["caracter"][1])
    return config, result

# Recursive method use for eleborating the way
def RecursiveSolution(num: int, character: str) -> str:
    if num == 1:
        return character
    return RecursiveSolution(num - 1, character) + "\n" + character * num + "\n" + RecursiveSolution(num - 1, character)


# Method use for changing the way orentation from vertical to orizontal
def Format(str: str, length: int, character: str) -> str:
    i = 0
    result = str.split("\n")
    while(i != len(result)):
        while(len(result[i]) != length):
            result[i] += character
        i += 1
    return result
