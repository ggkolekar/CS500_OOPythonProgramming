from abc import ABC, abstractmethod, abstractproperty
from datetime import date

import today as today


class PredictiveOil1:
    def __init__(self,futureDate, currentPrice, additionalPrice):
        self.__futureDate = futureDate

    def predictFuturePrice(futureDate, currentPrice, additionalprice):
        today =date.today()
        curdate= today.strftime(%d/%m/%Y)
        futurePrice=currentPrice+additionalprice

        return futurePrice
class PredictiveOil2:
    def __init__(self,futureDate, currentPrice, additionalPrice, someData2):
        self.__futureDate = futureDate
    def predictFuturePrice(futureDate, currentPrice, additionalPrice, someData2):
        today = date.today()
        curdate = today.strftime( % d / % m / % Y)
        futurePrice=currentPrice+additionalprice

        return futurePrice

class PredictiveOil3:
    def __init__(self,futureDate, currentPrice, additionalPrice, someData2, someData3):
        self.__futureDate=futureDate

    def predictFuturePrice(futureDate, currentPrice, additionalPrice, someData2, someData3):
        today = date.today()
        curdate = today.strftime( % d / % m / % Y)
        futureDate=
        futurePrice=currentPrice+additionalprice

        someData2=
        someData3=

        return futurePrice

class PredictiveOilFactory(ABC):
    @abstractmethod
    def createPredictiveOil(self):
        pass


class ClientPredictiveOilFactory:
    def createPredictOilFactory(self,currentPrice):
        factoryMap = {
            "PD1": PredictiveOil1,
            "PD2": PredictiveOil2,
            "PD3": PredictiveOil3
        }
        predictOilFactory = factoryMap.get(currentPrice)()

        return predictOilFactory



def main():
    po = PredictiveOil1()

    futureDate = input("Enter future date: ")

    currentDate = input("Enter current date: ")

    currentPrice = input("Enter current price: ")

    someData = input("Enter some data: ")

    futurePrice = po.predictFuturePrice(futureDate, currentPrice, someData)



