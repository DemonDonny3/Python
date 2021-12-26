from abc import abstractmethod
 
#
class Animal():
    @abstractmethod
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #
    def info(self):
        pass

    #
    def speak(self):
        pass

    #
    def move(self):
        pass

    #
    def eat(self):
        pass

    #
    def drink(self):
        pass

    #
    def sleep(self):
        pass

    #
    def getName(self) -> str:
        return self.name

    #
    def setName(self, newName: str):
        self.name = newName

    #
    def getAge(self) -> int:
        return self.age

    #
    def setAge(self, newAge: int):
        self.age = newAge
