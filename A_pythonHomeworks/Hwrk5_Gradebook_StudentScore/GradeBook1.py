from Semester import Semester
from Policy import Policy
from StudentScore import StudentScore
from Student import Student
from GradedItem import GradedItem, ProgramAssignment,Test,Exam
from typing import List,Dict
import pickle
import json

class Gradebook:

    def __init__(self,semester:Semester,year:int):
        self.__semester=semester
        self.__year=year
        #self.__gradedItemScores = []
        self.__studentScores:List[StudentScore]
        self.__studentScores = []
        self.__finalScores = {}
        self.__policy = None

    def setPolicy(self,policy:Policy):
        self.__policy = policy
        pickle.dump(policy,open('policy.dat','wb'))


    def changeStudentScore(self,studId:int, score:int, gradedItemType:str, gradedItemNum:int) -> bool:
        for itemScore in self.__studentScores:
            if itemScore.itemno == gradedItemNum and isinstance(itemScore.gradedItem,gradedItemType):
                #for k,v in itemScore.studentScores.items():
                    #if(k == studId):
                itemScore.score(score)
                return True

        return False

    def addStudentScore(self,studId:int, gradedItemNum:int, gradedItemType:str, score):
        ss = StudentScore(studId,gradedItemNum,gradedItemType,score)
        self.__studentScores.append(ss)

    def calculateFinalScores(self):
        result = False
        for stud in self.__semester.students:
            self.__finalScores[stud.studId] = self.calculateFinalScore(stud.studId, self.__policy)
        result = True
        #pickle.dump(self.__finalScores, open('grades.out', 'wb'))
        return result


    def calculateFinalScore(self, studId:int, policy:Policy):
        finalscore=0
        progAssignScore = 0
        testScore = 0
        examScore = 0

        progAssignScoreWt = policy.getGradedItemWeightage(ProgramAssignment.__name__)
        testScoreWt = policy.getGradedItemWeightage(Test.__name__)
        examScoreWt = policy.getGradedItemWeightage(Exam.__name__)

        studScores = []
        for studScore in self.__studentScores:
            if(studScore.studId == studId):
                studScores.append(studScore)

        for studScore in studScores:
            if(studScore.gradedItemType == ProgramAssignment.__name__):
                progAssignScore += studScore.score

            if (studScore.gradedItemType == Test.__name__):
                testScore += studScore.score

            if (studScore.gradedItemType == Exam.__name__):
                examScore += studScore.score

        print(progAssignScoreWt,' ',testScoreWt,' ',examScoreWt)

        finalscore = float(progAssignScore)/self.__semester.noOfProgAssignments * progAssignScoreWt + (float(testScore) / self.__semester.noOfTests * testScoreWt)+(float(examScore) / self.__semester.noOfExams * examScoreWt)

        return finalscore

    def display(self):
        for i in self.__studentScores:
            print('Student Id ',i.studId,' Graded Item Num ',i.gradedItemNum,' Graded Item Type ',i.gradedItemType,' Score ',i.score)
        for k,v in self.__finalScores.items():
            print('Student Id',k, ' Final Score ', v)

    def toJson(self):
        json.dumps(self.__studentScores,default = lambda o: o.__dict__,sort_keys = True, indent = 4)


def main():
    sem = Semester(1, 2, 2, 1)
    pa1 = ProgramAssignment(1, 'ProgAssign1')
    pa2 = ProgramAssignment(2, 'ProgAssign2')

    t1 = Test(1, 'Test1')
    t2 = Test(2, 'Test2')

    e1 = Exam(1, 'Final Exam')

    sem.addProgram(pa1)
    sem.addProgram(pa2)

    sem.addTest(t1)
    sem.addTest(t2)

    sem.addExam(e1)

    #sem.display()

    s1 = Student('John','Doe',1)
    s2 = Student('Jane','Doe',2)
    s3 = Student('Michael','Berry',3)
    s4 = Student('Tony','Chang',4)
    s5 = Student('Mia','Su',5)

    sem.addStudent(s1)
    sem.addStudent(s2)
    sem.addStudent(s3)
    sem.addStudent(s4)
    sem.addStudent(s5)

    #sem.display()

    gb = Gradebook(sem,2021)
    gb.addStudentScore(s1.studId,pa1.itemno,ProgramAssignment.__name__,80)
    gb.addStudentScore(s1.studId, pa2.itemno, ProgramAssignment.__name__, 82)

    gb.addStudentScore(s2.studId, pa1.itemno, ProgramAssignment.__name__, 83)
    gb.addStudentScore(s2.studId, pa2.itemno, ProgramAssignment.__name__, 84)

    gb.addStudentScore(s3.studId, pa1.itemno, ProgramAssignment.__name__, 85)
    gb.addStudentScore(s3.studId, pa2.itemno, ProgramAssignment.__name__, 86)

    gb.addStudentScore(s4.studId, pa1.itemno, ProgramAssignment.__name__, 87)
    gb.addStudentScore(s4.studId, pa2.itemno, ProgramAssignment.__name__, 88)

    gb.addStudentScore(s5.studId, pa1.itemno, ProgramAssignment.__name__, 89)
    gb.addStudentScore(s5.studId, pa2.itemno, ProgramAssignment.__name__, 90)

    #Test scores
    gb.addStudentScore(s1.studId, t1.itemno, Test.__name__, 80)
    gb.addStudentScore(s1.studId, t2.itemno, Test.__name__, 82)

    gb.addStudentScore(s2.studId, t1.itemno, Test.__name__, 83)
    gb.addStudentScore(s2.studId, t2.itemno, Test.__name__, 84)

    gb.addStudentScore(s3.studId, t1.itemno, Test.__name__, 85)
    gb.addStudentScore(s3.studId, t2.itemno, Test.__name__, 86)

    gb.addStudentScore(s4.studId, t1.itemno, Test.__name__, 87)
    gb.addStudentScore(s4.studId, t2.itemno, Test.__name__, 88)

    gb.addStudentScore(s5.studId, t1.itemno, Test.__name__, 89)
    gb.addStudentScore(s5.studId, t2.itemno, Test.__name__, 90)

    #exam score
    gb.addStudentScore(s1.studId, e1.itemno, Exam.__name__, 80)

    gb.addStudentScore(s2.studId, e1.itemno, Exam.__name__, 83)

    gb.addStudentScore(s3.studId, e1.itemno, Exam.__name__, 85)

    gb.addStudentScore(s4.studId, e1.itemno, Exam.__name__, 87)

    gb.addStudentScore(s5.studId, e1.itemno, Exam.__name__, 89)

    p = Policy()
    p.addGradedItemWeightage(ProgramAssignment.__name__, 0.5)
    p.addGradedItemWeightage(Test.__name__, 0.25)
    p.addGradedItemWeightage(Exam.__name__, 0.25)

    gb.setPolicy(p)

    #p.display()

    #print(gb.calculateFinalScore(s1.studId,p))
    gb.calculateFinalScores()

    gb.display()
    #gb.toJson()

main()