class Employee:
    def __init__(self, fname: str, lname: str, monthlySalary: int):
        self.__fname = fname
        self.__lname = lname
        self.__monthlySalary = monthlySalary

    @property
    def monthlySalary(self):
        return self.__monthlySalary

    @monthlySalary.setter
    def monthly(self, monthlySalary: int):
        self.__monthlySalary= monthlySalary


def main():
    employee =[]
    emp1 = Employee(" jon ", "doe ", "15000")
    emp2 = Employee(" jane ", "doe ", "20000")
    emp3 = Employee(" mary ", "smith ", "25000")
    emp1 = Employee(" maggie ", "smith ", "30000")

    for emp in employee:
        emp.Employee(emp1)


