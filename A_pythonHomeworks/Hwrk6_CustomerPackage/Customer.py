class Customer:
    def __init__(self, name:str, address:str, city:str,state:str, zipCode:str):
        self.__name = name
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zipCode = zipCode

        @property
        def name(self):
            return self.__name

        @property
        def address(self):
            return self.__address

        @property
        def city(self):
            return self.__city

        @property
        def state(self):
            return self.__state

        @property
        def zipcode(self):
            return self.__zipcode

    def display(self)->None:
        print("name: ",self.__name )
        print("address: ",self.__address)
        print("city: ", self.__city)
        print("state: ", self.__state)
        print("zipcode: ", self.__zipcode)