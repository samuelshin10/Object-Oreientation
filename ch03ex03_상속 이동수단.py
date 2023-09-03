#ch03ex03_상속 이동수단.py

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def __str__(self):
        return f'brand: {self.brand}, model: {self.model}'

    def move(self):
        print(f'{self.model} Drive!')

class Boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def __str__(self):
        return f'brand:{self.brand}, model:{self.model}'

    def move(self):
        print(f'{self.model} Sail!')

class Plane:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def __str__(self):
        return f'brand:{self.brand},model:{self.model}'

    def move(self):
        print(f'{self.model} Fly!')

car1=Car('Tesla','Model X')
boat1=Boat('Ibiza','Touring 20')
plane1=Plane('Boeing','747')

for one in(car1,boat1,plane1):
    print(one)
    one.move()
