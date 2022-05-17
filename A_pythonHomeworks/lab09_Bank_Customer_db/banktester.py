import db
from bankbusiness import Bank
from Customer import Customer
from db import CustomerRepository


def main():
    bank1 = Bank('Bank of America')

    #customers = db.getcustomers()
    cust1 = Customer(1234, 'Peter', 'Pan', 10000)
    cust2 = Customer(5678, 'Swati', 'Train', 20000) 
    cust3 = Customer(7842, 'jessie', 'Carleon', 30000)
    cust4 = Customer(8237, 'lucy', 'Smith', 40000)
    cust5 = Customer(7372, 'Ryan', 'Baker', 50000)
    bank1.addCustomer(cust1)
    bank1.addCustomer(cust2)
    bank1.addCustomer(cust3)
    bank1.addCustomer(cust4)
    bank1.addCustomer(cust5)
    print("display of the customers= ")
    bank1.display()

    maxBalance = bank1.findBiggestAccountBalance()
    print('maxBalance= ', int(maxBalance))

    minBalance = bank1.findSmallestAccountBalance()
    print('minBalance= ', int(minBalance))

    cust6 = Customer(1234, 'Peter', 'Pan', 17000)
    bank1.editCustomerInfo(cust6)

    bank1.removeCustomer(cust4)

    bank1.display()

    sortedCustomerAscOrder = bank1.printCustomerInfoInAscnOrder()
    for c in sortedCustomerAscOrder:
        print("Ascencustomer= ", c.accountNo, c.Fname, c.Lname, c.balance)

    print()

    sortedCustomerReverseOrder = bank1.printCustomerInfoInReverseOrder()
    for c in sortedCustomerReverseOrder:
        print("Reversecustomer= ", c.accountNo, c.Fname, c.Lname, c.balance)

    print()


if __name__ == "__main__":
    main()