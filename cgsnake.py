import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

wn = turtle.Screen()
wn.title("square annihilation")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# character
head = turtle.Turtle()
head.shape("circle")
head.color("blue")
head.penup()
head.goto(0,0)
head.direction = "stop"

def move():
    if head.direction == "up":
        y=head.ycor()
        head.sety(y + 20)
    
    if head.direction == "down":
        y=head.ycor()
        head.sety(y - 20)
   
    if head.direction == "left":
        x=head.xcor()
        head.setx(x - 20)
    
    if head.direction == "right":
        x=head.xcor()
        head.setx(x + 20)
    if head.direction == "upright":
        x=head.xcor()
        head.setx(x + 12)
        y=head.ycor()
        head.sety(y + 12)

def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"

robot = turtle.Turtle()
robot.shape("triangle")
robot.color("green")
robot.penup()
robot.goto(0,0)

pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score: 0 high score: 0", align="center", font=("courier", 24, "normal"))


bomb = turtle.Turtle()
bomb.shape("square")
bomb.color("red")
bomb.penup()
bomb.goto(0,0)


wn.listen()
wn.onkeypress (go_up, "w")
wn.onkeypress (go_down, "s")
wn.onkeypress (go_left, "a")
wn.onkeypress (go_right, "d")

while True:
    wn.update()
    
    if head.xcor()>290 or head.xcor()<-290 or head.ycor() > 290 or head.ycor() < -290:
        head.goto(0,0)
        head.direction="stop"

    if head.distance(bomb) < 20:
        head.goto(0,0)
        head.direction= "stop"


    if head.distance(robot) < 20: 
        a= random.randint(-290,290)
        b= random.randint(-290,290)
        robot.goto(a,b)
        x= random.randint(-290,290)
        y= random.randint(-290,290)
        bomb.goto(x,y)

        score = score + 1
        if score > high_score:
            score = high_score
        pen.clear()
        pen.write("score: {} high score: {}".format(score, high_score), align="center", font=("courier", 24, "normal"))

        if x==a and y==b:
            x= random.randint(-290,290)
            y= random.randint(-290,290)
        bomb.goto(x,y)  

        score 

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align = "center", font =("Courier", 24, "normal"))

    move()

    time.sleep(delay)


wn.mainloop()