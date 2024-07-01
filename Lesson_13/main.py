class Moving:
    def move(self):
        raise NotImplementedError("This method should be implemented in subclass")


class Animal(Moving):
    def voice(self):
        raise NotImplementedError("This method should be implemented in subclass")


class Transport(Moving):
    def launch(self):
        raise NotImplementedError("This method should be implemented in subclass")


class Duck(Animal):
    def voice(self):
        print('кря')

    def move(self):
        print('duck is moving')


class Tiger(Animal):
    def voice(self):
        print('rrrrrrrrrr')

    def move(self):
        print('Tiger is moving')


class Car(Transport):
    def __init__(self):
        self.status = 'not started'

    def launch(self):
        self.status = 'started'
        print('Car is started')

    def move(self):
        if self.status == 'started':
            print('Car is moving')
        else:
            print("Car is not started, can't move")


duck = Duck()
tiger = Tiger()
car = Car()
duck.voice()
duck.move()
tiger.voice()
tiger.move()
car.move()
car.launch()
car.move()
