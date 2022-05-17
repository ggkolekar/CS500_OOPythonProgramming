from GradedItem import GradedItem, ProgramAssignment,Test,Exam
from Student import Student
import pickle

class Semester:
    def __init__(self, semNo:int, noOfPrograms:int, noOfTests:int, noOfExams:int):
        self.__semNo = semNo
        self.__noOfPrograms = noOfPrograms
        self.__noOfTests = noOfTests
        self.__noOfExams = noOfExams
        self.__programs = []
        self.__tests = []
        self.__students = []
        self.__exam = None

    @property
    def noOfProgAssignments(self):
        return self.__noOfPrograms

    @property
    def noOfTests(self):
        return self.__noOfTests

    @property
    def noOfExams(self):
        return self.__noOfExams

    @property
    def students(self):
        return self.__students

    def addProgram(self,progAssign:ProgramAssignment):
        if(len(self.__programs) == self.__noOfPrograms):
            print('Assignment allocation completed before, can not add any more programming assignment')
        else:
            self.__programs.append(progAssign)

    def addTest(self,test:Test):
        if(len(self.__tests) == self.__noOfTests):
            print('Tests allocation completed before, can not add any more tests')
        else:
            self.__tests.append(test)

    def addExam(self,exam:Exam):
        if(self.__exam != None):
            print('Exam allocation completed before, can not add any more exams')
        else:
            self.__exam = exam

    def addStudent(self,student:Student):
        self.__students.append(student)
        pickle.dump(self.students, open('Grades.dat', 'wb'))


    def display(self):
        print('Semester No',self.__semNo)
        print('No of assignments',self.__noOfPrograms)
        print('No of tests', self.__noOfTests)
        print('No of Exams',self.__noOfExams)

        for i in self.__programs:
            i.display()
        for j in self.__tests:
            j.display()
        self.__exam.display()


def main():
    sem = Semester(1,2,2,1)
    pa1 = ProgramAssignment(1,'ProgAssign1')
    pa2 = ProgramAssignment(2, 'ProgAssign2')

    t1 = Test(1,'Test1')
    t2 = Test(2, 'Test2')

    e1 = Exam(1,'Final Exam')

    sem.addProgram(pa1)
    sem.addProgram(pa2)

    sem.addTest(t1)
    sem.addTest(t2)

    sem.addExam(e1)

    sem.display()

#main()
