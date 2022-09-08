#to create a constructor we will use __init__ method is implicitly called as soon as an object of a class is instantiated
class Person():
    #__init__constructor
    def __init__(self,name):
        self.name = name

    #method
    def say_hi(self):
        print("hello, my name is ", self.name)

#use constructor
p1 = Person('celal')
p2 = Person('Robert')
p3 = Person('can')
# usage of constructor
p1.say_hi()
p2.say_hi()
p3.say_hi()