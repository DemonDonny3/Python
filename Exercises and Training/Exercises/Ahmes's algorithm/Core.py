def Core(config:  dict) -> str:
    result = calculation(config)
    return result


def calculation(config:  dict) -> int:
    print("Numbers: ", end="")
    print(config["number"])
    if(config["number"][0] % 2 == 0):
        result = calculation({
            "number": [config["number"][0] / 2, config["number"][1] * 2],
            "visible": config["visible"],
            "save": config["save"]})
    else:
        if(config["number"][0] == 1):
            return config["number"][0] * config["number"][1]
        else:
            result = calculation({
            "number": [config["number"][0] - 1, config["number"][1]],
            "visible": config["visible"],
            "save": config["save"]})
            return result + config["number"][1]
    return result