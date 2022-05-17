from GradedItem import GradedItem, ProgramAssignment,Test,Exam

class Policy:

    def __init__(self):
        self.__gradedItemsWeights = {}

    def addGradedItemWeightage(self,gradedItem:GradedItem, weightage:float):
        self.__gradedItemsWeights[gradedItem] = weightage

    def getGradedItemWeightage(self,itemName:str):
        for k,v in self.__gradedItemsWeights.items():
            if(k == itemName):
                return v
        return None

    def display(self):
        for key, val in self.__gradedItemsWeights.items():
            print('Graded Item Name ',key)
            print('Weightage ',val)

def main():
    p = Policy()
    p.addGradedItemWeightage(ProgramAssignment.__name__, 50.00)
    p.addGradedItemWeightage(Test.__name__,25)
    p.addGradedItemWeightage(Exam.__name__,25)

    p.display()

#main()