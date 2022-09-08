class Dog():
    #variable(attributes)
    species = 'mammal'
    #constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age
    #method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    def speak(self, sound):
        return '{} says {}'.format(self.name, sound)

d1 = Dog('masa', 20)
d2 = Dog('yasa', 15)
d3 = Dog('pasa', 12)
print(d1.description())
print(d1.speak("howww"))