#   drawFract
#   uses Turtle to draw fractal patterns based on interpretation of L-systems
#   by rae
#   6-23-24 | 7:10 pm

import turtle as t
import numpy as np
import random as r
from colorsys import hls_to_rgb
from colorsys import rgb_to_hls
from collections import deque
t.home()

axiom = "X"
bgAxiom = "F+F+F+F"
P_01 = "F+[[X]-X]-F[-FX]+X" #X production
P_02 = "FF"                 #F production
posStack = deque()  #turtle position stack
output = ""
moveDistance = 18
g = 7
angle = 22.5
tWidth = 3
tBaseHue = 0
tBaseLit = .35
tBaseSat = 0
#tBaseHue = 21
#tBaseLit = .45
#tBaseSat = .29
tcIndex = 0
tMove = 18

t.hideturtle() #hide turtle
t.colormode(255)
t.bgcolor("#b5e3e0")
rgbColor = hls_to_rgb(tBaseHue, tBaseLit, tBaseSat)
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


#draw background squares
sqrColorRGB = rgb_to_hls(163/255, 220/255, 216/255)
sqrX = -405.5
sqrY = 443.33333333
sqrH = 0
sqrW = 45
sqrDec = 8
sBaseHue = sqrColorRGB[0]
sBaseLit = sqrColorRGB[1]
sBaseSat = sqrColorRGB[2]
sqrStack = deque()                                      #init square pos stack
posStack.append((t.xcor(), t.ycor(), t.heading()))      #record pos
t.pu()                                                  #disengage pen
t.seth(0)                                               #turtle heading due right (0 deg)
sqrColor = hls_to_rgb(sBaseHue, sBaseLit, sBaseSat)
t.pencolor(int(255*sqrColor[0]), int(255*sqrColor[1]), int(255*sqrColor[2]))
t.fillcolor(int(255*sqrColor[0]), int(255*sqrColor[1]), int(255*sqrColor[2]))
print("R: " + str(int(255*sqrColor[0])) + ", G: " + str(int(255*sqrColor[1])) +
       ", B: " + str(int(255*sqrColor[2])))
                                    
#print("X: " + str(t.xcor()) + ", Y: " + str(t.ycor()) + ", H: " + str(t.heading()) + "°")

for layer in range(6):
    t.pu()
    sqrColor = hls_to_rgb(sBaseHue, sBaseLit, sBaseSat)
    t.setx(sqrX - sqrDec*layer)     #starting pos - top left sqr
    t.sety(sqrY - sqrDec*layer)
    t.seth(sqrH)   
    for row in range(13):
        t.pencolor(int(255*sqrColor[0]), int(255*sqrColor[1]), int(255*sqrColor[2]))
        t.fillcolor(int(255*sqrColor[0]), int(255*sqrColor[1]), int(255*sqrColor[2]))
        if (row == 0):
            t.seth(90)                                          #offset for inner squares
        else:
            t.seth(270)                                          #offset for inner squares
        moveTurt("f", (sqrDec*layer)/2)
        t.seth(0)
        moveTurt("f", (sqrDec*layer)/2)
        t.pd()                                              #engage pen
        for col in range (12):
            sqrStack.append((t.xcor(), t.ycor(), t.heading()))
            t.begin_fill()
            for sqr in bgAxiom:
                if (sqr == "F") or (sqr == "f"):
                    moveTurt(sqr, sqrW - (layer*sqrDec))
                elif (sqr == "+") or (sqr == "-"):
                    angleTurt(sqr, 90)
            t.end_fill()
            sqrPos = sqrStack.pop()
            t.setx(sqrPos[0])
            t.sety(sqrPos[1])
            t.seth(sqrPos[2])
            moveTurt("f", (24 + 44.66666667))
        t.pu()                                              #disengage pen
        t.setx(sqrX)
        t.sety(sqrY - (row + 1)*(19.5 + 44.66666667))
    sBaseLit += .033
                                                
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

for cmd in range(len(axiom)):
    if (axiom[cmd] == "F") or (axiom[cmd] == "f"):
        theBoy = .2*r.random()
        rgbColor = hls_to_rgb(min(1, (max(0, ((t.ycor() + 480)/960)))), min(1, max(0, ((t.ycor() + 480)/960)) + theBoy), min(1, max(0, (abs(t.xcor())/420)) + theBoy))
        #print(str(int(min(1, max(0, abs(t.heading()/360)))*255)))
        t.pencolor(int(255*rgbColor[0]), int(255*rgbColor[1]), int(255*rgbColor[2]))
        tPenColor = t.pencolor()
        hslColor = rgb_to_hls(int(255*tPenColor[0]), int(255*tPenColor[1]), int(255*tPenColor[2]))
        #print(hslColor[0])
        moveTurt(axiom[cmd], moveDistance/g)
    elif (axiom[cmd] == "+") or (axiom[cmd] == "-"):
        angleTurt(axiom[cmd], (angle + (1)*r.random()))
    elif (axiom[cmd] == "["):
        posStack.append((t.xcor(), t.ycor(), t.heading()))
        t.width(t.width() - .2166667)
        tcIndex += 1
        tBaseLit += .025
        rgbColor = hls_to_rgb(tBaseHue, tBaseLit, tBaseSat)
        t.pencolor(int(255*rgbColor[0]), int(255*rgbColor[1]), int(255*rgbColor[2]))
    elif (axiom[cmd] == "]"):
        t.pu()
        oldPos = posStack.pop()
        t.setx(oldPos[0])
        t.sety(oldPos[1])
        t.seth(oldPos[2])
        t.pd()
        t.width(t.width() + .2166667)
        tcIndex -= 1
        tBaseLit -= .025
        rgbColor = hls_to_rgb(tBaseHue, tBaseLit, tBaseSat)
        t.pencolor(int(255*rgbColor[0]), int(255*rgbColor[1]), int(255*rgbColor[2])) 
t.update()

    
t.mainloop()