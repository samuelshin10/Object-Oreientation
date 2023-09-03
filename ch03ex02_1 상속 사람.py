#ch03ex02_1 상속 사람

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def __str__(self):
        return f'{self.name}은{self.age}살입니다.'
    

    def intro(self):
        print(f'이름:{self.name}')
        print(f'나이:{self.age}')

class Student(Person):

    def intro(self):
        super().intro()
        print(f'직업:학생')
class BizMan(Person):
    
    def intro(self):
        super().intro()
        print(f'직업:회사원')

p1=Person('임꺽정',999)
st1=Student('김영희',15)
b1=BizMan('나퇴근',38)

p1.intro()
print('-' * 50)
st1.intro()
print('-' * 50)
b1.intro()
print('-' * 50)


print(p1)
print(st1)
print(b1)

