import turtle

pencere=turtle.Screen()
pencere.title("PinPong")
pencere.bgcolor("green")
pencere.setup(width=800,height=600)
pencere.tracer(0)

raket_A=turtle.Turtle()
raket_A.speed(0)
raket_A.shape("square")
raket_A.color("Orange")
raket_A.penup()
raket_A.goto(-350,0)
raket_A.shapesize(5,1)

raket_B=turtle.Turtle()
raket_B.speed(0)
raket_B.shape("square")
raket_B.color("Orange")
raket_B.penup()
raket_B.goto(350,0)
raket_B.shapesize(5,1)

ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("purple")
ball.penup()
ball.dx=0.7
ball.dy=0.7

yazi=turtle.Turtle()
yazi.speed(0)
yazi.color("yellow")
yazi.penup()
yazi.goto(0,260)
yazi.write("OYUNCU A:0    OYUNCU B:0",align="center",font="courier 24 bold")
yazi.hideturtle()

puan_A=0
puan_B=0


def raket_A_up():
    y=raket_A.ycor()
    y=y+20
    raket_A.sety(y)

def raket_A_down():
    y=raket_A.ycor()
    y=y-20
    raket_A.sety(y)

def raket_B_up():
    y=raket_B.ycor()
    y=y+20
    raket_B.sety(y)

def raket_B_down():
    y=raket_B.ycor()
    y=y-20
    raket_B.sety(y)
pencere.listen()
pencere.onkeypress(raket_A_up,"w")
pencere.onkeypress(raket_A_down,"s")
pencere.onkeypress(raket_B_up,"Up")
pencere.onkeypress(raket_B_down,"Down")

while True:
    pencere.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if ball.ycor()>290 or ball.ycor()<-290:
        ball.dy=ball.dy*-1
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx=ball.dx*-1
        puan_A = puan_A + 1
        yazi.clear()
        yazi.write("Oyuncu A:{}   Oyuncu B:{}".format(puan_A, puan_B), align='center', font=('Courier', 24, 'bold'))
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx=ball.dx*-1
        puan_B = puan_B + 1
        yazi.clear()
        yazi.write("Oyuncu A:{}   Oyuncu B:{}".format(puan_A, puan_B), align='center', font=('Courier', 24, 'bold'))
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<raket_B.ycor()+60 and ball.ycor()>raket_B.ycor()-60):
        ball.setx(340)
        ball.dx = ball.dx * -1
    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<raket_A.ycor()+60 and ball.ycor()>raket_A.ycor()-60):
        ball.setx(-340)
        ball.dx = ball.dx * -1
