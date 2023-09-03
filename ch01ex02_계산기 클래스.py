#ch01ex02_계산기 클래스.py

class Calculator:
    def __init__(self):
        self.result=0

    def add(self,num):
        self.result+=num
        return self.result

c1=Calculator()
r=c1.add(5)
print(f'+5==>{r}')
r=c1.add(3)
print(f'+3==>{r}')

c2=Calculator()
r=c2.add(8)
print(f'+8==>{r}')
r=c2.add(2)
print(f'+2 ==>{r}')
