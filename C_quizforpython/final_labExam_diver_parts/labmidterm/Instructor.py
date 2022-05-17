from abc import ABC


class Displayable(ABC):
    @abstractmethod
    def display(self) -> None:
         pass


class Course(Displayable):
    def __init__(self, courseTitle: str, numOfHWs: int):
        self.__courseTitle=courseTitle
        self.__numOfHWs= numOfHWs

    @property
    def courseTitle(self):
        return self.__courseTitle

    @property
    def numOfHWs(self):
        return self.__numOfHWs

    @numOfHWs.setter
    def numOfHWs(self):
        self.__numOfHWs=numOfHWs

    def display(self) -> None:
        print('courseTitle= '+ str(courseTitle))
        print('numOfHWs= ' + str(numOfHWs))




class Instructer(Displayable):
    def __init__(self,instructorName:str, department: str, courses: List[Course]):
        self.__instructorName= instructorName
        self.__department=department
        courses=List[Course]


    def display(self) -> None:
        print('instrcture= '+ str(instrctorName))
        print('department= '+ str(department))

class Student():
    def __init__(self,studentName:str, project:str, courses:List[Course]):


    def display(self) -> None:
        print('studentName= '+ str(studentName))
        print('project= '+ str(project))


class AdvGradeBook():
    def __init__(self,projectScores: dict[str,int]):
        super().__init__(studentName,project,courses[List])
        self.__projectScores=projectScores

    def setProjectScore(studentName:str, score:int)->None:
        self.__projectScore= projectScore


    def getHomeworkAverageScore(hwNo:int)->float:
        total=0
        count=0
        for score in self.scores:
            total=scores[self.__score] += scores[self.__score]
            count++
            return total//count

    def getStudentAverageScore(studentName:str)->float:

    def display(self) -> None:
        print('projectScores= '+ str(projectScores))



class GradeBook(Displayable):
    def __init__(self,instructor:str,semester:str,course:Course, scores:Dict[str, List[int]],students:list[Student]):
        super().__init__(courseTitle,numOfHWs)
        super().__init__(studentName,project,courses)
        super().__init__(instructorName,department,courses)
        self.__instructor=instructor
        self.__semester= semester
        self.__course= Course
        scores= Dict[self.__studentName:str, List[scores:int]]
        students: list[Student]


    def display(self) -> None:
        print('instructor= '+str(instructor))
        print('semester= '+str(semester))

    def addStudent(student: Student)->None:
        self.student.append(student)



    def setHomeworkScore(studentName:str, hwNo:int, score:int)-> int:
        self.scores[student.studentName] = List[int] = [0] * self.course.numOfHWs

    def getHomeworkScore(studentName:str,hwNo:int)->int:
        homeWkScore = {}
        parts = None
        homeWkScore = None
        for score in self.scores:
            if (isinstance(scores, score)):
                # movablePart = MovablePart(part)
                if studentName.score in homeWkScore:
                    homeWkScore = homeWkScore.get(studentName.score)
                    homeWkScore.append(Score)
                else:
                    homeWkScore[scores.score] = [score]
        return homeWkScore


def main():
    numOfHWs=5
    HW1 =setHomeworkScore('Peter',1, 10)
    HW2 = setHomeWorkScore('Peter',2, 10)
    HW3 = setHomeWorkScore('Peter',3, 10)
    HW4 = setHomeWorkScore('Peter', 4, 10)
    HW5 = setHomeWorkScore('Peter', 3, 10)

    scores=Dict[str,List[int]]
    for sname in scores
        for score.studentName in scores
            scores[self.__score]= [score]








