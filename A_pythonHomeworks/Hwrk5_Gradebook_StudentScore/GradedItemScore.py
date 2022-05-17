from GradedItem import GradedItem,ProgramAssignment,Test,Exam

class GradedItemScore:
    def __init__(self, gradedItem:GradedItem):
        self.__gradedItem = gradedItem
        self.__studGrades = {}

    def display(self):
        self.__gradedItem.display()
        for key,val in self.__studGrades.items():
            print('Student Id ',key,' Score ',val)

    def addStudentScore(self,studId:int, score:int):
        self.__studGrades[studId] = score

    @property
    def gradedItem(self):
        return self.__gradedItem

    @property
    def studentScores(self):
        return self.__studGrades

def main():
    gi = ProgramAssignment(1,'Assignment 1')
    gig = GradedItemScore(gi)
    gig.addStudentScore(10,90)
    gig.addStudentScore(11,92)

    gig.display()

main()