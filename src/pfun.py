# functions for p

# >>> start of 1_hello_programming

import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

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
    # 위치와 방향의 저장
    oldpos=t1.pos()
    oldhead=t1.heading()
    giyuk(size)
    # 이동 궤적 지우기
    t1.penup()
    # 저장한 위치와 방향을 사용하기
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
# >>> start of 4_controlstructure

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


