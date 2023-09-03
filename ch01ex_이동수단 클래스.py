#ch01_ex_이동수단 클래서.py
class Vehicle:
    def start(self):
        print("출발")

    def stop(self):
        print("중지")

    def move(self):
        print("이동!")

class Car(Vehicle):
    pass

class Bicycle(Vehicle):
    pass



v1=Vehicle()
v1.start()
v1.move()
v1.stop()

c1=Car()
c1.start()

b1=Bicycle()
b1.move()
