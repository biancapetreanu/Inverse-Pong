import turtle

window = turtle.Screen()
window.title("Inverse Pong")
window.bgcolor("black")
window.setup(height=500, width=900)
window.tracer(0)



def border_drawer(z, w, x, y):
    border = turtle.Turtle()
    border.speed(0)
    border.shape("square")
    border.color("red")
    border.shapesize(stretch_wid=z, stretch_len=w)
    border.penup()
    border.goto(x, y)


def paddle_drawer(y):
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=1, stretch_len=6)
    paddle.penup()
    paddle.goto(0, y)
    return paddle


def ball_drawer():
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    return ball


def first_paddle_left():
    x = a.xcor()
    x -= 20
    a.setx(x)


def first_paddle_right():
    x = a.xcor()
    x += 20
    a.setx(x)


def second_paddle_left():
    x = b.xcor()
    x -= 20
    b.setx(x)


def second_paddle_right():
    x = b.xcor()
    x += 20
    b.setx(x)


border_drawer(1, 44, 0, 240)
border_drawer(1, 44, 0, -240)
border_drawer(25, 1, 430, 0)
border_drawer(25, 1, -440, 0)
a = paddle_drawer(210)
b = paddle_drawer(-210)
c = ball_drawer()

window.listen()
window.onkeypress(first_paddle_left, "a")
window.onkeypress(first_paddle_right, "d")
window.onkeypress(second_paddle_left, "Left")
window.onkeypress(second_paddle_right, "Right")

c.dx = 0.2
c.dy = 0.2

while True:
    window.update()

    c.setx(c.xcor()+c.dx)
    c.sety(c.ycor()+c.dy)

    if c.xcor() > 430:
        c.setx(430)
        c.dx *= -1
    elif c.xcor() < -440:
        c.setx(-440)
        c.dx *= -1
    if c.ycor() > 240 or c.ycor() < -240:
        c.goto(0, 0)
        c.dx *= -1

    if (160 < c.ycor() < 170) and (a.xcor() + 50 > c.xcor() > a.xcor() - 50):
        c.sety(160)
        c.dy *= -1
    if (-160 > c.ycor() > -170) and (b.xcor() + 50 > c.xcor() > b.xcor() - 50):
        c.sety(-160)
        c.dy *= -1
