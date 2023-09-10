import turtle as t
import  random

class Racer:
    def __init__(self,tt,y,color):

        self.tt=tt
        self.tt.speed(0)
        self.tt.shape("turtle")
        self.tt_speed=random.randint(2,10)
        self.tt.up()
        self.tt.goto(-250,y)
        self.tt.color(color)
        self.finish=False
    def move(self):
        self.tt.forward(self.tt_speed)
        if self.tt.xcor() > 250:
            self.finish=True

#창 생성
t.setup(600, 400)
t.bgcolor('orange')
#거북이 생성
rt=t.Turtle()
bt=t.Turtle()
gt=t.Turtle()

red_racer=Racer(rt,50,'red')
blue_racer=Racer(bt,-50,'blue')
green_racer=Racer(gt,0,'green')



#이동

while not red_racer.finish and not blue_racer.finish and not green_racer.finish:
#==while red_racer.finish == False and blue_racer.finish == False and green_racer.finish == False:

    red_racer.move()
    blue_racer.move()
    green_racer.move()


t.done()

