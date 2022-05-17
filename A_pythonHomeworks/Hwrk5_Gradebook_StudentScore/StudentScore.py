
class StudentScore:

    def __init__(self,studId:int, gradedItemNum:int, gradedItemType:str, score:int):
        self.__studId = studId
        self.__gradedItemNum = gradedItemNum
        self.__gradedItemType = gradedItemType
        self.__score = score

    @property
    def studId(self):
        return self.__studId

    @property
    def gradedItemNum(self):
        return self.__gradedItemNum

    @property
    def score(self):
        return self.__score

    @property
    def gradedItemType(self):
        return self.__gradedItemType

    @score.setter
    def score(self, score):
        self.__score=score

    def display(self):
        print('Student Id:',self.__studId,' Graded Item Number:',self.__gradedItemNum, ' Score:',self.__score)

def main():
    ss1 = StudentScore(11,1,'ProgramAssignment',90)
    ss2 = StudentScore(11,2,'Test',92)

    ss1.display()
    ss2.display()

#main()