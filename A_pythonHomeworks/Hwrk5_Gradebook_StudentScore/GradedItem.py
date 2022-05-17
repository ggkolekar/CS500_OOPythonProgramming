from abc import ABC, abstractproperty, abstractmethod

class GradedItem(ABC):
    def __init__(self,itemno:int,itemname:str):
        self.__itemno = itemno
        self.__itemname = itemname

    @property
    def itemno(self):
        return self.__itemno

    @property
    def itemname(self):
        return self.__itemname

    @abstractmethod
    def display(self):
        pass

class ProgramAssignment(GradedItem):
    def __init__(self,progAssigNo:int, progAssigName:str):
        GradedItem.__init__(self,progAssigNo,progAssigName)

    def display(self):
        print("Assignment Number: ", self.itemno)
        print("Assignment Name: ",self.itemname)

class Test(GradedItem):
    def __init__(self,testNo:int, testName:str):
        GradedItem.__init__(self,testNo,testName)

    def display(self):
        print("Test Number: ", self.itemno)
        print("Test Name: ",self.itemname)

class Exam(GradedItem):
    def __init__(self,examNo:int, examName:str):
        GradedItem.__init__(self,examNo,examName)

    def display(self):
        print("Exam Number: ", self.itemno)
        print("Exam Name: ",self.itemname)
        #print('class name',ProgramAssignment.__name__)

def main():
    gi = ProgramAssignment(1,'Programming Assignment1')
    t1 = Test(2, 'Test1')
    e1 = Exam(3, 'Exam1')

    gi.display()
    t1.display()
    e1.display()

#main()