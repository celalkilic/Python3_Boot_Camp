#private variable
#super keyword

class Vehicle:

    #double underscore private, single underscore is protected
    #you can use same concept for methods

    def __init__(self, name, color):
        #__name is private tp vehicle class
        self.__name = name
        self.__color = color

    def getColor(self): #getClor() function is accessible to class Car
        return self.__color

    def setColor(self,color): #setClor() function accessible outside the class
        self.__color = color
    def getName(self):
        return self.__name
class Car(Vehicle):
    def __init__(self, name, color, model):
        #call parent constructor to set name and color
        super().__init__(name,color)
        self.__model = model
    def getDescripction(self):
        return self.getName()+" "+self.__model+" in "+self.getColor()+" color"
# in method getDescription we are able to call getName, getClor and __model variable
#they are accessible to child class through inheritance
car = Car('honda','red','GT350')
print(car.getDescripction())
print(car.getName())