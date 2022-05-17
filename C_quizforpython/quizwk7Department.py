class Department:
    def __init__(self, deptName: str, building: Building, professor: List[]):
        self.__deptName = deptName
        self.__building = Building
        self.__professor: professor


    def addProfessors(self,prof: Professor):None

        self.__professor.append(addProfessors(prof))


    def getSeniorProfessor(self):List[Professor]
        for senior in self.__senior:
            if self.__professor == senior
                self.__professor.append(getSeniorProfessor())





    def __str__(self) -> str:
        return "deptName: {0}, building: {1} ,professor: {2}".format(self.__deptName, self.Building, List[Professor])

class Professor:
    def __init__(self, name: str, senior : bool):
        self.__name = name
        self.__senior = senior




    def __str__(self) -> str:
        return "name: {0}, senior: {1} ".format(self.__name, self.__senior)

class Building:
    def __init__(self, buildingName: str, stories : int):
        self.__buildingName = buildingName
        self.__stories = stories


    def __str__(self) -> str:
        return "buildingName: {0}, stories: {1} ".format(self.__buildingName, self.__stories)


def main():
    professor =Professor('xyz', 'abc',['ac', 'ad', 'bc'] )
    print(str(professor))
    department = Department('xyz', 5, 3.0)
    print(str(department))
    building = Building('abc', 2)
    print(str(building))
if __name__ == '__main__':
    main()