
class Customer:
    def __init__(self, accountNo: int, Lname:str, Fname:str, balance:int):
        self.__accountNo= accountNo
        self.__Lname=Lname
        self.__Fname = Fname
        self.__balance = balance

    @property
    def accountNo(self):
        return self.__accountNo

    @accountNo.setter
    def accountNo(self, accountNo: int):
        self.__accountNo = accountNo


    @property
    def Lname(self):
        return self.__Lname

    @property
    def Fname(self):
        return self.__Fname

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance:int):
        self.__balance=balance

    def display(self):
        print('accountNo=',self.__accountNo,'Fname=', self.__Fname, 'Lname=', self.__Lname, 'balance=', self.__balance)



    def getAccountNo (self, accountNo:int):
        self.__customers[accountNo]= accountNo
        return accountNo