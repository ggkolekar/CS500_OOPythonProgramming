from abc import ABC, abstractmethod
from typing import final,List


class DataList(ABC):

    def __init__(self):
        self.items = []

    def addItem(self, item):
        self.items.append(item)
    #This is a template method
    # A hook that has a default implementation
    def preprocess(self):
        print("No need to preprocess the data")

    # An abstract method that forces to the subclass to implement
    @abstractmethod
    def proprocess(self):
        pass

    @final
    def processList(self):
        self.preprocess()    # a hook

        for data in self.items:
            print(data)

        self.proprocess()   # abstract method



class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return self.name + "," + "{:.2f}".format(self.score)

class StudentList(DataList):
    def preprocess(self):
        for student in self.items:
            student.score *= 1.1

    def proprocess(self):
        min = None
        for student in self.items:
            if min is None or student.score < min.score:
                min =student
        print(min.name, "has the lowest score!")


class StudentList1(DataList):

    def proprocess(self):
        max = None
        for student in self.items:
            if max is None or student.score > max.score:
                max =student
        print(max.name, "has the highest score!")




def main():
    students = StudentList()
    students.addItem(Student("Peter", 90))
    students.addItem(Student("Lily", 70))
    students.addItem(Student("Jim", 80))

    students.processList()

    students1=  StudentList1()
    students1.addItem(Student("Peter", 90))
    students1.addItem(Student("Lily", 70))
    students1.addItem(Student("Jim", 80))

    students1.processList()

main()

