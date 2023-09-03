
class Car:
    def __init__(self,car_type='normal',color='white',speed=80,):
        self.car_type=car_type
        self.color=color
        self.speed=speed
        self.dist=0

    def __str__(self):
        return f'Car info:{self.car_type},{self.color},{self.speed}'

    def move_car(self):
        self.dist+=self.speed
        return self.dist
        

class FastCar(Car):
    def __init__(self):
        super().__init__('sport','red',100)

    def __str__(self):
        super_msg=super().__str__()
        return f'FAST CAR {super_msg}'

class TurboCar(Car):
    def __init__(self):
        super().__init__('turbo','black',300)

    def __str__(self):
        super_msg=super().__str__()
        return f'Turbo CAR :{super_msg}'

Car1=Car()
Car2=FastCar()
Car3=TurboCar()

for x in range(10):
    Car1.move_car()
    Car2.move_car()
    Car3.move_car()
    print(f'car1:{Car1.dist},car2:{Car2.dist},car3:{Car3.dist}')

print('-' *50)

print(Car1)
print(Car2)
print(Car3)
print(f'car1:{Car1.dist},car2:{Car2.dist},car3:{Car3.dist}')

