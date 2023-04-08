import OpenGL
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
    
    p1 = Point2D([100, 100])
    p1.size = 6.0
    p1.color = [0.0, 0.0, 0.0]

    p2 = Point2D([900, 100])
    p2.size = 6.0

    p3 = Point2D([100, 400])
    p3.size = 6.0 

    p4 = Point2D([900, 400])
    p4.size = 6.0

    drawWireframeRect(p1, p2, p3, p4)

    radius = 50
    center1 = Point2D([300, 100])
    center2 = Point2D([650, 100])

    drawCircleBresenham(center1, radius)
    drawCircleBresenham(center2, radius)

    
    p1.x = 150; p1.y = 200
    p2.x = 250; p2.y = 200
    p3.x = 150; p3.y = 350
    p4.x = 250; p4.y = 350
    drawWireframeRect(p1, p2, p3, p4)

    p1.x = 350; p1.y = 250
    p2.x = 450; p2.y = 250
    p3.x = 350; p3.y = 350
    p4.x = 450; p4.y = 350
    drawWireframeRect(p1, p2, p3, p4)

    p1.x = 550; p1.y = 250
    p2.x = 650; p2.y = 250
    p3.x = 550; p3.y = 350
    p4.x = 650; p4.y = 350
    drawWireframeRect(p1, p2, p3, p4)

    p1.x = 750; p1.y = 250
    p2.x = 850; p2.y = 250
    p3.x = 750; p3.y = 350
    p4.x = 850; p4.y = 350
    drawWireframeRect(p1, p2, p3, p4)

    glutSwapBuffers() 
 
 
def drawPoint(p):
    glColor3f(p.color[0], p.color[1], p.color[2])
    glPointSize(p.size)
    glBegin(GL_POINTS)
    glVertex2f(p.x, p.y)
    glEnd() 


def drawLine(p1, p2):
    glColor3f(p1.color[0], p1.color[1], p1.color[2])
    glLineWidth(p1.size)
    glBegin(GL_LINES)
    glVertex2f(p1.x, p1.y)
    glVertex2f(p2.x, p2.y)
    glEnd() 


def drawWireframeRect(p1, p2, p3, p4): # dikdörtgen çizme
    glColor3f(p1.color[0], p1.color[1], p1.color[2])
    glLineWidth(p1.size)
    glBegin(GL_LINE_LOOP)
    glVertex2f(p1.x, p1.y)
    glVertex2f(p2.x, p2.y)
    
    glVertex2f(p4.x, p4.y)
    glVertex2f(p3.x, p3.y)
    glVertex2f(p1.x, p1.y)
    glEnd() 

def drawLineDDA(p1, p2):
    
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    
    pCount = -1 
    
    if(abs(dx)>abs(dy)):
        pCount = abs(dx)
    else:
        pCount = abs(dy)

    xDelta = float(dx)/float(pCount)
    yDelta = float(dy)/float(pCount)

    current_point = Point2D([p1.x, p1.y])
    nextX = float(current_point.x)
    nextY = float(current_point.y)
    while(pCount>0):
        drawPoint(current_point)
        nextX = nextX + xDelta
        nextY = nextY + yDelta
        current_point.x = int(nextX)
        current_point.y = int(nextY)
        pCount = pCount - 1  


def drawCircleBresenham(c, r):
    x = r; y = 0; error = 0
    first_point = Point2D([x,y])
    drawCirclePoints(first_point, c)

    error1 = 0; error2 = 0
    while (x > y):
        error1 = error + (2*y+1)
        error2 = error + (2*y+1)-(2*x-1)
        if abs(error1) < abs(error2):
            y = y + 1
            error = error1
        else:
            x = x - 1
            y = y + 1
            error = error2
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
    drawLineDDA(p0,p1)
    drawLineDDA(p2,p3)
    drawLineDDA(p4,p6)
    drawLineDDA(p5,p7)

win_width  = 960
win_height = 540    
win_x_coord = 480
win_y_coord = 270
win_name ="Odev 2- Minibus Cizimi"



glutInit()  
glutInitDisplayMode(GLUT_RGBA)  
glutInitWindowPosition(win_x_coord,win_y_coord)  
glutInitWindowSize(win_width,win_height)  
glutCreateWindow(win_name)  
initializeGL() 
glutDisplayFunc(displayGL)  
glutMainLoop() 
