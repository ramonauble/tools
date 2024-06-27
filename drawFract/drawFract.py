#   drawFract
#   uses Turtle to draw fractal patterns based on interpretation of L-systems
#   by rae
#   6-23-24 | 7:10 pm

import turtle as t
from collections import deque
t.home()

axiom = "X"
P_01 = "F+[[X]-X]-F[-FX]+X"
P_02 = "FF"
posStack = deque()  #turtle position stack
output = ""
moveDistance = 32
g = 6
angle = 25
tWidth = 3
tColors = ["#6a4a3a", "#8a604c", "#9a6d59", "#a27560", "#aa7c67",
           "#b58772", "#c1937f", "#ce9f8b", "#d4a794", "#e4baa9",
           "#ecc7b7", "#f1d7cf", "#f7eae7"]
tcIndex = 0

t.hideturtle() #hide turtle
t.colormode(255)
t.bgcolor("#57c2be")
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

for cmd in range(len(axiom)):
    if (axiom[cmd] == "F") or (axiom[cmd] == "f"):
        moveTurt(axiom[cmd], moveDistance/g)
    elif (axiom[cmd] == "+") or (axiom[cmd] == "-"):
        angleTurt(axiom[cmd], angle)
    elif (axiom[cmd] == "["):
        posStack.append((t.xcor(), t.ycor(), t.heading()))
        t.width(t.width() - .25)
        tcIndex += 1
        print(tcIndex)
        t.pencolor(tColors[tcIndex])
    elif (axiom[cmd] == "]"):
        t.pu()
        oldPos = posStack.pop()
        t.setx(oldPos[0])
        t.sety(oldPos[1])
        t.seth(oldPos[2])
        t.pd()
        t.width(t.width() + .25)
        tcIndex -= 1
        print(tcIndex)
        t.pencolor(tColors[tcIndex])
t.update()
    
t.mainloop()