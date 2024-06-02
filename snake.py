import time
import turtle
import random

delay = 0.1
#setup screen
wn = turtle.Screen()
wn.title("Snakebites")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("green")
head.penup()
head.goto(0,0)
head.direction = "stop"

#food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0,100)

#body
body = []


#function

def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_right():
    head.direction = "right"

def go_left():
    head.direction = "left"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

    if head.direction == "left" :
        x = head.xcor()
        head.setx(x-20)         

#controls

wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")


#Main game loop
while True:
    wn.update()

    if head.distance(food) < 20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y) 

        #body
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.color("light green")
        new_body.penup()
        body.append(new_body)

    for index in range(len(body)-1,0,-1):
        x=body[index-1].xcor()
        y=body[index-1].ycor()
        body[index].goto(x,y)

    if len(body)>0:
        x=head.xcor()
        y=head.ycor()
        body[0].goto(x,y)    



    move()
    time.sleep(delay)
    
wn.mainloop()
