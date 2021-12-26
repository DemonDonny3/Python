from Animals import Animal


#
class Lion(Animal):
    def __init__(self, weight):
        self.weight = weight

    #
    def info(self):
        return self.weight

    #
    def speak(self):
        return "roars"

    #
    def move(self):
        return "it goes like lightning"

    #
    def eat(self):
        return "devours"

    #
    def drink(self):
        return "swallows"

    #
    def getweight(self) -> str:
        return self.weight

    #
    def setweight(self, newWeight: str):
        self.weight = newWeight
