from abc import ABC, abstractmethod, abstractproperty
from typing import List
class Bird:
    def fly(self):
        print("A bird is flying in the sky")

class Car:
    def run(self):
        print("A car is running on the road")

class Furniture:
    def assemble(self):
        print("A Furniture is being assembled")

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class FlyCommand(Command):
    def __init__(self, bird):
        self.bird = bird

    def execute(self):
        self.bird.fly()

class RunCommand(Command):
    def __init__(self,car):
        self.car = car

    def execute(self):
        self.car.run()

class AssembleCommand(Command):
    def __init__(self, furniture):
        self.furniture = furniture

    def execute(self):
        self.furniture.assemble()


class Invoker:
    def __init__(self):
        self.commands:List[Command]=[]

    def setCommand(self, command):
        self.slot = command

    def addCommand(self, command):
        self.commands.append(command)

    def invoke(self):
        self.slot.execute()

    def executeall(self):
        for command in self.commands:
            command.execute()

def main():
    bird= Bird()
    car= Car()
    furniture=Furniture()

    invoker = Invoker()
    invoker.addCommand(FlyCommand(bird))
    invoker.addCommand(RunCommand(car))
    invoker.addCommand(AssembleCommand(furniture))


    invoker.executeall()

if __name__ == '__main__':
    main()


