# functions for p

# start of 1_hello_programming

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

# end of 1_hello_programming

