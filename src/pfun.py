#
# author jsl
# last updated 20150325FRI
#
# functions for p
#
# status: 
# 1) reload() problem??
# 2) gamePlay() seems ok except the 2nd rectangle??
# press 'q' to exit gamePlay()

## how to import
## in the directory where *.ipynb is saved
# import src.pfun as p
# p.main()
## if changes in pfun.py
# p.reload()

# >>> start of 1_hello_programming
# glbals
import turtle
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
    if 'src.pfun' in sys.modules:
        imp.reload(sys.modules['src.pfun'])
    else:
        import src.pfun as p

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

def drawSquareOrTriangle(size,sides,angle):
    t1.home()
    t1.clear()
    for i in range(0,sides):
        t1.forward(size)
        t1.right(angle)

def makeSwirlSquare(size,bigger,turns,sides,angle):
    nBigger=sides-2
    for i in range(0,turns):
        # if not divide
        if(i%nBigger and nBigger >=2):
            size+=bigger
        t1.forward(size)
        t1.right(angle)

def makeSwirlSquareAt(size,bigger,turns,sides,angle,pos):
    t1.penup()
    t1.goto(pos)
    t1.pendown()
    makeSwirlSquare(size,bigger,turns,sides,angle)

def testSwirl():
    # square
    size=10
    bigger=10
    turns=10
    sides=4
    angle=90
    makeSwirlSquare(size,bigger,turns,sides,angle)
    makeSwirlSquareAt(size,bigger,turns,sides,angle,(100,100))

#--->> tmp
myCoords=[ [(100, 100), (200, 200)],[(50, 50), (150, -50)]]
# determine if a point is inside a triangle
# input:
# 1) point: tuple (or list) (x,y)
# 2) coord: list of tuples [(x1,y1),(x2,y2)]
# output: True or False
# usage:
# point=(0, 0)
# coord=[(100, 100), (200, 200)]
# isInRectangle(point,coord)
def isInRectangle(point,coord):
    x1=coord[0][0]
    x2=coord[1][0]
    y1=coord[0][1]
    y2=coord[1][1]
    x=point[0]
    y=point[1]
    return (x1 <= x <= x2 and y1 <= y <= y2)

# determine if a point is inside any triangle
# input:
# 1) point: tuple (or list) (x,y)
# 2) coords: list of list of tuples [(x1,y1),(x2,y2)]
# output: True or False
# usage:
# point=(0, 0)
# coords=[ [(100, 100), (200, 200)],[(50, 50), (150, -50)]]
# isInRectangles(point,coords)
def isInRectangles(point,coords=myCoords):
    isIn=False
    for coord in coords:
        # return true if in any one of rectangle
        if(isInRectangle(point,coord)):
            isIn=True
            return isIn
    return isIn

def drawSquareWithCoords(coords=myCoords):
    for coord in coords:
        x1=coord[0][0]
        x2=coord[1][0]
        y1=coord[0][1]
        y2=coord[1][1]
        t1.penup()
        t1.setpos((x1,y1))
        t1.pendown()
        t1.setpos((x2,y1))
        t1.setpos((x2,y2))
        t1.setpos((x1,y2))
        t1.setpos((x1,y1))

def t1up():
    pt=t1.pos()
    print "up",pt
    if(isInRectangles(pt)):
        t1.write(pt)
    t1.forward(45)

def t1left():
    t1.left(45)

def t1right():
    t1.right(45)

def t1down():
    pt=t1.pos()
    print "down",pt
    if(isInRectangles(pt)):
        t1.write(pt)
    t1.back(45)

def bindKeys():
    wn.onkey(t1up, "Up")
    wn.onkey(t1left, "Left")
    wn.onkey(t1right, "Right")
    wn.onkey(t1down, "Down")
    wn.onkey(wn.bye, "q") # Register function exit to event key_press "q"

def gamePlay():
    drawSquareWithCoords()
    bindKeys()
    # listen to any input
    wn.listen()
    # do loop until exit
    # turtle's mainloop
    turtle.mainloop()

#<<--- tmp

def lab1():
    testSwirl()

def main():
    lab1()

