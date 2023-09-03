
class Vehicle:
    def __init__(self,brand,model):  
        self.brand=brand
        self.model=model

    def __str__(self):
        return f'Brand: {self.brand}, Model:{self.model}'

    def move(self):
        print (f'{self.model} Drive!')

class Boat(Vehicle):
    def move (self):
        print(f'{self.model} Sail!')

class Plane(Vehicle):

    def move (self):
        print(f'{self.model} Fly!')

car1=Vehicle('현대','제네시스')
boat1=Boat('대우','유람선')
plane1=Plane('보잉','747')

for one in (car1,boat1,plane1):
    print(one)
    one.move()
    
    
    
