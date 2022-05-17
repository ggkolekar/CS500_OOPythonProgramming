from Student import Student
from StudentScore import StudentScore
from GradeBook1 import Gradebook
from Policy import Policy
#from db import StudentRepository
from Semester import Semester, ProgramAssignment, Test,Exam
import os,sys
from typing import List


class GradeBookApp:
    #def __init__(self):
        #self.__studentdb = StudentRepository()
        #self.__student = self.__studentdb.getstudents()
        #self.__order = Order()



    def showTitle(self):
        print("The business program")
        print()

    def showMenu(self):
        print("COMMAND MENU")
        print(" \n S : Set up for new semester \n A  : Add student to the student repository \n P  : Record programming",
              " assignment score  \n T  : Record test score for all students \n F  : Record final exam score for all ",
              "students \n C : change grade for perticular student \n G :  calculate final score \n O : output the ",
              "grade data, ordered alphabetically by name \n Q : Quit program")
        print()


def main():
    gba = GradeBookApp()
    gba.showMenu()
    gb = None
    while True:
        opt = input("\n Enter Menu Option below: ")
        if opt == "Q":
            print("\n You choosen to quit")
            exit()

        if opt == "S":
            #sem= Semester()
            numOfProgAssigs = int(input("Enter numberOfProgrammingAssignments= "))
            progAssignments = {}
            itemNum = 0
            iteName = None
            for i in range(numOfProgAssigs):
                itemNum = int(input(" ID of Program Assignment: "))
                itemName = input("Please enter Name of Program Assignment: ")
                progAssignments[itemNum] = itemName

            tests = {}
            numberoftests = int(input("Enter numberoftests= "))
            for i in range(numberoftests):
                itemNum = input("ID of test: ")
                itemName = input("Please enter Name of test: ")
                tests[itemNum] = itemName

            exams = {}
            numberOffinalexams = int(input("Enter number Of final exams "))
            for i in range(numberOffinalexams):
                itemNum = input(" ID of final exam: ")
                itemName = input("Please enter Name of exam: ")
                exams[itemNum] = itemName

            sem = Semester(1, numOfProgAssigs,numberoftests,numberOffinalexams)

            for k,v in progAssignments.items():
                pa = ProgramAssignment(k,v)
                sem.addProgram(pa)

            for k,v in tests.items():
                t = Test(k,v)
                sem.addTest(t)

            for k,v in exams.items():
                e = Exam(k,v)
                sem.addProgram(e)

            gb = Gradebook(sem,2021)

        elif opt == "A":
            studentID = input("Enter StudentID: ")
            fname = input("Enter firstname: ")
            lname = input("Enter lastname: ")

            s = Student(studentID, fname, lname)
            sem.addStudent(s)

        elif opt == "P":
            an = int(input("Enter assignment number: "))
            sd = int(input('Enter student Id: '))
            sn = input('Enter student name: ')
            s = input('Enter score: ')
            gb.addStudentScore(sd,an,ProgramAssignment.__name__,s)

        elif opt == "T":
            tn = int(input("Enter test number: "))
            sd = int(input('Enter student Id: '))
            sn = input('Enter student name: ')
            s = input('Enter score: ')
            gb.addStudentScore(sd, tn, Test.__name__,s)

        elif opt == "F":
            e = int(input("Enter Exam number: "))
            sd = int(input('Enter student Id: '))
            sn = input('Enter student name: ')
            s = input('Enter score: ')
            gb.addStudentScore(sd, e, Exam.__name__,s)

        elif opt == "C":
            sid = int(input('Enter student id: '))
            ts = input('Type of score to change P, T or F: ')
            if ts == 'P':
                ps = int(input('Enter program assignment number: '))
                s = int(input('Enter new score: '))
                result = gb.changeStudentScore(sid,s,ProgramAssignment.__name__,ps)
                if result == True:
                    print('Score updated successfully for student id ', sid, ' for programming assignment with number ', ps)
                else:
                    print('Something went wrong. Please try again later: ')
            elif ts == 'T':
                ps = int(input('Enter test number: '))
                s = int(input('Enter new score: '))
                result = gb.changeStudentScore(sid, s, Test.__name__, ps)
                if result == True:
                    print('Score updated successfully for student id ', sid, ' for test with number ', ps)
                else:
                    print('Something went wrong. Please try again later')
            elif ts == 'F':
                ps = int(input('Enter final exam number: '))
                s = int(input('Enter new score: '))
                result = gb.changeStudentScore(sid, s, Exam.__name__, ps)
                if result == True:
                    print('Score updated successfully for student id ',sid,' for exam with number ',ps)
                else:
                    print('Something went wrong. Please try again later')
            else:
                print('Invalid input')


        elif opt == "L":
            p = Policy()
            pw = float(input('Enter Programming Assignment Weightage e.g. 0.5 for 50% : '))
            tw = float(input('Enter Test Weightage e.g. 0.25 for 25% : '))
            ew = float(input('Enter Exam Weightage e.g. 0.25 for 25% : '))
            p.addGradedItemWeightage(ProgramAssignment.__name__, pw)
            p.addGradedItemWeightage(Test.__name__, tw)
            p.addGradedItemWeightage(Exam.__name__, ew)
            gb.setPolicy(p)

        elif opt == "G":
            res = gb.calculateFinalScores()
            if res == True:
                print('Grades updated successfully')
            else:
                print('Something went wrong. Please try again later.')

        elif opt == "O":
            gb.display()
        else:
            print("\n You Choosen Option: ",opt)
            print()

main()