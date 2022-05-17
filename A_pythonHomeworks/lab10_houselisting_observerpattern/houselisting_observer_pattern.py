from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def registerObserver(self, o):
        pass

    @abstractmethod
    def removeObserver(self, o):
        pass

    @abstractmethod
    def notifyObserver(self):
        pass

class Observer(ABC):
    @abstractmethod
    def update(self, newprice, new_house, sold):
        pass

class DisplayElements(ABC):
    @abstractmethod
    def display(self):
        pass

class House(DisplayElements):
    def __init__(self, address, squareFeet, numRooms, price):
        self.__address = address
        self.__squareFeet = squareFeet
        self.__numRooms = numRooms
        self.__price = price

    # add some public properties here if necessary

    @property
    def address(self):
        return self.__address

    @property
    def squareFeet(self):
        return self.__squareFeet

    @squareFeet.setter
    def squareFeet(self, squareFeet):
        self.__squareFeet = squareFeet

    @property
    def numRooms(self):
        return self.__numRooms

    @numRooms.setter
    def numRooms(self, numRooms):
        self.__numRooms = numRooms

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price


    def display(self):
        print('address= ', self.__address)
        print('squareFeet= ', self.__squareFeet)
        print('numRooms= ', self.__numRooms)
        print('price= ', self.__price)


class Contact(DisplayElements):
    def __init__(self, firstName, lastName, phoneNumber, email):
        self.__lastName = lastName
        self.__firstName = firstName
        self.__email = email
        self.__phoneNumber = phoneNumber

    # add some public properties here if necessary

    @property
    def lastName(self):
        return self.__lastName

    @property
    def firstName(self):
        return self.__firstName

    @property
    def email(self):
        return self.__email

    @property
    def phoneNumber(self):
        return self.__phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, phoneNumber):
        self.__phoneNumber = phoneNumber



    def display(self):
        print('lastname= ', self.__lastName)
        print('firstname= ', self.__firstName)
        print('email= ', self.__email)
        print('phoneNumber= ', self.__phoneNumber)



class Owner(Contact, Observer):
    def __init__(self, lastName, firstName, phoneNumber, email):
        super().__init__(lastName, firstName, phoneNumber, email)
        self.__houses = []

    def addHouse(self, house):
        self.__houses.append(house)

    def display(self):
        super().display()
        print('houses= ', self.__houses)

    def update(self, newprice, new_house, sold):
        self.__newprice = newprice
        self.__new_house = new_house
        self.__sold = True

        newHouse = True
        if newHouse == True:
            print('{} {} got message "{}"'.format(self.firstName, self.lastName,'new house is in listing'))
            print('new house address is {}',self.__new_house)
            print('new house price is {}',newprice)
        if sold == True:
            print('{} {} got message "{}"'.format(self.firstName, self.lastName, 'The house is sold'))
            print('address of house is {}', self.__new_house)
            print('new house price is {}', newprice)




class Buyer(Contact, Observer):
    def __init__(self, lastName, firstName, phoneNumber, email):
        super().__init__(lastName, firstName, phoneNumber, email)
        self.__watchList = []
        self.__saveForLater=[]

    @property
    def watchList(self):
        return self.__watchList

    @property
    def saveForLaterList(self):
        return self.__saveForLater

    #  Save the house in his watch list
    def saveForLater(self, house):
        self.__saveForLater.append(house)

    # Remove the house from his watch list
    def removeFromSaveForLater(self, house):
        self.__saveForLater.remove(house)

    def display(self):
        super().display()
        print('saveForLater= ',self.__saveForLater)

    def update(self, newprice, new_house, sold):
        self.__newprice = newprice
        self.__new_house = new_house
        self.__sold = True

        newHouse = True
        if newHouse == True:
            print('{} {} got message "{}"'.format(self.firstName, self.lastName,'new house is in listing'))
            print('new house address is {}',self.__new_house)
            print('new house price is {}',newprice)
        if sold == True:
            print('{} {} got message "{}"'.format(self.firstName, self.lastName, 'The house is sold'))
            print('address of house is {}', self.__new_house)
            print('new house price is {}', newprice)


class Agent(Contact, Observer):
    def __init__(self, lastName, firstName, phoneNumber, email, position, company):
        super().__init__(lastName, firstName, phoneNumber, email)
        self.__position = position
        self.__company = company

    @property
    def position(self):
        return self.__position

    @property
    def company(self):
        return self.__company

    def addHouseToListingForOwner(self, owner, house):
        self.__company.addOwner(owner)
        self.__company.addHouseToListing(house)

    def helpBuyerToSaveForLater(self, buyer, house):
        #self.__company.addBuyer(buyer)  # to avoid duplicate entry of buyer
        if self.__company.getHouseByAddress(house.address) is not None:
            buyer.saveForLater(house)
        else:
            print('Could not find your dream house but we kept your information first!')


    def editHousePrice(self, address, newPrice):
        self.__company.editHousePrice(address, newPrice)

    def soldHouse(self, house):
        print('House sold= ','address=', house.address,'squareFeet=', house.squareFeet,'numRooms=', house.numRooms,'price=', house.price)

    def display(self):
        super().display()
        print('position= ', self.__position)
        print('company= ', self.__company)


    def update(self, newprice, new_house, sold):
        self.__newprice = newprice
        self.__new_house = new_house
        self.__sold = True

        newHouse = True
        if newHouse == True and sold == False:
            print('{} {} got message "{}"'.format(self.firstName, self.lastName,'new house is in listing'))
            print('new house address is {}',self.__new_house)
            print('new house price is {}',newprice)
        if sold == True:
            print('{} {} got message "{}"'.format(self.firstName, self.lastName, 'The house is sold'))
            print('address of house is {}', self.__new_house)
            print('new house price is {}', newprice)


class EngineData(Subject):
    def __init__(self):
        self.__observers = []

    def registerObserver(self, o):
        self.__observers.append(o)

    def removeObserver(self, o):
        i = self.__observers.index(o)
        if i >= 0:
            self.__observers.pop(i)

    def notifyObserver(self):
        for o in self.__observers:
            o.update(self.__price, self.__new_house, self.__sold)
            print()

    def meaurementsChanged(self):
        self.notifyObserver()

    def setMeasurements(self, price,new_house, sold):
        self.__price = price
        self.__new_house = new_house
        self.__sold = sold
        self.meaurementsChanged()

class DigitalDisplay(Observer, DisplayElements):
    def __init__(self, engineData):
        self.__engineData = engineData
        self.__newprice = 0
        self.__new_house = 0.0
        self.__sold = 0.0
        engineData.registerObserver(self)

    def display(self):
        print("Digital Display:")
        print("new price =", self.__newprice)
        print("new house address =", self.__new_house)
        print("house is not sold =", self.__sold)

    def update(self, newprice, new_house, sold):
        self.__newprice = newprice
        self.__new_house = new_house
        self.__sold = sold
        self.display()


class Company(DisplayElements):
    def __init__(self, companyName):
        self.__companyName = companyName
        self.__owners = []
        self.__buyers = []
        self.__agents = []
        self.__houses = []
        self.__saveForLater=[]

    @property
    def companyName(self):
        return self.__companyName
    @property
    def company(self):
        return self.__company

    @property
    def buyers(self):
        return self.__buyers

    @property
    def owners(self):
        return self.__owners

    @property
    def agents(self):
        return self.__agents

    @property
    def houses(self):
        return self.__houses


    def addOwner(self, owner):
        self.__owners.append(owner)

    def addBuyer(self, buyer):
        self.__buyers.append(buyer)

    def addAgent(self, agent):
        self.__agents.append(agent)

    def addHouseToListing(self, house):
        if self.getHouseByAddress(house.address) is None:
            self.__houses.append(house)

    def getHouseByAddress(self, address):
        for h in self.__houses:
            if address==h.address:
                return h

    def removeHouseFromListing(self, house):
        for h in self.__houses:
            if house == h.house:
                self.__houses.remove(house)

    # Help to remove that house from all buyers' watch list.
    def removeHouseFromSaveForLater(self, house):
        self.__saveForLater.remove(house)

    def getBuyersByHouse(self, house):
        buyers = []
        for b in self.buyers:
            for h in b.saveForLaterList:
                if house.address == h.address:
                    buyers.append(b)
        return buyers

    def editHousePrice(self, address, newHousePrice):
        for h in self.__houses:
            if address == h.address:
                h.price= newHousePrice


    def display(self):
        print('List of owners= ')
        for w in self.__owners:
            print('firstName=', w.firstName,'lastName=', w.lastName,'phoneNumber=', w.phoneNumber,'email=', w.email )
        print('List of buyers= ')
        for b in self.__buyers:
            print('lastName=', b.lastName,'firstName=', b.firstName,'phoneNumber=', b.phoneNumber,'email=', b.email)
        print('List of agents= ')
        for a in self.__agents:
            print('lastName=', a.lastName,'firstName=', a.firstName,'phoneNumber=', a.phoneNumber,'email=', a.email,'position=', a.position,'company=', a.company )
        print('List of houses= ')
        for h in self.__houses:
            print('address=', h.address,'squareFeet=', h.squareFeet,'numRooms=', h.numRooms,'price=', h.price)


    # print all potential buyers who are interested in buying that house
    def printPotentialBuyers(self, house):
        for b in  self.getBuyersByHouse(house):
            print('Potential Buyers= ', b.firstName, b.lastName,b.phoneNumber, b.email)


def main():
    owner1 = Owner('Peter', 'Li', '510-111-2222', 'peter@yahoo.com')
    owner2 = Owner('Carl', 'Buck', '408-111-2222', 'carl@yahoo.com')

    house1 = House('1111 Mission Blvd', 1000, 2, 1000000)
    house2 = House('2222 Mission Blvd', 2000, 3, 1500000)
    house3 = House('3333 Mission Blvd', 3000, 4, 2000000)

    owner1.addHouse(house1)
    owner2.addHouse(house2)
    owner2.addHouse(house3)

    buyer1 = Buyer('Tom', 'Buke', '408-555-2222', 'tom@yahoo.com')
    buyer2 = Buyer('Lily', 'Go', '510-222-3333', 'lily@yahoo.com')
    """
    buyer1.saveForLater(house1)
    buyer1.saveForLater(house2)

    buyer2.saveForLater(house2)
    buyer2.saveForLater(house3)
    """

    company = Company('Good Future Real Estate')
    agent1 = Agent('Dave', 'Henderson', '408-777-3333',
                   'dave@yahoo.com', 'Senior Agent', company)
    company.addAgent(agent1)

    company.addBuyer(buyer1)
    company.addBuyer(buyer2)

    agent1.addHouseToListingForOwner(owner1, house1)
    agent1.addHouseToListingForOwner(owner2, house2)
    agent1.addHouseToListingForOwner(owner2, house3)

    agent1.helpBuyerToSaveForLater(buyer1, house1)
    agent1.helpBuyerToSaveForLater(buyer1, house2)
    agent1.helpBuyerToSaveForLater(buyer1, house3)

    agent1.helpBuyerToSaveForLater(buyer2, house2)
    agent1.helpBuyerToSaveForLater(buyer2, house3)

    agent1.editHousePrice('2222 Mission Blvd', 1200000)

    company.display()

    print('\nAfter one house was sold ..........................')
    agent1.soldHouse(house3)
    company.display()

    print('\nDisplaying potential buyers for house 1 ..........................')
    company.printPotentialBuyers(house1)
    print()

    engineData = EngineData()

    #analog = AnalogDisplay(engineData)
    digital = DigitalDisplay(engineData)

    print("The first setMeasurements called.")
    engineData.setMeasurements(100000, '1000, Fremont Blvd', True)
    engineData.registerObserver(digital)
    #engineData.notifyObserver()

    engineData.removeObserver(digital)
    print('The house is removed from the list.')
    print()


    print("The second setMeasurements called.")
    engineData.setMeasurements(150000, '2000, Fremont Blvd', True)

    engineData.registerObserver(digital)

    print("The third setMeasurements called.")
    engineData.setMeasurements(175000, '3000, Fremont Blvd', True)




if __name__ == "__main__":
    main()

