
class Calculator:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def add(self):
        r=self.n1 +self.n2
        return r
    def sub(self):
        r=self.n1 -self.n2
        return r
    def mul(self):
        r=self.n1 *self.n2
        return r
    def div(self):
        r=self.n1 /self.n2
        return r
cal=Calculator(3,5)
res=cal.add()
print(f'{cal.n1} + {cal.n2} = {res}');
res=cal.sub()
print(f'{cal.n1} - {cal.n2} = {res}')
res=cal.mul()
print(f'{cal.n1} * {cal.n2} = {res}')
res=cal.div()
print(f'{cal.n1} / {cal.n2} = {res}')
