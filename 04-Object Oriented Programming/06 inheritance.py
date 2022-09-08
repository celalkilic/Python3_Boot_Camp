#parent class
class Pets:
    dogs = []
    def __init__(self,dogs):
        self.dogs = dogs

#Parent class
class Dog():

    # variable(attributes)
    species = 'mammal'

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True
    #methods
    def description(self):
        return self.name, self.age
    def speak(self, sound):
        return "%s says %s"%(self.name, sound)
    def eat(self):
        self.is_hungry = False
class RusselTerrier(Dog):
    def run(self, speed):
        return "%s runs %s "%(self.name, speed)
class BullDog(Dog):
    def run(self, speed):
        return "%s runs %s "%(self.name,speed)

#create an objects
my_dogs = [
    BullDog('mikey',6),
    RusselTerrier('jack',5),
    Dog('larry', 9)
]

my_pets = Pets(my_dogs)
print('i have {} dogs.'.format(len(my_pets.dogs)))
for dog in my_pets.dogs:
    dog.eat()
    print('{} is {}'.format(dog.name, dog.eat))
print('and they are all {}s of course'.format(dog.species))

are_my_dogs_hungry = True
for dog in my_pets.dogs:
    if dog.is_hungry:
        are_my_dogs_hungry = True

if are_my_dogs_hungry:
    print('my dogs are hungry')
else:
    print('my dogs are not hungry')