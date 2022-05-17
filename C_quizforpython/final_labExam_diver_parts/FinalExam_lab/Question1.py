from abc import ABC, abstractmethod
from typing import List, Dict

class Displayable(ABC):
    @abstractmethod
    def display(self) -> None:
        pass

class Part(Displayable):

    def __init__(self, serialNumber:str, readings:List[float]) -> None:
        self.serialNumber:str = serialNumber
        self.readings:List[float] = readings
        self.__parts: List[Part]

    @property
    def parts(self):
        return self.__parts


    @property
    def serialNumber(self):
        return self.__serialNumber

    def display(self):
        print("serial Number: ", self.serialNumber)
        for item in self.readings:
            print("readings : ", self.__readings)

    @property
    def parts(self):
        return self.__parts

    def addPart(self, part: Part) -> None:
        self.__parts.append(part)


    def getBadParts(runData: Dict[str, List[Part]]) -> Dict[str, List[str]]:
        badParts={}
        avgVolt =0
        for key, value in runData.items():
            if (key == key.runData):
                if(value.runData== 5):
                    badParts.append(runData[Part])





class BadPart(Part):
    def __init__(self, partType: str, avgVoltage: float, serialNumber:str,readings:List[float]):
        Part.__init__(self, serialNumber, readings)
        self.__partType = partType

    @property
    def partType(self) -> int:
        return self.__partType

    def fail(self):
        avgVolt = 0
        if (avgVolt == 5):
            print("partType : " + str(self.partType) + " is failed!")


def main():

    runData ={ 'Lot123' : [],
            'Lot124' : [],
            'Lot125' : [],
            'Lot126' : [],
            'Lot126' : []}

    runData['Lot123'] =[Part('PartAA', [3.5, 3.8,3.9])]
    print("bad Part: ", runData.getBadParts)



    main()