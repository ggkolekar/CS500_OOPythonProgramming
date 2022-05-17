from abc import ABC, abstractmethod
import enum

class Displayable(ABC):
    @abstractmethod
    def display(self) -> None:
        pass

class flyable(ABC):
    def fly(self) -> None:
        pass


class Product(Displayable):
    def __init__(self,productName:str,basePrice:float):
        super().__init__(self)
        self.productName=productName
        self.basePrice=basePrice


    @property
    def productName(self):
        return self.productName

    @property
    def basePrice(self):
        return self.basePrice



    def display(self)->None:
        print('productName= '+ str(self.productName))
        print('basePrice= ' + str(self.basePrice))



class Computer():
    def __init__(self, model:str, speed:float, touch:bool, cellular:bool):
        super().__init__(self,productName, basePrice)
        self.model=model
        self.speed=speed
        self.touch=False
        self.cellular=False

    @property
    def model(self)->str:
        return self.model

    @property
    def speed(self)->float:
        return self.speed

    @speed.setter
    def speed (self,speed:float)->float:
        self.speed=speed

    def computer(self)-> None:

    def addBaseprice(self):
        if touch == False:
            return
        else:
            basePrice= basePrice + 15/100


        if cellular == False:
            return
        else:
            basePrice= baseprice+1/10

    def display(self) -> None:
        print('model= ' + str(self.model))
        print('speed= ' + str(self.speed))

class Drone():
    def __init__(self,camera:str, maxFlightTime:float, gps:bool):
        super().__init__(self, productname,baseprice)
        self.camera=camera
        self.maxFlightTime=maxFlightTime
        self.gps=False


        @property
        def camera(self)->str:
            return self.camera

        @property
        def maxFlightTime(self)->float:
            return maxFlightTime


    def record(self)->None:
        print("maxFlightTime= "+ str(self.maxFlightTime))

    def display(self)->None:
        print('camera= '+ str(self.camera))
        print('maxFlightTime= ' + str(self.maxFlightTime))


class Factory(Displayable):
    def __init__(self, factoryName:str, products: list[Product]):
        super().__init__(self, )
        self.factoryName=factoryName
        self.__products= list[Product]

    @property
    def factoryName(self)->str:
        return factoryName

    def products(self)->list[Product]:
        return self.__products


    def display(self) -> None:
        print('factoryName= ' + str(self.factoryName))
    #print('speed= ' + str(self.speed))



    def addProduct(product:Product)->None:
        self.products.append(Product)



    def getTopFiveFastestComputers(self)-> List[Computer]:


    def getAllDronesWithGPS(self)-> List[Drone]:
        droneswithgps=list[Drone]
        for P in self.products:
            if(isinstance(Drone, gps)):
                droneswithgps.append(Drone)


    def getProduct(self, index):Product
        print ('Product= '+ str(Product))







class BuildingType(enum):
    def __init__(self, HEAVY_INDUSTRIAL=0, WAREHOUSE=1,COLD_STORAGE=2,LIGHT_INDUSTRIAL=3,DATA_HOUSING=4)
        self.HEAVY_INDUSTRIAL=0
        self.WAREHOUSE=1
        self.COLD_STORAGE=2
        self.LIGHT_INDUSTRIAL=3
        self.DATA_HOUSING=4


    def display(self)->None:
        print('HEAVY_INDUSTRIAL= '+ str(self.HEAVY_INDUSTRIAL))
        print('WAREHOUSE= ' + str(self.WAREHOUSE))
        print('COLD_STORAGE= ' + str(self.COLD_STORAGE))
        print('LIGHT_INDUSTRIAL= ' + str(self.LIGHT_INDUSTRIAL))
        print('DATA_HOUSING= ' + str(self.DATA_HOUSING))





class Building():
    def __init__(self, buildindName: str, area: float, stories: int, type: BuildingType)
        self.buildingName=buildingName
        self.area=float
        self.stories=stories
        self.type=BuildingType

    @property
    def area(self):
        return self.area

    @area.setter
    def area(self, area):
        self.area=area



    @property
    def buildingName(self):
        return self.buildingName

    @property
    def stories(self):
        return self.stories

    @property
    def type(self):
        return self.BuildingType


    def display(self):
        print('buildingName= ' + str(self.buildingName))
        print('stories= ' + str(self.stories))
        print('BuildingType= ' + str(self.BuildingType))
        print('area= ' + str(self.area))


class ProductFactory():

    def __init__(self, category:str, buildings: List[Building]):
        self.category=category
        buildings= List[Building]

    def findLargestBuilding(self)-> Building:
        largestStore=1
        largestStoreB=[]
        for stories in Building:
            if (stories >2)
                largestStore= stories
            largestStoreB.append(largestStore)
        return largestStoreB




    def findAllProductMoreThan(self, price:double):List[Product]


    def getBuildingsByType(self):Dict[BuildingType, List[Building]]






def main():
    products=[]
    P1= Product('computer', 20000)
    P2 = Product('computer', 30000)
    P3 = Product('Drone', 20000)
    P4=Product('Drone', 30000)

    products.append(p1)
    products.append(p2)
    products.append(p3)
    products.append(p4)

    for product in products:
        product.display()
        print()

    getAllDronesWithGPS().display()

    buildings=[]
    buildings.addBulding(Building('Costco',1000,2,'WAREHOUSE'))
    buildings.addBulding(Building('NorthView', 1000, 2, 'DATAHOUSING'))
    buildings.addBulding(Building('Storeroom', 1000, 2, 'COLD_STORAGE'))
    buildings.addBulding(Building('VACAVILLE', 1000, 2, 'HEAVY_INDSTRIAL'))

    Dict=[BuildingType,List[Building]]

    getBuildingsBytype().display






