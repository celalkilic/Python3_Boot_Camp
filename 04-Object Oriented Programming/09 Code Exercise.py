class Person:
    #defining constructor
    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge
    #defining class methods
    def showName(self):
        print(self.name)

    def showAge(self):
        print(self.age)

class Student:

    def __init__(self, studentId):
        self.Id = studentId

    def getId(self):
        return self.Id
class Resident(Person,Student):
    def __init__(self,name,age,id):
        Person.__init__(self,name,age)
        Student.__init__(self,id)

resident1 = Resident('celal',21,'1002')
resident1.showName()
resident1.showAge()
print(resident1.getId())