from Animals import Animal


#
class Dog(Animal):
    def __init__(self, race):
        self.race = race

    #
    def info(self):
        return self.race

    #
    def speak(self):
        return "barks"

    #
    def move(self):
        return "runs"

    #
    def eat(self):
        return "eats"

    #
    def drink(self):
        return "drinks"

    #
    def getNRace(self) -> str:
        return self.race

    #
    def setRace(self, newRace: str):
        self.race = newRace
