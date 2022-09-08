class Car:
    def speed(self, brand = None):#
        if brand is not None:
            return brand + " is speeding"
        else:
            return ('speed is normal')
obj = Car()
print(obj.speed('honda'))