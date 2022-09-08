#Multiple Inheritance
class Class1:
    def m(self):
        print('in class 1')

class Class2(Class1):
    def m(self):
        print('in class 2')

class Class3(Class1):
    def m(self):
        print('in class 3')

class Class4(Class2, Class3):
    def m(self):
        print('in class 4')

obj = Class4()
obj.m()
Class2.m(obj)
Class3.m(obj)
Class1.m(obj)