
class Calculator():    # class Calculator
    def __init__(self,n1,n2):
        self.n1=n1 #n1 속성
        self.n2=n2 #n2 속성

    def add(self): #add 메서드(method)
        r=self.n1 +self.n2
        return r

cal=Calculator(3,5) #두 속성(3,5)를 갖는 Calculator 객체를 생성
res=cal.add() #cal 객처의 add 매서드 실행
print(f'{cal.n1} + {cal.n2} = {res}') #3+5=8

#두 속성(5, 8)을 갖는 Calculator 객체 cal2를 생성
cal2=Calculator(5,8)
#cal2의 add() 매서드 결과를 res변수에 대입 후 출력
res=cal2.add()
print(f'{cal2.n1} + {cal2.n2} ={res}')
