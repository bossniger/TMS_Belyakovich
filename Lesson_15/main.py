import random


class House:
    def __init__(self):
        pass


class Car:
    def __init__(self):
        pass


class Person:
    def __init__(self):
        self.bank_account = 0
        self.house = None
        self.car = None

    def work(self):
        earnings = random.randint(5, 10)
        self.bank_account += earnings
        print(f"I worked and earned {earnings} coins.")

    def buy_car(self):
        if self.bank_account >= 40:
            self.bank_account -= 40
            self.car = Car()
            print("Bought a car!")
        else:
            print("Not enough money to buy a car.")

    def buy_house(self):
        if self.bank_account >= 100 and self.car is not None:
            self.bank_account -= 100
            self.house = House()
            print("Bought a house!")
        else:
            print("Not enough money to buy a house.")

    def sell_car(self):
        if self.car:
            self.bank_account += 40
            self.car = None
            print("Sold the car.")
        else:
            print("No car to sale.")

    def sell_house(self):
        if self.house:
            self.bank_account += 100
            self.house = None
            print("Sold the house.")
        else:
            print("No car to sale.")


# flow-line
person = Person()
while person.bank_account <= 40:
    person.work()
print(person.bank_account)
person.buy_house()
person.buy_car()
while person.bank_account <= 100:
    person.work()
print(person.bank_account)
person.buy_house()
person.sell_house()
person.sell_car()
