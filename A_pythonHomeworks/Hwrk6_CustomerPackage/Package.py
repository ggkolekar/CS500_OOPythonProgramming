from Customer import Customer
class Package:
    def __init__(self, sender:Customer, receiver:Customer,weight:float,w8basedcost:float):
        self.__sender=sender
        self.__receiver=receiver
        self._weight=weight
        self.__w8basedcost=w8basedcost

        @property
        def weight(self):
            return self.__weight

        @property
        def w8basedcost(self):
            return self.__w8basedcost

    def calculateCost(self)->None:
        return self._weight * self.__w8basedcost
 
class TwoDayPackage(Package):
    def __init__(self, sender:Customer, receiver:Customer,weight:float,w8basedcost:float,tdpflatcost:float):
        super().__init__(sender, receiver,weight,w8basedcost)
        self.__tdpflatcost = tdpflatcost

    @property
    def tdpflatcost(self):
        return self.__tdpflatcost

    def display(self)->None:
        print("additional cost: ",self.__tdpflatcost )

    def calculateCost(self, flatcharge) -> None:
        baseCost = super(TwoDayPackage, self).calculateCost()
        return baseCost + self.__tdpflatcost

class OvernightPackage(Package):
    def __init__(self, sender:Customer, receiver:Customer,weight:float,w8basedcost:float,ovpaddincost:float):
        super().__init__(sender, receiver,weight,w8basedcost)
        self.__ovpaddincost = ovpaddincost

    @property
    def ovpaddincost(self):
        return self.__ovpaddincost

    def display(self)->None:
        print("additional  cost: ",self.__ovpaddincost )

    def calculateCost(self) -> None:
        baseCost = super().calculateCost()
        additionalCost = self._weight * self.__ovpaddincost
        return baseCost + additionalCost


def main():
    sender= Customer("john Doe","123 abc Dr", "Fremont","CA","94555")
    receiver= Customer("Jame Doe", "456 xyz Dr", "San Rafael","CA","95901")
    p=Package(sender, receiver, 7, 8.00)
    tdp=TwoDayPackage(sender,receiver, 2, 7.00, 7)
    tdp.display()
    onp=OvernightPackage(sender, receiver, 4,8.00, 7.00)
    onp.display()
    print("calculated cost: ", tdp.calculateCost(7))
    print("calculated cost: ", onp.calculateCost())



if __name__ == "__main__":
    main()