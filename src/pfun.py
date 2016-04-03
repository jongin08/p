"""
author jsl
last updated 20150325FRI

collection of function for the lecture

"""
# >>> start of 1_hello_programming
# globals
global myhome
global mywd
global plantdir
global wn
global t1
global myCoords

def setup():
    global t1
    global wn
    global myhome
    global mywd
    global plantdir
    global myCoords

    import sys
    import os
    import turtle
    myhome=os.path.expanduser('~')
    mywd=os.getcwd() # runs from the dir where ipynb is
    plantdir=os.path.join(mywd,'lib/')
    sys.path.append(os.path.join(mywd,'src'))

    myCoords=[ [(100, 100), (200, 200)],[(50, 50), (150, -50)]]
    if 'wn' in dir():
        del wn
    if 't1' in dir():
        del t1
    wn=turtle.Screen()
    t1=turtle.Turtle()

# input: none
# output: none
# usage: sfun.reload()
def reload():
    import imp
    import sys
    if 'pfun' in sys.modules:
        imp.reload(sys.modules['pfun'])
    else:
        import pfun

def giyuk(size):
    t1.fd(size)
    t1.right(90)
    t1.fd(size)

def nieun(size):
    t1.right(90)
    t1.fd(size)
    t1.left(90)
    t1.fd(size)

def mieum(size):
    giyuk(size)
    nieun(size)

def mieumPos(size):
    # save old position and heading
    oldpos=t1.pos()
    oldhead=t1.heading()
    giyuk(size)
    # move without drawing
    t1.penup()
    # restore old settings
    t1.setpos(oldpos)
    t1.setheading(oldhead)
    t1.pendown()
    nieun(size)

def giyukAt(size,at):
    t1.penup()
    t1.goto(at,0)
    t1.setheading(0)
    t1.pendown()
    t1.pos()
    t1.write(t1.pos())
    giyuk(size)

# <<< end of 1_2_3_2_3_hello_programming
# >>> start of 4_5_controlstructure

def drawSquare(size):
    for i in range(0,4):
        t1.forward(size)
        t1.right(90)

def drawTriangle(size):
    for i in range(0,3):
        t1.forward(size)
        t1.right(120)

def drawSquareAt(size, pos):
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    for i in range(0,4):
        t1.forward(size)
        t1.right(90)

def drawStar(size):
    for i in range(5):
        t1.forward(size)
        t1.right(144)

def drawStarFill(size, color):
    angle = 144
    t1.fillcolor(color)
    t1.begin_fill()
    for side in range(5):
        t1.forward(size)
        t1.right(angle)
    t1.end_fill()

def drawPolygon(size,tilt,sides):
    t1.right(tilt)
    for i in range(0,sides):
        t1.forward(size)
        t1.right(360/sides)

def drawSquareOrTriangle(size,sides,angle):
    t1.home()
    t1.clear()
    for i in range(0,sides):
        t1.forward(size)
        t1.right(angle)

def makeSwirlSquare(size,bigger,turns,angle):
    nBigger=2
    for i in range(0,turns):
        #if divided by nBigger, make it bigger
        if not i%nBigger:
            size+=bigger
        t1.forward(size)
        t1.right(angle)

def makeSwirlSquareAt(size,bigger,turns,angle,pos):
    t1.penup()
    t1.goto(pos)
    t1.pendown()
    makeSwirlSquare(size,bigger,turns,angle)

def convertTemperature(sel,temperature):
    res=0.0
    if sel=='F':
        res=(temperature-32)*5/9.0
    elif sel=='C':
        res=temperature*9.0/5.0+32
    else:
        print "Error: Enter either F or C!"
    print "{0:d}{1:s} --> {2:.2f}".format(temperature,sel,res)
    return res

def computeGrade(marks):
    if marks>=90 and marks<=100:
        grade='A'
    elif marks>=80 and marks<90:
        grade='B'
    elif marks>=70 and marks<80:
        grade='C'
    elif marks>=60 and marks<70:
        grade='D'
    else:
        grade='F'
    print "You enterd marks {0:.1f} --> grade {1:2s}".format(marks,grade)
    return grade

def rspPlay(u1, u2):
    if u1 == u2:
        res="draw"
    elif u1 == 'scissor':
        if u2 == 'rock':
            res="rock won."
        else:
            res="scissor won."
    elif u1 == 'rock':
        if u2 == 'paper':
            res="paper won."
        else:
            res="rock won."
    elif u1 == 'paper':
        if u2 == 'rock':
            res="paper won."
        else:
            res="scissor won."
    else:
        res="Error: select one of scissor, rock or paper!"
    return res

def rspPlayV1(u1, u2):
    if u1 == u2:
        res="draw"
    elif u1 == 'scissor' and u2 == 'rock':
        res="rock won."
    elif u1 == 'scissor' and u2 == 'paper':
        res="scissor won."
    elif u1 == 'rock' and  u2 == 'paper':
        res="paper won."
    elif u1 == 'rock' and  u2 == 'scissor':
        res="rock won."
    elif u1 == 'paper' and u2 == 'rock':
        res="paper won."
    elif u1 == 'paper' and u2 == 'scissor':
        res="scissor won."
    else:
        res="Error: select one of scissor, rock or paper!"
    return res

def lab1():
    print "hello"

def main():
    setup()
    lab1()

if __name__=="__main__":
    main()

#@



