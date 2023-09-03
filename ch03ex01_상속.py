#ch0301_상속.py
#계산기

class Calculator:
    def __init__(self): #생성자
        self.result=0

    def add(self,num):
        self.result +=num
        return self.result

    def sub(self,num):
        self.result -=num
        return self.result

    def mul(self,num):
        self.result *=num
        return self.result

    def div(self,num):
        self.result /=num
        return self.result

class ExpertCalculator(Calculator):
    def pow(self,num):
        self.result**=num
        return self.result

    def div(self,num):
        if num==0:
            print('0으로 나눌 수 없습니다.')
            return self.result
        else:
            self.result  /=num
            return self.result

cal1=Calculator()
r=cal1.add(5)
print(f'+5 ==>{r}')
r=cal1.sub(2)
print(f'-2 ==>{r}')
r=cal1.mul(5)
print(f'*5 ==>{r}')
r=cal1.div(2)
print(f'/2 ==>{r}')

print('-'*50)
cal2=ExpertCalculator()
print(f'+5==>{cal2.add(5)}')
print(f'-3==>{cal2.sub(3)}')
print(f'*2==>{cal2.mul(2)}')
print(f'**3==>{cal2.pow(3)}')
print(f'/2==>{cal2.div(0)}')
