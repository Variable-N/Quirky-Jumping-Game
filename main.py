from turtle import *
import random
window = Screen()
window.title("Jump game")
window.bgcolor(0.0,0.0,0.05)
window.setup(width=1000,height=1000)
window.tracer(0)


# Border
borderL = Turtle()
borderL.speed(0)
borderL.shape("square")
borderL.color("light blue")
borderL.shapesize(stretch_wid=51, stretch_len= 1)
borderL.penup()
borderL.goto(-500,0)

borderR = Turtle()
borderR.speed(0)
borderR.shape("square")
borderR.color("light blue")
borderR.shapesize(stretch_wid=51, stretch_len= 1)
borderR.penup()
borderR.goto(500,0)

borderU = Turtle()
borderU.speed(0)
borderU.shape("square")
borderU.color("light blue")
borderU.shapesize(stretch_wid=1, stretch_len= 51)
borderU.penup()
borderU.goto(0,500)

borderD = Turtle()
borderD.speed(0)
borderD.shape("square")
borderD.color("light blue")
borderD.shapesize(stretch_wid=1, stretch_len= 51)
borderD.penup()
borderD.goto(0,-499)

# Player
player = Turtle()
player.speed(0)
player.shape("circle")
player.color("red")
player.penup()
player.goto(0,100)
player.dx = 0
player.dy = -1

# Grounds

gr = Turtle()
gr.speed = 0
gr.shape("square")
gr.color("white")
gr.shapesize(stretch_wid=1, stretch_len= 10)
gr.penup()
gr.goto(random.randint(-200,200),600)

gr0 = Turtle()
gr0.speed = 0
gr0.shape("square")
gr0.color("white")
gr0.shapesize(stretch_wid=1, stretch_len= 10)
gr0.penup()
gr0.goto(random.randint(-200,200),400)

gr1 = Turtle()
gr1.speed = 0
gr1.shape("square")
gr1.color("white")
gr1.shapesize(stretch_wid=1, stretch_len= 10)
gr1.penup()
gr1.goto(random.randint(-200,200),200)

gr2 = Turtle()
gr2.speed = 0
gr2.shape("square")
gr2.color("white")
gr2.shapesize(stretch_wid=1, stretch_len= 10)
gr2.penup()
gr2.goto(0,0)

gr3 = Turtle()
gr3.speed = 0
gr3.shape("square")
gr3.color("white")
gr3.shapesize(stretch_wid=1, stretch_len= 10)
gr3.penup()
gr3.goto(random.randint(-200,200),-200)

gr4 = Turtle()
gr4.speed = 0
gr4.shape("square")
gr4.color("white")
gr4.shapesize(stretch_wid=1, stretch_len= 10)
gr4.penup()
gr4.goto(random.randint(-200,200),-400)


#Player Movement


def playerLeft():
    player.setx(player.xcor()-20)

def playerRight():
    player.setx(player.xcor()+20)

def playerUp():
    if player.ycor() >225:
        player.sety(475)
    else:
        player.sety(player.ycor()+250)

window.listen()
window.onkeypress(playerLeft, "a")
window.onkeypress(playerRight, "d")
window.onkeypress(playerUp, "space")

#Score system

score = 3
pen = Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,400)
pen.write("You are at level {}".format(score),align = "center", font=("Courier",24,"normal"))

# Restart System

def restart():
    gr.goto(random.randint(-200,200),600)
    gr0.goto(random.randint(-200,200),400)
    gr1.goto(random.randint(-200,200),200)
    gr2.goto(0,0)
    gr3.goto(random.randint(-200,200),-200)
    gr4.goto(random.randint(-200,200),-400)
    player.goto(0,100)





#Main loop
while True:

    #player gravity
    if (player.ycor() < gr0.ycor()+23 and player.ycor() > gr0.ycor()+21 and player.xcor() +12 < gr0.xcor() + 125 and player.xcor() - 12 > gr0.xcor() - 125) or (player.ycor() < gr1.ycor()+23 and player.ycor() > gr1.ycor()+21 and player.xcor() +12 < gr1.xcor() + 125 and player.xcor() - 12 > gr1.xcor() - 125) or (player.ycor() < gr2.ycor()+23 and player.ycor() > gr2.ycor()+21 and player.xcor() +12 < gr2.xcor() + 125 and player.xcor() - 12 > gr2.xcor() - 125) or (player.ycor() < gr3.ycor()+23 and player.ycor() > gr3.ycor()+21 and player.xcor() +12 < gr3.xcor() + 125 and player.xcor() - 12 > gr3.xcor() - 125) or (player.ycor() < gr4.ycor()+23 and player.ycor() > gr4.ycor()+21 and player.xcor() +12 < gr4.xcor() + 125 and player.xcor() - 12 > gr4.xcor() - 125) or (player.ycor() < gr.ycor()+23 and player.ycor() > gr.ycor()+21 and player.xcor() +12 < gr.xcor() + 125 and player.xcor() - 12 > gr.xcor() - 125)  :
        # collision with ground will stop gravity code
        pass
    else:
        # Gravity code
        player.sety(player.ycor() + player.dy)


    #ground gravity
    gr.sety(gr.ycor()-0.1)
    gr0.sety(gr0.ycor()-0.1)
    gr1.sety(gr1.ycor()-0.1)
    gr2.sety(gr2.ycor()-0.1)
    gr3.sety(gr3.ycor()-0.1)
    gr4.sety(gr4.ycor()-0.1)

    #New ground maker code
    if gr.ycor() < -500:
        gr.goto(random.randint(-200,200),700)
        score += 1
        pen.clear()
        pen.write("You are at level {}".format(score),align = "center", font=("Courier",24,"normal"))
    if gr0.ycor() < -500:
        gr0.goto(random.randint(-200,200),700)
        score += 1
        pen.clear()
        pen.write("You are at level {}".format(score),align = "center", font=("Courier",24,"normal"))
    if gr1.ycor() < -500:
        gr1.goto(random.randint(-200,200),700)
        score += 1
        pen.clear()
        pen.write("You are at level {}".format(score),align = "center", font=("Courier",24,"normal"))
    if gr2.ycor() < -500:
        gr2.goto(random.randint(-200,200),700)
        score += 1
        pen.clear()
        pen.write("You are at level {}".format(score),align = "center", font=("Courier",24,"normal"))
    if gr3.ycor() < -500:
        gr3.goto(random.randint(-200,200),700)
        score += 1
        pen.clear()
        pen.write("You are at level {}".format(score),align = "center", font=("Courier",24,"normal"))
    if gr4.ycor() < -500:
        gr4.goto(random.randint(-200,200),700)
        score += 1
        pen.clear()
        pen.write("You are at level {}".format(score),align = "center", font=("Courier",24,"normal"))


    #Restart
    if player.ycor() < -500: 
        score = 3
        pen.clear()
        pen.write("You are at level {}".format(score),align = "center", font=("Courier",24,"normal"))
        restart()

    #Player border limit"
    if player.xcor() > 450:
        player.setx(450)
    if player.xcor() < -450:
        player.setx(-450)

    window.update()