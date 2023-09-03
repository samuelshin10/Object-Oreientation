#ch03ex02_상속 사람.py

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def intro(self):
        print(f'이름:{self.name}')
        print(f'나이:{self.age}')

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def intro(self):
        print(f'이름:{self.name}')
        print(f'나이:{self.age}')
        print(f'직업: 학생')

class BizMan:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def intro(self):
        print(f'이름:{self.name}')
        print(f'나이:{self.age}')
        print(f'직업:회사원')

p1=Person('홍길동', 9999)
p1.intro()
print('-' *50)

s1=Student('김철수', 14)
s1.intro()
print('-' *50)

b2=BizMan('박출근', 33)
b2.intro()


























