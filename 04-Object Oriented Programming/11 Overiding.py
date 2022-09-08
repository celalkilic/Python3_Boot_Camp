class Parent1:
    def show(self):
        print('inside parent1')

class Parent2:
    def display(self):
        print('inside parent2')
class Child(Parent1, Parent2):
    def show(self):
        print('inside child from show')
    def display(self):
        print('inside child for display')

obj = Child()
obj.show()
obj.display()