
class Diver:
    def __init__(self, name, difficulty, score1:float,score2:float,score3,score4,score5,score6,score7,score8,score9):
        self.__name=name
        self.__difficulty=difficulty
        self.__score1 = score1
        self.__score2 = score2
        self.__score3 = score3
        self.__score4 = score4
        self.__score5 = score5
        self.__score6 = score6
        self.__score7 = score7
        self.__score8 = score8
        self.__score9 = score9

    @property
    def name(self):
        return self.__name

    @property
    def difficulty(self):
        return self.__difficulty





class Score:
    def __init__(self, diver:Diver, divers:[Diver]):
        self.__divers= divers


    def listDiver(self):
        divers=[]
        for i in range(len(divers)):
            print(i+1,score[i])

        print()

    def addDatatoArrayList(self,diverName:str,difficulty:float, divers: [Diver],score1,score2,score3,score4,score5,score6,score7,score8,score9):
        divers.append(diverName)
        divers.append(difficulty)
        divers.append(score1)
        divers.append(score2)
        divers.append(score3)
        divers.append(score4)
        divers.append(score5)
        divers.append(score6)
        divers.append(score7)
        divers.append(score8)
        divers.append(score9)


    def gethighestscore(self,divers):
        max=0
        for i in divers:
            if (i.score >= divers[i]):
                max=divers[i]
            else:
                max= divers[i]






    def calculateDiversFinalscore(self,divers):
        finalscore=0
        for i in divers:
            if(divers[i]== i.score):
            finalscore=i.score+i.score

        return finalscore












def main():
    divers=[]
    d1=Diver('Peter', 2.5, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0)
    d2 =Diver('David' , 3.5, 9.0, 8.0, 7.0, 8.0, 8.0, 5.0, 8.0, 9.5, 5.5)
    d3 =Diver('Judy', 2.5, 9.5, 8.0, 8.5, 8.0,7.0, 5.5, 8.5, 9.5, 10.0)

    divers.addDatatoArrayList(d1)
    divers.addDatatoArrayList(d2)
    divers.addDatatoArrayList(d3)
