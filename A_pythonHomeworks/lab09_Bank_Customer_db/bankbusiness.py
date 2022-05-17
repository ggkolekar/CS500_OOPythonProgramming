from typing import List
from operator import attrgetter
from Customer import Customer
from db import CustomerRepository

class Bank:
    def __init__(self, bankName:str) -> None:
        self.__bankName = bankName
        #self.__customers: List[Customer]=[]
        self.__customerdb = CustomerRepository()
        self.__customers = self.__customerdb.getcustomerList()

    def __refresh(self):
        self.__customers = self.__customerdb.getcustomerList()

    def addCustomer(self, customer: Customer) -> None:
        self.__customerdb.addnewCustomer(customer)
        self.__refresh( )

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        if self.__index == len(self.__customers)-1:
            raise StopIteration
        self.__index +=1
        customers = self.__customers[self.__index]
        return customers



    def printCustomerInfoInAscnOrder(self):
        asceSortedCustomers = sorted(self.__customers,key=attrgetter('accountNo') )
        return asceSortedCustomers

    def printCustomerInfoInReverseOrder(self):
        #customerList: List[Customer] = []
        desceSortedCustomers = sorted(self.__customers,key=attrgetter('Fname'), reverse=True)
        return desceSortedCustomers[:5]


    def editCustomerInfo(self, customer: Customer):
        self.__customerdb.updateCustomer(customer)
        self.__refresh()

    def removeCustomer(self, customer: Customer):
        self.__customerdb.removeCustomer(customer)
        print("Account " + str(customer.accountNo) + " was deleted.\n")


    def findBiggestAccountBalance(self):
        max= 0
        for cust in self.__customers:
            if max <= cust.balance:     # access getter balance
                max = cust.balance      # balance is not a attribute

        return max



    def findSmallestAccountBalance(self):
        min = self.__customers[0].balance
        for cust in self.__customers:
            if min >= cust.balance:
                min= cust.balance

        return min

    def display(self):
        for c in self.__customers:
            print (c.display())


def main():
    bank1 = Bank('Bank of America')

    cust1 = Customer(1234, 'Peter', 'Pan', 10000)
    cust2 = Customer(5678, 'Swati', 'Train', 20000)
    cust3 = Customer(1234, 'jessie', 'Carleon', 30000)
    cust4 = Customer(1234, 'lucy', 'Smith', 40000)
    cust5 = Customer(1234, 'Ryan', 'Baker', 50000)

    bank1.addCustomer(cust1)
    bank1.addCustomer(cust2)
    bank1.addCustomer(cust3)
    bank1.addCustomer(cust4)
    bank1.addCustomer(cust5)
    #cust1.display()

    bank1.display()

    sortedCustomerAscOrder = bank1.printCustomerInfoInAscnOrder()
    for c in sortedCustomerAscOrder:
        print('Lname: ', c.Lname, 'Fname: ', c.Fname, 'accountNo: ',c.accountNo, 'balance: ', c.balance)

    #print()

    sortedCustomerReverseOrder = bank1.printCustomerInfoInReverseOrder()
    for c in sortedCustomerReverseOrder:
        print('Lname: ', c.Lname, 'Fname: ', c.Fname, 'accountNo: ', c.accountNo, 'balance: ', c.balance)

    print()

    maxBalance= bank1.findBiggestAccountBalance()
    print('maxBalance= ',int(maxBalance))

    minBalance = bank1.findSmallestAccountBalance()
    print('minBalance= ', int(minBalance))


    Ascencustomer= bank1.printCustomerInfoInAscnOrder()
    for c in Ascencustomer:
        print("Ascencustomer= ", c.accountNo, c.Fname, c.Lname, c.balance)

    print()

    Reversecustomer = bank1.printCustomerInfoInReverseOrder()
    for c in Reversecustomer:
        print("Reversecustomer= ", c.accountNo, c.Fname, c.Lname, c.balance)

    print()

#if __name__ =="__main__":
    #main()