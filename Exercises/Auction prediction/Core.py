import random


def Core(config: dict) -> str:
    Auction(config)
    return


def Auction(config: dict) -> str:
    prediction = [config["max"] / config["relationship"]]
    file = open(config["save"][0], config["save"][1])
    averageList = {}

    for i in range(config["iterations"]):
        result = 0
        iteration = []
        average = 0

        for l in range(config["participants"]):
            result = random.randrange(config["min"], config["max"])
            iteration.append(result)
            average += result
            l += 1

        average = round(average / config["participants"])
        result += average
        winner = Winner(iteration)  
        
        prediction.append(int((prediction[len(prediction) - 1] + average / config["relationship"]) / 2))

        try:
            averageList[average] += 1
        except:
            averageList[average] = 1

        file.write(str(average)  + "\t" +
                   winner + "\t" + 
                   str(iteration) + "\n\n")
        i += 1

    if config["visible"]:
        print(prediction)
        print(averageList)
    file.close()

    file = open(config["save"][0], "r")
    return


def Winner(result: list) -> str:
    result.sort()
    result.reverse()
    for j in result:
        if(result.count(j) == 1):
            return str(j)
    return "No winner"