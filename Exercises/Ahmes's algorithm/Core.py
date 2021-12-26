# Is the method where the process takes place
def Core(config:  dict) -> str:
    result = calculation(config, ["Start:\t\t\t" + str(config["number"][0]) + " * " + str(config["number"][1])])
    return config, result


# Is the method that executes Ahmes's algorithm
def calculation(config:  dict, result: list[str]) -> list[str]:
    if(config["number"][0] % 2 == 0):                                                           # If the first number is even
        if(config["visible"] or config["save"]):                                                # If it is set to write to screen or save the process
            result.append("a / 2 * 2 * b:\t\t" + str(config["number"][0]) + " / 2 * 2 " + str(config["number"][1]))
        return calculation({                                                                    # The calculation is transformed into: a / 2 * 2 * b
            "number": [int(config["number"][0] / 2), config["number"][1] * 2],
            "visible": config["visible"],
            "save": config["save"]},
            result)
    else:                                                                                                                                   # If the first number is odd
        if(config["number"][0] == 1):                                                                                                       # If the first number is 1
            if(config["visible"] or config["save"]):                                                                                        # If it is set to write to screen or save the process
                result.append(str(config["number"][0]) + " / 2 * 2 " + str(config["number"][1]))
            return config["number"][0] * config["number"][1], result                                                                        # It is returned a * b
        else:                                                                                                                               # If the first number is not 1
            if(config["visible"] or config["save"]):                                                                                        # If it is set to write to screen or save the process
                result.append("(a - 1) * b + b:\t(" + str(config["number"][0]) + " - 1) * " + str(config["number"][1]) + " + " + str(config["number"][1]))
            num = calculation({                                                                                                            # The calculation is transformed into: (a - 1) * b + b
            "number": [config["number"][0] - 1, config["number"][1]],
            "visible": config["visible"],
            "save": config["save"]}, result)
            return num[0] + config["number"][1], result                                                                                    # End the calculation for this case
    return 