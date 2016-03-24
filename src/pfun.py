# author jsl
# last updated 20150324
# functions for p

## how to import
## goto p2/src and run ipython
# import pfun
# pfun.main()
## if changes in pfun.py
# pfun.reload()

# >>> start of 1_hello_programming
# glbals
import turtle
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
# >>> start of 4_controlstructure


def lab1():
    giyuk(100)


def main():
    lab1()
