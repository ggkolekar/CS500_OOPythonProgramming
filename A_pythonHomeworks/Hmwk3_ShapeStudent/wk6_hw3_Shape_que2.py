import math
from abc import ABC, abstractmethod, abstractproperty
class Shape(ABC):
    def __init__(self, name:str) -> None:
        self._name = name

    @abstractmethod
    def surfaceArea(self) -> float:
        pass

    def display(self):
        print('name:', self._name)

class Shape2D(Shape):
    def __init__(self, name: str) -> None:
        super().__init__(name)

class Shape3D(Shape):
    def __init__(self, name: str) -> None:
        super().__init__(name)

class Square(Shape2D):
    def __init__(self, len: int) -> int:
        super().__init__("Square")
        self.__len = len

    def surfaceArea(self) -> None:
        #A=len^2
        return self.__len * self.__len


    def display(self):
        super().display()
        print('length: ' + str(self.__len))

class Circle(Shape2D):
    def __init__(self, radius: float) -> None:
        super().__init__("Circle")
        self.__radius= radius


    def surfaceArea(self) -> None:
        #A=pi*r^2
        return math.pi * self.__radius * self.__radius

    def display(self):
        super().display()
        print('radius: ' + str(self.__radius))


class Rectangle(Shape2D):
    def __init__(self, len: int, width: int) -> None:
        super().__init__("Rectangle")
        self.__len = len
        self.__width = width

    def surfaceArea(self) -> None:
        #A=lw
        return self.__len * self.__width


    def display(self):
        super().display()
        print('length: ' + str(self.__len))
        print('width: ' + str(self.__width))

class Cylinder(Shape3D):
    def __init__(self, radius: int, height: int) -> None:
        super().__init__("Cylinder")
        self.__radius= radius
        self.__height =height

    def surfaceArea(self) -> None:
        # A=2pi*rh+ 2pi*r^2
        return 2 * math.pi * self.__radius * (self.__height + self.__radius)

    def display(self):
        super().display()
        print('radius: '+ str(self.__radius))
        print('height: ' + str(self.__height))

class Pyramid(Shape3D):
    def __init__(self, len: int, width: int, height: int) -> None:
        super().__init__("Pyramid")
        self.__len = len
        self.__width = width
        self.__height = height

    def surfaceArea(self) -> None:
        #A=1/2*lw+lw
        surfaceArea = 1/2 * self.__len * self.__width + self.__len * self.__width
        return surfaceArea

    def display(self):
        super().display()
        print('length: ' + str(self.__len))
        print('width: ' + str(self.__width))
        print('height: ' + str(self.__height))

def main():
    square = Square(4)
    square.display()
    print("Square surface area: ", square.surfaceArea())

    circle = Circle(4)
    circle.display()
    print("Circle surface area: " , circle.surfaceArea())

    rectangle = Rectangle(2, 4)
    rectangle.display()
    print("Rectangle surface area: " , rectangle.surfaceArea())

    cylinder = Cylinder(2,4)
    cylinder.display()
    print("Cylinder surface area: " , cylinder.surfaceArea())

    pyramid = Pyramid(2,4,6)
    pyramid.display()
    print("Pyramid surface area: " , pyramid.surfaceArea())

main()








