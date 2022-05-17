from abc import ABC, abstractmethod, abstractproperty
from typing import Tuple
class IMath(ABC):
    @abstractmethod
    def divide(self):
        pass

class Math(IMath):
    def divide(self, x: int, y: int) -> None:
        quotient = x // y;
        remainder = x % y;
        print("quotient =", quotient)
        print("remainder =", remainder)


class Math2(IMath):
    def divide(self, x: int, y: int) -> Tuple:
        quotient = x // y;
        remainder = x % y;
        return (quotient, remainder)

class MathAdapter(Math):
    def __init__(self, math:Math2):
        self.math = math


    def divide(self):
        try:
            x= int(input("Enter the first integer: "))
            y = int(input("Enter the second integer: "))

        except ValueError:
            x=y=0


        return self.math.add(x, y)

class Factory:
    def getMath(self):
        math = Math2()
        return MathAdapter(math)

def main():
    math = Factory().getMath()
    math.divide(5,2)
    #print("Sum =", math.add())

if __name__ == '__main__':
    main()

