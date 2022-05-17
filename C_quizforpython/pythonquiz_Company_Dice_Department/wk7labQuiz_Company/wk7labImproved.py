from abc import ABC, abstractmethod

class Displayable(ABC):
    @abstractmethod
    def display(self) -> None:
        pass

class Employee(Displayable):
    def __init__(self, empId: int, salary: float ):
        self.__empId = empId
        self.__salary = salary

    @property
    def empId(self) -> int:
        return self.__empId

    @property
    def salary(self) -> int:
        return self.__salary

    @salary.setter
    def salary(self,salary: float)->float:
        self.__salary= salary


    def display(self) -> None:
        print("Employee "+ self.__empId+" "+str(self.salary))


class CompanyConstant():
    def __init__(self):
        self.__MAX_EMPLOYEE_SIZE = 10

    @property
    def maxemployeeSize(self) -> int:
        return self.__MAX_EMPLOYEE_SIZE

    @maxemployeeSize.setter
    def maxemployeeSize(self) -> int:
        self.__MAX_EMPLOYEE_SIZE = 10


class Company(CompanyConstant):
    def __init__(self, compName: str, numEmployees: int):
        self.__compName = compName
        self.__employees = []
        self.__numEmployees= numEmployees


    @property
    def compName(self):
        return self.__compName

    @property
    def employees(self) -> list[Employee]:
        return self.__employees

    @property
    def numEmployees(self) -> None:
        return self.__numEmployees

    @numEmployees.setter
    def numEmployees(self,numEmployees: int) -> int:

        self.__numEmployees = numEmployees


    def addEmployee(self,employee):
        employees = []
        maxnumemployee=0
        for employee in employees:
            if len(employees) <= 10:
                self.__employees.append(employee)
                maxnumemployee += 1
        return employees


class InternetCompany(Company):
    def __init__(self, compName: str, numEmployees: int, url: str) -> None:
        Company.__init__(self,compName,numEmployees)
        self.__url= url


    def getEmployeesHighSalary(self, limit: float):
        EmployeesHighSalary = []
        for emp in self.employees:
            if emp.salary >= limit:
                EmployeesHighSalary.append(emp)
        return EmployeesHighSalary


def main():
    emp1 = Employee("01", 12000)
    emp2 = Employee("02", 12000)
    emp3 = Employee("03", 12000)
    emp4 = Employee("04", 12000)
    emp5 = Employee("05", 12000)
    emp6 = Employee("06", 12000)
    emp7 = Employee("07", 12000)

    cmp = Company("Unicorn Corp", 10)
    cmp.addEmployee(emp1)
    cmp.addEmployee(emp2)
    cmp.addEmployee(emp3)

    icmp = InternetCompany("i company",100,"abc")



    emp1.display()
    print()

    print("\nEmployees high salary than limit----")
    empwithHighSal = icmp.getEmployeesHighSalary(10000)

    for emp in icmp.employees:
        emp.display()


main()
