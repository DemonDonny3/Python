from Animals import Animal


#
class Horse(Animal):
    def __init__(self, coat):
        self.coat = coat

    #
    def info(self):
        return self.coat

    #
    def speak(self):
        return "neighs"

    #
    def move(self):
        return "gallops"

    #
    def eat(self):
        return "eats"

    #
    def drink(self):
        return "drinks"
        
    #
    def getCoat(self) -> str:
        return self.coat

    #
    def setCoat(self, newCoat: str):
        self.coat = newCoat
