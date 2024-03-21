import random
import turtle

# SCREEN
screen = turtle.Screen()
screen.title("Pong Game")
screen.bgcolor("black")
WIDTH, HEIGHT = 800, 600
screen.setup(WIDTH, HEIGHT)
screen.tracer(0)

# Create the layout of the game.
pen = turtle.Turtle()
pen.speed(0)
pen.color("White")
pen.penup()
pen.goto(0, HEIGHT / 3)
pen.write("player A = 0 player B = 0", align="center", font=("Courier", 16, "normal"))

pen.goto(0, HEIGHT)
pen.right(90)

# for loops
for i in range(50):
    pen.pendown()
    pen.forward(10)
    pen.penup()
    pen.forward(10)
pen.hideturtle()
# Move paddles via keyboard method
paddle_a_up = False
paddle_a_down = False

paddle_b_up = False
paddle_b_down = False

# Move paddle function
def paddle_a_up():
    global paddle_a_up
    paddle_a_up = True

# Stop paddle A from moving up.
def paddle_a_stop():
  global paddle_a_up
  paddle_a_up = False
    
# Move paddle A function
def move_paddle_a_down():
  global paddle_a_down
  paddle_a_down = True

# Stop paddle A from moving down.
def stop_paddle_a_down():
  global paddle_a_stop
  paddle_a_down = False

# Stop paddle B from moving up.
def stop_paddle_b_up():
  global paddle_b_up
  paddle_b_up = False
  
# Move paddle B function
def move_paddle_b_up():
  global paddle_b
  paddle_b_up = True

# Stop paddle B from moving down.
def stop_paddle_b_down():
  global paddle_b_down
  paddle_b_down = False

# Move paddle B down function
def move_paddle_b_down():
  global paddle_b_down
  paddle_b_down = True
  
# Setup keyboard bindings
screen.onkeypress(paddle_a_up, "w")
screen.onkeyrelease(paddle_a_stop, "w")

screen.onkeypress(paddle_a_down, "s")
screen.onkeyrelease(stop_paddle_a_down, "s")

# Setup keyboard bindings (Other side)
screen.onkeypress(move_paddle_b_up, "Up")
screen.onkeyrelease(stop_paddle_b_up, "Up")

screen.onkeypress(move_paddle_b_down, "Down")
screen.onkeyrelease(stop_paddle_b_down, "Down")

screen.listen()

# Create the paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.penup()
paddle_a.goto(-WIDTH / 2, 0)
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)

# Create the paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("purple")
paddle_b.penup()
paddle_b.goto(WIDTH / 2, 0)
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
# Create the ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()

# Set the balls direction.
ball.dx = 0.15
ball.dy = 0.15

# Create line.

# While loops
while (True):
  if paddle_a_up == True:
    y = paddle_a.ycor()
    y += 2
    paddle_a.sety(y)

  if paddle_a_down == True:
    y = paddle_a.ycor()
    y -= 2
    paddle_a.sety(y)
  screen.update()