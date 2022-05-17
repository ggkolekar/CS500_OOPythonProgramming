class Student:
    def __init__(self, id : int, name : str) -> None:
        self._id = id
        self._name = name
    def display(self) -> None:
        print('Id:', self._id, 'Name:', self._name)

class GraduateStudent(Student):
    def __init__(self, id: int, name: str, concentrationArea: str):
        super().__init__(id, name)
        self._concentrationArea = concentrationArea

    def display(self) -> None:
        super().display()
        print('concentrationArea: ', self._concentrationArea)

class UndergraduateStudent(Student):
    def __init__(self, id : int, name : str, programTitle: str):
        super().__init__(id, name)
        self._programTitle = programTitle


    def display(self) -> None:
        super().display()
        print('Program Title: ', self._programTitle)

class Freshman(UndergraduateStudent):
    def __init__(self, id: int, name: str, programTitle: str , classNo: int):
        super().__init__(id, name, programTitle)
        self._classNo = classNo


    def display(self) -> None:
        super().display()
        #print('programTitle: ', self._programTitle)
        print('classNo: ', self._classNo)

class Sophomore(UndergraduateStudent):
    def __init__(self, id : int, name : str,programTitle: str, classNo: int ):
        super().__init__(id, name, programTitle)
        self._classNo = classNo

    def display(self) -> None:
        super().display()
        print('classNo: ', self._classNo)

class Junior(UndergraduateStudent):
    def __init__(self, id : int, name : str, programTitle: str, classNo: int):
        super().__init__(id, name, programTitle)
        self._classNo = classNo

    def display(self) -> None:
        super().display()
        print('classNo: ', self._classNo)

class Senior(UndergraduateStudent):
    def __init__(self, id : int, name : str, programTitle: str, classNo: int):
        super().__init__(id, name,programTitle)
        self._classNo = classNo

    def display(self) -> None:
        super().display()
        print('classNo: ', self._classNo)

class DoctoralStudent(GraduateStudent):
    def __init__(self, id : int, name : str, concentrationArea: str, classNo: int):
        super().__init__(id, name, concentrationArea)
        self._classNo = classNo


    def display(self) -> None:
        super().display()
        print('classNo: ', self._classNo)

class MastersStudent(GraduateStudent):
    def __init__(self, id : int, name : str, concentrationArea: str, classNo: int):
        super().__init__(id, name, concentrationArea)
        self._classNo = classNo

    def display(self) -> None:
        super().display()
        print('classNo: ', self._classNo)



def main():
    #stud = Student(12345, "Peter")
    #gradstud = GraduateStudent(15582, "Smith", "MBA")
    #ungradstud = UndergraduateStudent("BE")
    frsmn = Freshman(12345, "Peter","Freshman", 230)
    sfr = Sophomore(13276, "Smith","Sophomore", 250)
    jnr = Junior(12309, "Hanah", "Junior", 270)
    snr = Senior(51687, "Nancy", "Senior", 280)
    docstud = DoctoralStudent(15582,"Andy", "DoctorateStudent", 571 )
    mstrstud = MastersStudent(64272, "Tommy", "MasterStudent", 450)

    #stud.display()
    #gradstud.display()
    #ungradstud.display()
    frsmn.display()
    sfr.display()
    jnr.display()
    snr.display()
    docstud.display()
    mstrstud.display()

main()



