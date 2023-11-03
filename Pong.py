import turtle

wn = turtle.Screen()
wn.title("BaoZeDongPong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = .05
ball.dy = -.05

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f'Player 1: {score_a} | Player 2: {score_b}', align='center', font=("Calibri", 24, 'underline'))

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 35
    paddle_a.sety(y)
    return

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 35
    paddle_a.sety(y)
    return

def paddle_b_up():
    y = paddle_b.ycor()
    y += 35
    paddle_b.sety(y)
    return

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 35
    paddle_b.sety(y)
    return
# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_a_up, 'W')
wn.onkeypress(paddle_a_down, 'S')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')
# Main game loop
while True:
    wn.update()
    # Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # Borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= - 1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= - 1
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = -.05
        score_a += 1
        pen.clear()
        pen.write(f'Player 1: {score_a} | Player 2: {score_b}', align='center', font=("Calibri", 24, 'underline'))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = .05
        score_b += 1
        pen.clear()
        pen.write(f'Player 1: {score_a} | Player 2: {score_b}', align='center', font=("Calibri", 24, 'underline'))
    # Paddle Collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1.2
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1.2


