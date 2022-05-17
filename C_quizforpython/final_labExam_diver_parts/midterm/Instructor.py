from abc import ABC, abstractmethod

class Displayable(ABC):
    @abstractmethod
    def display(self) -> None:
         pass


class Course(Displayable):
    def __init__(self, courseTitle: str, numOfHWs: int):
        self.__courseTitle = courseTitle                               #initialize private classmember variable
        self._numOfHWs = numOfHWs

    @property
    def courseTitle(self):
        return self.__courseTitle

    @property
    def numOfHWs(self) -> int:
        return self._numOfHWs

    @numOfHWs.setter
    def numOfHWs(self, noOFHWs: int):
        self.__numOfHWs=noOFHWs

    def display(self) -> None:
        print('courseTitle= '+ str(courseTitle))
        print('numOfHWs= ' + str(numOfHWs))




class Instructor(Displayable):
    def __init__(self,instructorName:str, department: str, courses: [Course]):
        self.__instructorName= instructorName
        self.__department=department
        courses=List[Course]


    def display(self) -> None:
        print('instrcture= '+ str(instrctorName))
        print('department= '+ str(department))
        for c in self.__courses:                         #display list elements through looping
            print(c)

class Student():
    def __init__(self,studentName:str, project:str, courses:[Course]):
        self.__studentName = studentName
        self.__project = project
        self.__courses = courses

    @property
    def studentName(self):
        return self.__studentName


    def display(self) -> None:
        print('studentName= '+ str(studentName))
        print('project= '+ str(project))
        for c in self.__courses:
            print(c)



class GradeBook(Displayable):
    def __init__(self,instructor:str,semester:str, course:Course):
        #super().__init__(courseTitle,numOfHWs)
        #super().__init__(studentName,project,courses)
        #super().__init__(instructorName,department,courses)
        self.__instructor=instructor
        self.__semester= semester
        self.__course= course
        self._scores = {}
        self.__students= []
        #self._scores= Dict[self.__studentName:str, List[scores:int]]
        #self.__students: list[Student]

    @property
    def scores(self):
        return self._scores

    def display(self) -> None:
        print('instructor= '+str(self.__instructor))
        print('semester= '+str(self.__semester))
        print('Course= ',self.__course.courseTitle, " ",self.__course.numOfHWs)

    def addStudent(self,student: Student)->None:
        self.student.append(student)
        #self.scores[student.studentName] = List[int] = [0] * self.course.numOfHWs
        #self.scores(student.studentName,[0]*self.__course.numOfHws)



    def setHomeworkScore(self,studentName:str, hwNo:int, score:int):
        #self.scores[student.studentName] = List[int] = [0] * self.course.numOfHWs
        if studentName in self._scores:
            self._scores[studentName][hwNo-1] = score
        else:
            nhw = self.__course.numOfHWs
            hwl = [0] * nhw          #num of hws in course
            hwl[0] = score                               #value at 0th in list hwl
            self._scores[studentName] = hwl               #value at studentName in list scores

    def getHomeworkScore(self,studentName:str,hwNo:int)->int:
        return self._scores[studentName][hwNo]

class AdvGradeBook(GradeBook):
    #def __init__(self,projectScores: dict[str,int]):
    def __init__(self, instructor:str,semester:str,course:Course):
        super().__init__(instructor,semester,course)
        self.__projectScores={}

    def setProjectScore(self,studentName:str, score:int)->None:
        self.__projectScore[studentName]= score


    def getHomeworkAverageScore(self,hwNo:int)->float:
        total=0
        #count=0
        for studentName, scoreList in self.scores.items():           #looping through dictionary score by key n value
            total= total +scoreList[hwNo -1]
            #count++
            return total//len(self.scores)

    def getStudentAverageScore(self, studentName:str)->float:
        total=0
        scoreList = self.scores[studentName]      # make list of score from studentNameth value in dict scores
        for score in scoreList:
            total=total+score                       #total score

        return total / len(scoreList)                #avg score


    def display(self) -> None:
        super().display()                                    # first implement display function from superclass
        for key, value in self.__projectScores.items():    #looping through list projectscores
            print('projectScores= ', key, " ",value)


def main():

    course1 = Course('Database', 2)
    course2 = Course('Algorithm', 3)
    course3 = Course('Python',2)

    s1= Student('Peter', 'Project1',[course1, course2])
    s2 = Student('Lilly','Project2',[course2, course3])

    gradeBook1 = AdvGradeBook('VBhaskar', 'Fall', course1)
    gradeBook2 = AdvGradeBook('Chang', 'Fall', course2)
    gradeBook3 = AdvGradeBook('Cheung', 'Fall', course3)

    gradeBook1.setHomeworkScore('Peter', 1, 9)
    gradeBook1.setHomeworkScore('Peter', 2, 8)

    gradeBook2.setHomeworkScore('Peter',1, 7)
    gradeBook2.setHomeworkScore('Peter', 3, 10)
    gradeBook2.setHomeworkScore('Peter', 2, 6)

    gradeBook2.setHomeworkScore('Lilly', 1, 7)
    gradeBook2.setHomeworkScore('Lilly', 2, 6)
    gradeBook2.setHomeworkScore('Lilly', 3, 10)

    gradeBook3.setHomeworkScore('Lilly', 1, 8)
    gradeBook3.setHomeworkScore('Lilly', 1, 9)

    gradeBook1.display()
    gradeBook1.display()
    gradeBook1.display()

    print('homework avg score= ', gradeBook2.getHomeworkAverageScore(1))
    print('student avg score=  ', gradeBook2.getStudentAverageScore('Peter'))


main()








