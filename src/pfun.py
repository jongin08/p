"""
author jsl
last updated 20150325FRI

collection of function for the lecture

status
-----
    1) possible to use an anonymouse trutle e.g., turtle.fd(100)
    2) reload() -> t1 problem
        * turtle.getturtle() -> now seems ok
        * ???why call setup() twice to run ok
    3) wn.bye -> t1.bye??
    3) gamePlay -> find treasure? -> gold in a rectangle???
        1) scores
            * double scores
                * ??global state: isAlreadyIn
            * big vs small scores
                * ??global scores
            * score history -> sum
            * shapes
                * rectangles, triangles...
        2) file
            * save username, time, scores
            * save shapes to load
                * set difficulty
        3) status bar
        4) menu bar
        5) ondrag -> moveto

how to import
-----
    * go to the directory where *.ipynb is saved
    * run ipython or ipython notebook
        ```
        %cd src
        import pfun
        pfun.setup()
        pfun.lab1()
        ```
    * to write any changes in pfun.py
        ```
        %%writefile pfun.py -a
        ```
    * to update vim when editing pfun.py -> :edit
    * reloading (e.g. add lab5() in the module (pfun.py))
        ```
        pfun.reload()
        pfun.lab5()
        ```
    * docstring
        ```
        import pfun
        dir(pfun)
        help(pfun)
        help(pfun.setup)
        ```

useful ipython commands
-----
    * %load 65-67 -> run history 65-67
    * %load -r 1-10 pfun.py -> run lines 1-10 from pfun.py
    * %history -n 1-10 src/todel.py -> NOTE it is not appending
    * %save -a pfun.py 76-80 -> append history 76-80 to pfun.py
    * %%writefile pfun.py -a -> append current cell to pfun.py
    * %bookmark root -> get_ipython().magic(u'bookmark root')
    * %cd {"/home/jsl"} -> get_ipython().magic(u'cd {"/home/jsl/"}')
    * %cd -b root -> get_ipython().magic(u'cd -b root')
"""
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
    mywd=os.path.dirname(os.path.realpath(__file__))
    plantdir=os.path.join(mywd,'../lib/')
    sys.path.append(mywd)
    myCoords=[ [(100, 100), (200, 200)],[(50, 50), (150, -50)]]
    print "if t1 exists {0}...".format('t1' in vars())
    t1=turtle.getturtle() # 
    wn=turtle.getscreen()


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

# >>> begin 1_2_3_hello_programming
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

# <<< end of 1_2_3_hello_programming
# >>> begin 4_5_controlstructure

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

def drawTriangleWithChar(nTimes,symbol):
    maxTimes=nTimes
    for i in range(1,maxTimes+1):
        print((maxTimes-i)*" "+2*i*symbol)

def computeBMI(height,weight):
    bmi = float(weight / height / height)
    print 'Your BMI is %.2f' % bmi
    if bmi <= 18.5:
        res = 'Underweight'
    elif bmi >= 18.5 and bmi < 23:
        res = 'Normal weight'
    elif bmi >= 23 and bmi < 25:
        res = 'Risk of overweight'
    elif bmi >= 25 and bmi < 30:
        res = "Obese Stage 1"
    elif bmi >= 30 and bmi < 40:
        res = "Obese Stage 2"
    elif bmi >= 40:
        res = "Obese Stage 3"
    else:
        res = "Error"
    return res

def pEuler1():
    sum=0
    for num in range(0,1000,3):
        if not (num % 3 and num % 5): sum+=num
    return sum

def pEuler_19():
    D=[31,28,31,
       30,31,30,
       31,31,30,
       31,30,31]
    d,n=0,0
    for i in range(0,10):
        if (not (1900+i)%4 and (1900+i)%100) or not (1900+i)%400:
            D[1]=29
        else:
            D[1]=28
        for t in D:
            if not (d-1)%7 and i>=1:
                n+=1
            d+=t
            #print n, t, d,not(d-1)%7
    return n

# <<< end of 4_5_controlstructure
# >>> begin 

#@here

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
    xs=min(x1,x2)
    xe=max(x1,x2)
    ys=min(y1,y2)
    ye=max(y1,y2)
    x=point[0]
    y=point[1]
    return (xs <= x <= xe and ys <= y <= ye)

# determine if a point is inside any rectangles
# input:
# 1) point: tuple (or list) (x,y)
# 2) coords: list of list of tuples [(x1,y1),(x2,y2)]
# output: True or False
# usage:
# point=(0, 0)
# coords=[ [(100, 100), (200, 200)],[(50, 50), (150, -50)]]
# isInRectangles(point,coords)
def isInRectangles(point,coords):
    isIn=False
    for coord in coords:
        # return true if in any one of rectangle
        if(isInRectangle(point,coord)):
            print "turtle in ",coord
            isIn=True
            return isIn
    return isIn

def drawSquareWithCoords(coords):
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

def keyup():
    pt=t1.pos()
    print "up",pt
    if(isInRectangles(pt,myCoords)):
        t1.write(pt)
    t1.forward(45)

def keyleft():
    t1.left(45)

def keyright():
    t1.right(45)

def keydown():
    pt=t1.pos()
    print "down",pt
    if(isInRectangles(pt,myCoords)):
        t1.write(pt)
    t1.back(45)

def addKeys():
    wn.onkey(keyup, "Up")
    wn.onkey(keyleft, "Left")
    wn.onkey(keyright, "Right")
    wn.onkey(keydown, "Down")
    wn.onkey(wn.bye, "q") # Register function exit to event key_press "q"

def mousegoto(x,y):
    msg="mouse clicked {0} {1}".format(x,y)
    wn.title(msg)
    t1.setpos(x,y)
    isInRectangles((x,y),myCoords)
    #t1.write(x, y)

def addMouse():
    wn.onclick(mousegoto)  # Wire up a click on the window.

def gamePlay():
    import turtle
    drawSquareWithCoords(myCoords)
    addKeys()
    addMouse()
    # listen to any input
    wn.listen()
    # do loop until exit
    # turtle's mainloop
    turtle.mainloop()

def lab6():
    gamePlay()

def lab5():
    setup()
    drawStar(100)
    turns=20
    size=5
    bigger=15
    angle=90
    t1.home()
    t1.clear()
    makeSwirlSquare(size,bigger,turns,angle)
    makeSwirlSquareAt(size,bigger,turns,angle,(100,100))

def lab5a():
    sel = raw_input('Enter F or C: ')
    temp = raw_input('Enter temperature: ')
    temperature = int(temp)
    result=convertTemperature(sel,temperature)
    print "{0:d}{1:s} --> {2:.2f}".format(temperature,sel,result)

def lab5b():
    marksTmp = raw_input('Enter marks (0~100): ')
    marks = float(marksTmp)
    grade=computeGrade(marks)
    print "You enterd marks {0:.1f} --> grade {1:2s}".format(marks,grade)

def lab5c():
    sel1 = raw_input("You select scissor, rock or paper: ")
    sel2 = raw_input("(S)he selects scissor, rock or paper: ")
    print(rspPlay(sel1, sel2))
    print(rspPlayV1(sel1, sel2))

def lab5d():
    drawTriangleWithChar(8,'#')
    height=1.74
    weight=69
    print computeBMI(height,weight)
    answer=pEuler1()
    print "sum of 3,5 multiples =",answer
    print "p euler 19 =", pEuler_19()

def lab1():
    """
    to test list as a param to setpos()
    """
    t1.setpos([100,100])
    t1.setpos([100,200])
    t1.setpos((200,200))

def main():
    setup()
    lab1()

if __name__=="__main__":
    main()

#@


