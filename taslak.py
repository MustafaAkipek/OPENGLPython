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
    glLoadIdentity() # kodu yazmaya başladığımız kısım

    p1 = Point2D([100, 100])
    p2 = Point2D([300, 100])
    drawLine(p1,p2)

    glutSwapBuffers() # çizim yapacağımız kodun bitiş kısmı

def drawPoint(p): # nokta çizer
    glColor3f(p.color[0], p.color[1], p.color[2]); 
    glPointSize(p.size)
    glBegin(GL_POINTS); 
    glVertex2f(p.x, p.y); 
    glEnd() 


def drawLine(p1, p2): # çizgi çizer drawPoint' i kullanarak
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
            
def drawCircle(c, r): # çember çizer drawcirclepoint' i kullanarak
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

 
win_width  = 960
win_height = 540    
win_x_coord = 480
win_y_coord = 270 
 
glutInit()  
glutInitDisplayMode(GLUT_RGBA)  
glutInitWindowPosition(win_x_coord,win_y_coord)  # pencere koordinatları
glutInitWindowSize(win_width,win_height)  # pencere boyutu
glutCreateWindow("Lab1b - DDA Algoritmasi Cizgi Cizme")  # pencere ismi
initializeGL() 
glutDisplayFunc(displayGL)  
glutMainLoop() 
