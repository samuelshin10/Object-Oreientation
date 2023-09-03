#ch03ex04.py

class  Racer:
    def __init__(self,name,age,speed):
        self.name=name
        self.age=age
        self.speed=speed
        self.dist=0
    def __str__(self):
        return f'선수이름 {self.name}, 나이{self.age}, 속력:{self.speed}'

    def move(self):
        self.dist+=self.speed

r1=Racer('길동',20,10)
r2=Racer('철수',30,7)
r3=Racer('발장',17,15)

print(r1)
print(r2)
print(r3)
print('-'*50)
print()

for _ in range(5):
    for one in [r1,r2,r3]:
        one.move()
        print(f'{one.name}의 이동거리:{one.dist}')
    print('-'* 30)
