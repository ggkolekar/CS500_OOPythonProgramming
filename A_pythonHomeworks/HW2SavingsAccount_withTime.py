#!/usr/bin/python
from datetime import datetime
class Time:
    def __init__(self, h = 0, m = 0, s = 0):
        self.__showTm = None
        self.__h = h
        self.__m = m
        self.__s = s

    @property
    def h(self) -> None:
        return self.h

    @property
    def m(self) -> None :
        return self.m

    @property
    def s(self) -> None :
        return self.s

    def showTm(self):
        print("Hour:", self.h)
        print("Minute:", self.m)
        print("Second:", self.s)

    @property
    def showTm(self):
        return self.showTm

    def timenow(self) -> str:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return current_time
        #print("Current Time =", current_time)

    def advanceTm(self, h, m, s):

        secs = self.__s + s
        mins = self.__m + m
        hrs = self.__h + h

        if secs > 59:
            mins += secs / 60
            secs = secs % 60
        if mins > 59:
            hrs += mins / 60
            mins = mins % 60
        if hrs > 23:
            hrs = (int) (hrs % 24)

        self.__h = hrs
        self.__m = mins
        self.__s = secs

    def set(self, h, m, s):
        self.__h = h
        self.__m = m
        self.__s = s

    def __str__(self):
        return str(self.__h) + ":" + str(self.__m) + ":" + str(self.__s)
"""
t1 = Time(10,15,30)
t1.set(11,16,31)
t1.show()
t1.advance(15,55,1)
t1.show()
"""

class SavingAccount:
    def __init__(self, name: str, annualinterest: float, balance: float, lastupdated: Time):
        self.__annualinterest = annualinterest    #initialized attribute
        self.__balance = balance                  #initialised attribute
        self.__time = lastupdated
        self.__name = name

    def __init__(self, name: str, balance: float, lastupdated: Time):
        self.__annualinterest = None
        self.__balance = balance
        self.__time = lastupdated
        self.__name = name

    @property
    def annualinterest(self) -> float:
        return self.__annualinterest

    @annualinterest.setter
    def annualinterest(self, annualinterest: float, value):
        self.__annualinterest = value

    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, value) -> None:
        self.__balance = value

    @property
    def time(self) -> Time:
        return self.__time

    @time.setter
    def time(self, value) -> None:
        self.__time = value


    def updateBalance(self, annualinterestrate: float, lastupdated: Time):
        # convert annual interest rate to monthly interest
        monthlyInterestRate = annualinterestrate/12/100

        # calculate the future value
        monthlyInterestAmount = self.balance * monthlyInterestRate
        estimatedBalance = self.balance + monthlyInterestAmount
        self.balance = estimatedBalance
        self.time = lastupdated

        print(str(lastupdated)+" and "+ str(self.time))


    def displaySavingAccountwithTime(self):

        # format and display the result
        #print("Balance: \t\t" + "{:.2f})".format(self.balance) + "," + "Updated: \t\t" + '{0:02d}:{1:02d}):{2:02d}'.format(self.time))
        print("Balance "+str(self.balance)+" Last updated "+str(self.time))    #Instead of formating time printed string with property instance


def main():
    time = Time()
    sa1 = SavingAccount("John",1000, time.timenow)   #initializing saving account holders instances
    sa2 = SavingAccount("Sam",2000, time.timenow)
    sa3 = SavingAccount("Lilly",3000, time.timenow)
    sa4 = SavingAccount("Kelly",4000, time.timenow)
    sa5 = SavingAccount("Carlos",5000, time.timenow)

    # get inputs from the keyboard
    annualInterestRate = float(input("Enter annual interest rate:\t"))

    confirm = 'Y'
    while confirm.lower() == 'y':
        # get the estimated balance
        sa1.updateBalance(annualInterestRate, time.timenow())
        sa2.updateBalance(annualInterestRate, time.timenow())
        sa3.updateBalance(annualInterestRate, time.timenow())
        sa4.updateBalance(annualInterestRate, time.timenow())
        sa5.updateBalance(annualInterestRate, time.timenow())

        time = Time()
        print("Balance at the end of ")
        sa1.displaySavingAccountwithTime()
        sa2.displaySavingAccountwithTime()
        sa3.displaySavingAccountwithTime()
        sa4.displaySavingAccountwithTime()
        sa5.displaySavingAccountwithTime()

        # see if user wants to continue
        confirm= input("Continue ? (y/n): ")
        if(confirm.lower() == 'n'): break

    annualInterestRate = float(input("Enter different annual interest rate:\t"))
    confirm = 'Y'
    while True:
        # get the estimated balance
        sa1.updateBalance(annualInterestRate, time.timenow())
        sa2.updateBalance(annualInterestRate, time.timenow())
        sa3.updateBalance(annualInterestRate, time.timenow())
        sa4.updateBalance(annualInterestRate, time.timenow())
        sa5.updateBalance(annualInterestRate, time.timenow())

        print("Balance at the end of ")
        sa1.displaySavingAccountwithTime()
        sa2.displaySavingAccountwithTime()
        sa3.displaySavingAccountwithTime()
        sa4.displaySavingAccountwithTime()
        sa5.displaySavingAccountwithTime()

        # see if user wants to continue
        confirm = input("Continue ? (y/n): ")
        if (confirm.lower() == 'n'):
            break


if __name__ == '__main__':
    main()