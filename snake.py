import time
import turtle

delay = 0.1
#setup screen
wn = turtle.Screen()
wn.title("Snakebites")
wn.bgcolor("dark blue")
wn.setup(width=600, height=600)
wn.tracer(0)

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "up"

#function
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

#Main game loop
while True:
    wn.update()
    move()
    time.sleep(delay)


wn.mainloop()