#Super keyword
#It allows us to call a method from the parent class
class Vehicle:
    def start(self):
        print('startigng engine')
    def stop(self):
        print('stoppong engine')
class Honda(Vehicle):
    def say(self):
        super().start()
        print('we can write extra code between two super')
        super().stop()

honda = Honda()
honda.say()
