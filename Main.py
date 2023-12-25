#  Play pong

import turtle
import winsound


wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor('black')

wn.setup(width=800 , height= 700)
wn.tracer(0)


# paddle a

p_a = turtle.Turtle()
p_a.speed(0)
p_a.shape('square')
p_a.color('white')
p_a.shapesize(stretch_wid= 5 , stretch_len= 1)
p_a.penup()
p_a.goto(-350 , 0)

# paddle b
p_b = turtle.Turtle()
p_b.speed(0)
p_b.shape('square')
p_b.color('white')
p_b.shapesize(stretch_wid= 5 , stretch_len= 1)
p_b.penup()
p_b.goto(350 , 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.color('white')
ball.shape('square')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = -0.25


# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Player A: 0  Player B: 0" , align= 'center' , font=('courier' , 24 , "normal"))

# Score
score_a = 0
score_b = 0

#Function

# paddle a up
def p_a_up():
    y = p_a.ycor()
    y += 20
    p_a.sety(y)

# paddle a down
def p_a_down():
    y = p_a.ycor()
    y -= 20
    p_a.sety(y)

# paddle b up
def p_b_up():
    y = p_b.ycor()
    y += 20
    p_b.sety(y)

# paddle b down
def p_b_down():
    y = p_b.ycor()
    y -= 20
    p_b.sety(y)

# ball



# keyboard binding
wn.listen()
wn.onkeypress(p_a_up, 'w')
wn.onkeypress(p_a_down, 's')

wn.onkeypress(p_b_up, 'Up')
wn.onkeypress(p_b_down, 'Down')




# Main game loop

while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border
    if ball.ycor() > 280:
        ball.sety(280)
        winsound.PlaySound('bounce.wav' , winsound.SND_ASYNC)

        ball.dy *= -1


    if ball.ycor() < -280:
        ball.sety(-280)
        winsound.PlaySound('bounce.wav' , winsound.SND_ASYNC)

        ball.dy *= -1




    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        winsound.PlaySound('bounce.wav' , winsound.SND_ASYNC)


        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a , score_b) ,  align='center', font=('courier', 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        winsound.PlaySound('bounce.wav' , winsound.SND_ASYNC)


        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a , score_b) ,  align='center', font=('courier', 24, "normal"))



    # collisions

    if (ball.xcor() > 340 and ball.xcor() < 350 ) and (ball.xcor() < p_b.xcor() + 40) and ball.ycor() > (p_b.ycor() - 40):
        ball.setx(340)
        winsound.PlaySound('bounce.wav' , winsound.SND_ASYNC)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350 ) and (ball.xcor() < p_a.xcor() + 40) and ball.ycor() > (p_a.ycor() - 40):
        ball.setx(-340)
        winsound.PlaySound('bounce.wav' , winsound.SND_ASYNC)


        ball.dx *= -1





