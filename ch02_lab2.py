class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def intro(self):
        print(f'{self.name}은(는) {self.age} 살입니다.')




p1=Person('김철수',14)
p1.intro()
p2=Person('홍길동',999)
p2.intro()
p3=Person('신성근',14)
p3.intro()
