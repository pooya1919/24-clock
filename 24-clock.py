"""
24 Clock
"""
#import library
from turtle import Turtle, Screen
import datetime

#creating window
window = Screen()
#setting window title
window.title("24 Clock")
#setting background color
window.bgcolor("black")
#setting height and width of window
window.setup(width=600, height=500)

#creating outer circle
circle = Turtle()
circle.penup()
circle.pencolor("#452299")
circle.speed(0)
circle.pensize(10)
circle.hideturtle()
circle.goto(0, -200)
circle.pendown()
circle.fillcolor("#51117C")
circle.begin_fill()
circle.circle(200)
circle.end_fill()

#creating hour hand
hHand = Turtle()
hHand.shape("arrow")
hHand.color("white")
hHand.speed(10)
hHand.shapesize(stretch_wid=0.4, stretch_len=9)

#creating minute hand
mHand = Turtle()
mHand.shape("arrow")
mHand.color("white")
mHand.speed(10)
mHand.shapesize(stretch_wid=0.4, stretch_len=12)

#creating second hand
sHand = Turtle()
sHand.shape("arrow")
sHand.color("dark red")
sHand.speed(10)
sHand.shapesize(stretch_wid=0.4, stretch_len=15)

#creating center circle
centerCircle = Turtle()
centerCircle.shape("circle")
#setting color to white
centerCircle.color("white")
centerCircle.shapesize(stretch_wid=0.3, stretch_len=0.3)

# numbers with pen
pen = Turtle()
pen.speed(0)
pen.color("white")

#number 1
pen.penup()
pen.hideturtle()
pen.goto(85, 130)
pen.write("2", align="center", font=("STENCIL", 25, "bold"))

#number 2
pen.penup()
pen.hideturtle()
pen.goto(150, 70)
pen.write("4", align="center", font=("STENCIL", 25, "bold"))

#number 3
pen.penup()
pen.hideturtle()
pen.goto(170, -15)
pen.write("6", align="center", font=("STENCIL", 25, "bold"))

#number 4
pen.penup()
pen.hideturtle()
pen.goto(150, -100)
pen.write("8", align="center", font=("STENCIL", 25, "bold"))

#number 5
pen.penup()
pen.hideturtle()
pen.goto(85, -162.5)
pen.write("10", align="center", font=("STENCIL", 25, "bold"))

#number 6
pen.penup()
pen.hideturtle()
pen.goto(0, -185)
pen.write("12", align="center", font=("STENCIL", 25, "bold"))

#number 7
pen.penup()
pen.hideturtle()
pen.goto(-85, -162.5)
pen.write("14", align="center", font=("STENCIL", 25, "bold"))

#number 8
pen.penup()
pen.hideturtle()
pen.goto(-150, -100)
pen.write("16", align="center", font=("STENCIL", 25, "bold"))

#number 9
pen.penup()
pen.hideturtle()
pen.goto(-170, -15)
pen.write("18", align="center", font=("STENCIL", 25, "bold"))

#number 10
pen.penup()
pen.hideturtle()
pen.goto(-140, 70)
pen.write("20", align="center", font=("STENCIL", 25, "bold"))

#number 11
pen.penup()
pen.hideturtle()
pen.goto(-80, 130)
pen.write("22", align="center", font=("STENCIL", 25, "bold"))

#number 12
pen.penup()
pen.hideturtle()
pen.goto(0, 150)
pen.write("24", align="center", font=("STENCIL", 25, "bold"))

#Defining function to movie hour hand
def movehHand():
   currentHourInternal = datetime.datetime.now().hour
   degree = (currentHourInternal/2 - 15) * -30
   currentMinuteInternal = datetime.datetime.now().minute
   degree = degree + -0.25 * currentMinuteInternal
   hHand.setheading(degree)
   window.ontimer(movehHand, 30000)


#Defining function to minute hand
def movemHand():
    currentMinuteInternal = datetime.datetime.now().minute
    degree = (currentMinuteInternal - 15) * -6
    currentSecondInternal = datetime.datetime.now().second
    degree = degree + (-currentSecondInternal * 0.1)
    mHand.setheading(degree)
    window.ontimer(movemHand, 1000)

#Defining function to second hand
def movesHand():
    currentSecondInternal = datetime.datetime.now().second
    degree = (currentSecondInternal - 15) * -6
    sHand.setheading(degree)
    window.ontimer(movesHand, 1000)

window.ontimer(movehHand, 1)
window.ontimer(movemHand, 1)
window.ontimer(movesHand, 1)
window.exitonclick()
