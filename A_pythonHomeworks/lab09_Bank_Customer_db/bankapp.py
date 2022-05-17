from bankbusiness import Customer
from db import CustomerRepository


class bankapp:
    def __init__(self):
        self.__customerdb = CustomerRepository()
        self.__customer = self.__customerdb.getcustomers()
        #self.__order = Order()



    def showTitle(self):
        print("The business program")
        print()

    def showMenu(self):
        print("COMMAND MENU")
        print("display - Show the customer list")
        print("add  - Add customer to the customer repository")
        print("edit  - edit customer info from customer repository")
        print("remove  - remove customer from customer repository")
        print("printInAscenOrder  - print customer info in ascending order from customer repository")
        print("printInDesenOrder  - print customer info in descending order from customer repository")
        print("findmax  - find max balance from customer repository")
        print("findmin  - find min balance from customer repository")
        print("exit - Exit program")
        print()

    def getInput(self):

        accountNo= input(print("Enter AccountNo= "))
        Fname= input(print("Enter First Name= "))
        Lname=input(print("Enter Last Name= "))
        balance= input(print("Enter Balance= "))


