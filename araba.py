import OpenGL, math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from Shapes import Point2D


def initializeGL():
    glClearColor(1.0, 1.0, 1.0, 0.0)  
    glShadeModel(GL_FLAT)  

def displayGL():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity() 
    glViewport(0, 0, win_width, win_height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, win_width, 0.0, win_height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity() 

    p1 = Point2D([50, 100])
    p2 = Point2D([200, 100])
    drawLine(p1,p2) # x bitiş 200

    p1.x = 250
    r = 50
    drawCircle(p1, r) # x bitiş 300

    p1.x = 300
    p2.x = 650
    drawLine(p1,p2) # x bitiş 650

    p1.x = 700
    r = 50
    drawCircle(p1,r) # x bitiş 750

    p1.x = 750
    p2.x = 875
    drawLine(p1,p2) # x bitiş 875, y bitiş 100

    p1.x = 875
    p1.y = 100
    p2.x = 900
    p2.y = 275
    drawLine(p1,p2) # x bitiş 900, y bitiş 275

    p1.x = 900
    p1.y = 275
    p2.x = 800
    p2.y = 275
    drawLine(p1,p2) # x bitiş 800, y bitiş 275

    p1.x = 800
    p1.y = 275
    p2.x = 700
    p2.y = 150
    drawLine(p1,p2) # x bitiş 700, y bitiş 150

    p1.x = 800
    p1.y = 275
    p2.x = 750
    p2.y = 425
    drawLine(p1,p2) # x bitiş 750, y bitiş 425

    p1.x = 750
    p1.y = 425
    p2.x = 400
    p2.y = 425
    drawLine(p1,p2) # x bitiş 400, y bitiş 425

    p1.x = 400
    p1.y = 425
    p2.x = 325
    p2.y = 275
    drawLine(p1,p2) # x bitiş 325, y bitiş 275

    p1.x = 325
    p1.y = 275
    p2.x = 125
    p2.y = 200
    drawLine(p1,p2) # x bitiş 125, y bitiş 200

    p1.x = 125
    p1.y = 200
    p2.x = 50
    p2.y = 100
    drawLine(p1,p2) # x bitiş 50, y bitiş 100

    p1.x = 325
    p1.y = 275
    p2.x = 375
    p2.y = 100
    drawLine(p1,p2) # x bitiş 375, y bitiş 100

    p1.x = 325
    p1.y = 275
    p2.x = 800
    p2.y = 275
    drawLine(p1,p2) # x bitiş 800, y bitiş 275

    p1.x = 525
    p1.y = 275
    p2.x = 575
    p2.y = 425
    drawLine(p1,p2) # x bitiş 575, y bitiş 425

    p1.x = 525
    p1.y = 275
    p2.x = 475
    p2.y = 100
    drawLine(p1,p2) # x bitiş 475, y bitiş 100

    p1.x = 475
    p1.y = 250
    p2.x = 425
    p2.y = 250
    drawLine(p1,p2) # x bitiş 425, y bitiş 250

    p1.x = 575
    p1.y = 250
    p2.x = 625
    p2.y = 250
    drawLine(p1,p2) # x bitiş 425, y bitiş 250

    p1.x = 250
    p1.y = 100
    r = 25
    drawCircle(p1, r) # x bitiş 300

    p1.x = 700
    p1.y = 100
    r = 25
    drawCircle(p1, r) # x bitiş 300

    glutSwapBuffers() 

def drawPoint(p):
    glColor3f(p.color[0], p.color[1], p.color[2]); 
    glPointSize(p.size)
    glBegin(GL_POINTS); 
    glVertex2f(p.x, p.y); 
    glEnd() 


def drawLine(p1, p2): # çizgi çizme
    dx = p2.x - p1.x; dy = p2.y - p1.y
    pCount = -1 

    if(abs(dx)>abs(dy)):  
        pCount = abs(dx)
    else:  
        pCount = abs(dy)

    xDelta = float(dx)/float(pCount)
    yDelta = float(dy)/float(pCount)

    current_point = Point2D([p1.x, p1.y])
    nextX = float(current_point.x); nextY = float(current_point.y)

    while(pCount>0):
        drawPoint(current_point)
        nextX = nextX + xDelta; nextY = nextY + yDelta
        current_point.x = int(nextX); current_point.y = int(nextY)
        pCount = pCount - 1  
            
def drawCircle(c, r): # çember çizme fonksiyonu
    x = r; y = 0; error = 0 
    first_point = Point2D([x,y])
    drawCirclePoints(first_point, c)
    error1 = 0; error2 = 0
    
    while (x > y):
        error1 = error + (2*y+1); error2 = error + (2*y+1)-(2*x-1)
        if abs(error1) < abs(error2): 
            y = y + 1; error = error1
        else: 
            x = x - 1; y = y + 1; error = error2

        nextPoint = Point2D([x, y])
        drawCirclePoints(nextPoint, c)

def drawCirclePoints(p, c):
    p0=Point2D([(c.x+p.x), (c.y+p.y)]); drawPoint(p0)
    p1=Point2D([(c.x-p.x), (c.y+p.y)]); drawPoint(p1)
    p2=Point2D([(c.x+p.x), (c.y-p.y)]); drawPoint(p2)
    p3=Point2D([(c.x-p.x), (c.y-p.y)]); drawPoint(p3) 
    p4=Point2D([(c.x+p.y), (c.y+p.x)]); drawPoint(p4)
    p5=Point2D([(c.x-p.y), (c.y+p.x)]); drawPoint(p5)
    p6=Point2D([(c.x+p.y), (c.y-p.x)]); drawPoint(p6)
    p7=Point2D([(c.x-p.y), (c.y-p.x)]); drawPoint(p7) 

# pencere boyutu ve koordinatları
win_width  = 960
win_height = 540    
win_x_coord = 480
win_y_coord = 270 
 
glutInit()  
glutInitDisplayMode(GLUT_RGBA)  
glutInitWindowPosition(100,100) # pencerenin başlangıç noktası
glutInitWindowSize(win_width,win_height) # pencere boyutu
glutCreateWindow("Lab1b - DDA Algoritmasi Cizgi Cizme") # pencerenin adı
initializeGL() 
glutDisplayFunc(displayGL)  
glutMainLoop() 
