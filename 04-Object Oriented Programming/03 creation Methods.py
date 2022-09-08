#first create a class
class MyClass():
#second create a variable
    var = 9
#third create a method
    def firstM(self):
# self represents the instance of a class
# by using the self keyword we access the attributes and methods of python class
        print("hello world")
#forth create an object
obj = MyClass()
print(obj.var)
#call method
obj.firstM()