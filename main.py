import turtle
import random

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

# Create the score system.
scoreA = 0
scoreB = 0

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
def move_paddle_a_up():
    global paddle_a_up
    paddle_a_up = True

# Stop paddle A from moving up.
def stop_paddle_a_up():
  global paddle_a_up
  paddle_a_up = False
    
# Move paddle A function
def move_paddle_a_down(): # on Keypress
  global paddle_a_down
  paddle_a_down = True

# Stop paddle A from moving down.
def stop_paddle_a_down(): # On key release.
  global paddle_a_down
  paddle_a_down = False

# Stop paddle B from moving up.
def stop_paddle_b_up():
  global paddle_b_up
  paddle_b_up = False
  
# Move paddle B function
def move_paddle_b_up():
  global paddle_b_up
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
screen.onkeypress(move_paddle_a_up, "w")
screen.onkeyrelease(stop_paddle_a_up, "w")

screen.onkeypress(move_paddle_a_down, "s")
screen.onkeyrelease(stop_paddle_a_down, "s")

# Setup keyboard bindings (Other side)
screen.onkeypress(move_paddle_b_up, "Up")
screen.onkeyrelease(stop_paddle_b_up, "Up")

screen.onkeypress(move_paddle_b_down, "Down")
screen.onkeyrelease(stop_paddle_b_down, "Down")

screen.listen()
bg_squares = []
for i in range(10):
  square = turtle.Turtle()
  square.speed(0)
  square.shape("square")
  square.color("black")
  square.penup()
  square.goto(random.randint(-300, 300), random.randint(-300, 300))
  square.sqSize = random.randint(1, 7)
  square.dx = random.uniform(0.15, 0.55)
  square.dy = random.uniform(0.15, 0.55)
  square.shapesize(square.sqSize, square.sqSize)
  bg_squares.append(square)
  
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
ball.dx = 0.30
ball.dy = 0.30

# While loops (gameloops)
while True:
  screen.update()
  ball.setx(ball.xcor() + ball.dx)
  ball.sety(ball.ycor() + ball.dy)
  
  # Border checking
  if ball.ycor() > HEIGHT / 3 or  ball.ycor() < -HEIGHT / 3:
    ball.dy *= -1
    
  if ball.xcor() > WIDTH / 2:
    ball.goto(0, 0)
    ball.dx *= -1
    scoreA += 1
    pen.clear()
    pen.write("player A: {} player B: {}".format(scoreA, scoreB, align="center", font=("Courier", 16, "normal")))
    
  if ball.xcor() < -WIDTH / 2 or ball.xcor() > WIDTH / 2:
    ball.goto(0, 0)
    ball.dx *= -1
    scoreB += 1
    pen.clear()
    pen.left(90)
    pen.goto(0, HEIGHT / 3)
    pen.write("Player A: {} Player B: {}".format(scoreA, scoreB), align="center", font = ("Courier", 24, "bold"))
    pen.right(90)
    for i in range(50):
      pen.pendown()
      pen.forward(10)
      pen.penup()
      pen.forward(10)
      pen.hideturtle()
    pen.write("player A: {} player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 16, "normal"))
    
  if (ball.xcor() > paddle_b.xcor()- 10 and ball.xcor() < paddle_b.xcor() + 10) and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() - 60):
      ball.setx(paddle_b.xcor() + 10)
      ball.dx *= -1
    
  if (ball.xcor() > paddle_a.xcor()- 10 and ball.xcor() < paddle_a.xcor() + 10) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() - 60):
    ball.setx(paddle_a.xcor() + 10)
    ball.dx *= -1
  if paddle_a_up == True:
    y = paddle_a.ycor()
    y += 2
    paddle_a.sety(y)

  if paddle_a_down == True:
    y = paddle_a.ycor()
    y -= 2
    paddle_a.sety(y)

  if paddle_b_up == True:
    y = paddle_b.ycor()
    y += 2
    paddle_b.sety(y)
  if paddle_b_down == True:
    y = paddle_b.ycor()
    y -= 2
    paddle_b.sety(y)

    # Update the screen
  if paddle_a.ycor() < HEIGHT / 3:
    paddle_a.sety(HEIGHT / 3)
  if paddle_a.ycor() > - HEIGHT / 3:
    paddle_a.sety(-HEIGHT / 3)
    # Between paddle A and B for Height.
  if paddle_b.ycor() < HEIGHT / 3:
    paddle_b.sety(HEIGHT / 3)