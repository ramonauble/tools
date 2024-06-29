#   drawFract
#   uses Turtle to draw fractal patterns based on interpretation of L-systems
#   by rae
#   6-23-24 | 7:10 pm

import turtle as t
import numpy as np
import random as r
from collections import deque
t.home()

axiom = "X"
bgAxiom = "F+F+F+F"
P_01 = "F+[[X]-X]-F[-FX]+X" #X production
P_02 = "FF"                 #F production
posStack = deque()  #turtle position stack
output = ""
moveDistance = 16
g = 7
angle = 20
tWidth = 3.2
tColors = ["#6a4a3a", "#8a604c", "#9a6d59", "#a27560", "#aa7c67",
           "#b58772", "#c1937f", "#ce9f8b", "#d4a794", "#e4baa9",
           "#ecc7b7", "#f1d7cf", "#f7eae7", "#f9eeec", "#f9eeec"]
tcIndex = 0


t.hideturtle() #hide turtle
t.colormode(255)
t.bgcolor("#daf1f0")
t.color(tColors[tcIndex])
t.pd() #pen down
t.speed("fastest")  #fastest
t.setx(80)
t.sety(-480)
t.seth(90)
t.width(tWidth)
t.clear() #clear screen
t.tracer(0, 0)


def moveTurt(a, d):
    if (a == "F"):
        t.forward(d)
    elif (a == "f"):
        t.pu() #pen up
        t.forward(d)
        t.pd() #pen down

def angleTurt(a, d):
    if (a == "+"):
        #add d to turtle angle (clockwise rotation - degrees)
        t.right(d)
    elif (a == "-"):
        #subtract d from turtle angle (counter-clockwise rotation - degrees)
        t.left(d)

sqrStack = deque()

#draw background squares
posStack.append((t.xcor(), t.ycor(), t.heading()))      #record pos
t.pu()                                                  #disengage pen
t.setx(-418)                                            #top left corner ||
t.sety(392.5)                                           #                \/
t.seth(0)                                               #turtle heading due right (0 deg)
t.pencolor("#b5e3e0")                                  #pen color for bg squares
#t.pencolor("#000000")                                   #pen color for bg squares


#starting pos
moveTurt("F", 12.5)
angleTurt("+", 90)
moveTurt("F", 12.5)
t.seth(0)
t.pd()                                              #engage pen

for row in range(12):
    for col in range (12):
        sqrStack.append((t.xcor(), t.ycor(), t.heading()))
        for sqr in bgAxiom:
            if (sqr == "F") or (sqr == "f"):
                moveTurt(sqr, 45)
            elif (sqr == "+") or (sqr == "-"):
                angleTurt(sqr, 90)
        sqrPos = sqrStack.pop()
        t.setx(sqrPos[0])
        t.sety(sqrPos[1])
        t.seth(sqrPos[2])
        moveTurt("f", (24 + 44.66666667))
    t.pu()                                            #disengage pen
    t.setx(-418 + 12.5)
    t.sety(392.5 - (row + 1)*(19.5 + 44.66666667) - 12.5)
    t.seth(0)
    t.pd()                                            #engage pen
t.update()

t.pu()
oldPos = posStack.pop()
t.setx(oldPos[0])
t.sety(oldPos[1])
t.seth(oldPos[2])
t.pd()

for generation in range (g):
    output = ""
    for command in range(len(axiom)):
        if axiom[command] == "X":
            output = output + P_01
        elif axiom[command] == "F":
            output = output + P_02
        else:
            output = output + axiom[command] #unity production
    axiom = output

#input("Press any key when ready: ")

t.pencolor(tColors[tcIndex])
for cmd in range(len(axiom)):
    if (axiom[cmd] == "F") or (axiom[cmd] == "f"):
        moveTurt(axiom[cmd], moveDistance/g)
    elif (axiom[cmd] == "+") or (axiom[cmd] == "-"):
        angleTurt(axiom[cmd], (angle + (.2/(tcIndex + 1))*r.random()))
    elif (axiom[cmd] == "["):
        posStack.append((t.xcor(), t.ycor(), t.heading()))
        t.width(t.width() - .2)
        tcIndex += 1
        t.pencolor(tColors[tcIndex])
    elif (axiom[cmd] == "]"):
        t.pu()
        oldPos = posStack.pop()
        t.setx(oldPos[0])
        t.sety(oldPos[1])
        t.seth(oldPos[2])
        t.pd()
        t.width(t.width() + .2)
        tcIndex -= 1
        t.pencolor(tColors[tcIndex])
t.update()
    
t.mainloop()