#거북이 달리기

import turtle as t
import  random

def race():
        red_turtle.forward(red_turtle_speed)
        blue_turtle.forward(blue_turtle_speed)
        green_turtle.forward(green_turtle_speed)
        if red_turtle.xcor() <250 and blue_turtle.xcor() <250 and green_turtle.xcor() <250:

            t.ontimer(race,100)  #0.1초마다 race 함수 실행

t.setup(600,400 )
t.bgcolor('orange')

red_turtle=t.Turtle()
red_turtle.shape("turtle")
red_turtle.speed(0)
red_turtle.color('red')
red_turtle.up()
red_turtle.goto(-250,50)
red_turtle_speed=random.randint(2,20)

green_turtle=t.Turtle()
green_turtle.shape("turtle")
green_turtle.speed(0)
green_turtle.color('green')
green_turtle.up()
green_turtle.goto(-250,0)
green_turtle_speed=random.randint(2,20)


blue_turtle=t.Turtle()
blue_turtle.shape("turtle")
blue_turtle.speed(0)
blue_turtle.color('blue')
blue_turtle.up()
blue_turtle.goto(-250,-50)
blue_turtle_speed=random.randint(2,20)

race()


t.done()
