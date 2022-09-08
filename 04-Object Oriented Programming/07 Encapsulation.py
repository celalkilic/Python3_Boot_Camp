#hiding data from the user(sensitive)===account number last four digits *****  ***** ***** 2345

class MyClass():
    def setAge(self,number):
        self.age = number

    def getAge(self):
        return self.age

bob = MyClass()
bob.setAge(40)
print(bob.getAge())

bob.setAge('fourty')
print(bob.getAge())