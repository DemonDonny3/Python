import json
import os
import random

import names

jsonPath = os.path.dirname(os.path.realpath(__file__)) + '/Attributes.json'


'''
Name:   Generate
Access: public
Description:
    
Parameters:
    
Returns:
    
'''
def Generate(animale: str):
    with open(jsonPath) as outfile:
        data = json.load(outfile)
    result = ["mia", 10]
    match animale:
        case "Dog":
            result.append(DogsGenerator(data[animale]))
        case "Horse":
            result.append(HorsesGenerator(data[animale]))
        case "Lion":
            result.append(LionsGenerator(data[animale]))
    return result



def AnimalsGenerator():
    result = ""
    return result



def DogsGenerator(dogsRaces: list):
    races = dogsRaces["Races"]
    result = races[random.randrange(len(races))]
    return result



def HorsesGenerator(dogsCoat: list):
    coat = dogsCoat["Coat"]
    result = coat[random.randrange(len(coat))]
    return result



def LionsGenerator(dogsWeight: list):
    weight = dogsWeight["Weight"]
    result = random.randrange(weight["Min"], weight["Max"])
    return result



Generate("Lion")