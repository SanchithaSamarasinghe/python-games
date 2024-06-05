import time
import turtle
import random
import os



# Get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the image file
image_path = os.path.join(current_dir, "greens-apple4.gif")

# Ensure the file exists
if not os.path.exists(image_path):
    print(f"Error: The file {image_path} does not exist.")
else:
    delay = 0.1
    # Setup screen
    wn = turtle.Screen()
    wn.title("Snakebites")
    wn.bgcolor("black")
    wn.setup(width=600, height=600)
    wn.tracer(0)

    # Register the image shape
    wn.addshape(image_path)

    # Snake head
    head = turtle.Turtle()
    head.speed(0)
    head.shape("circle")
    head.color("green")
    head.penup()
    head.goto(0, 0)
    head.direction = "stop"

    # Food
    food = turtle.Turtle()
    food.speed(0)
    food.shape(image_path)  # Use the image path as the shape
    food.penup()
    food.goto(0, 100)

    # Body
    body = []

    # Functions
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
            head.sety(y + 20)
        if head.direction == "down":
            y = head.ycor()
            head.sety(y - 20)
        if head.direction == "right":
            x = head.xcor()
            head.setx(x + 20)
        if head.direction == "left":
            x = head.xcor()
            head.setx(x - 20)

    # Controls
    wn.listen()
    wn.onkeypress(go_up, "w")
    wn.onkeypress(go_down, "s")
    wn.onkeypress(go_left, "a")
    wn.onkeypress(go_right, "d")

    # Main game loop
    while True:
        wn.update()

        if head.distance(food) < 20:
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x, y)

            # Add new body segment
            new_body = turtle.Turtle()
            new_body.speed(0)
            new_body.shape("square")
            new_body.color("light green")
            new_body.penup()
            body.append(new_body)

        for index in range(len(body) - 1, 0, -1):
            x = body[index - 1].xcor()
            y = body[index - 1].ycor()
            body[index].goto(x, y)

        if len(body) > 0:
            x = head.xcor()
            y = head.ycor()
            body[0].goto(x, y)

        move()
        time.sleep(delay)

    wn.mainloop()
