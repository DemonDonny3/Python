from random     import random
from time       import sleep

from Animals.Dog    import Dog
from Animals.Horse  import Horse
from Animals.Lion   import Lion

from Attributes.AttributesGenerator import Generate


'''
Name:   Core
Access: public
Description:
    Method used to verify that an input is correct given a list of string of accepted values, 
    with error handling and exceptions
Parameters:
    config      dict            Program's configuration
Returns:
    result      string
'''
# Is the method where the process takes place
def Core(config:  dict) -> str:
    zoo = {
        "dogs":     Create(Dog), 
        "horses":   Create(Horse),
        "lions":    Create(Lion)
    }
    result = zoo
    return result


'''
Name:   Create
Access: public
Description:
    Method used to do the job
Parameters:
    config      dict            Program's configuration
Returns:
    result      string
'''
def Create(beast) -> str:
    animals = []
    for l in random.randrange(1, 10):
        animals.append(Generate(beast, ["nome", 10], "razza"))
    return animals
