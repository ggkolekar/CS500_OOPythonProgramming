import GradedItem

class Student:
    def __init__(self, fName:str,lName:str,stuID:int):
        self.__fName = fName
        self.__lName = lName
        self.__stuID = stuID

    def display(self):
        print('fName =', self.__fName)
        print('fName =', self.__lName)
        print('stuID =', self.__stuID)

    @property
    def studId(self):
        return self.__stuID

    @property
    def fName(self):
        return self.__fName

    @property
    def lName(self):
        return self.__lName

def main():
    s = Student('John','Doe',100)
    s.display()

#main()