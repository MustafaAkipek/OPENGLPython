import OpenGL, math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from Shapes import Point2D

# drawFilledTriangle, findPoints, drawLine, drawPoint fonk kullanılır
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

    p1 = Point2D([200, 100])
    p2 = Point2D([150, 400])
    p3 = Point2D([600, 200])

    drawFilledTriangle(p1,p2,p3) # içi dolu üçgen çizdirir
    glutSwapBuffers() 
 
def drawPoint(p):
    glColor3f(p.color[0], p.color[1], p.color[2])
    glPointSize(p.size)
    glBegin(GL_POINTS)
    glVertex2f(p.x, p.y)
    glEnd() 


def drawLine(p1, p2):
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
        nextX = nextX + xDelta;
        nextY = nextY + yDelta;
        current_point.x = int(nextX)
        current_point.y = int(nextY) 
        pCount = pCount - 1  

def findPoints(p1, p2, plist): # üçgen çizerken kullanılır
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
        nextX = nextX + xDelta;
        nextY = nextY + yDelta;
        current_point.x = int(nextX)
        current_point.y = int(nextY)   
        plist.append(Point2D([current_point.x, current_point.y]))
        pCount = pCount - 1 


def drawFilledTriangle(p1, p2, p3): # üçgen çizen fonk
    findPoints(p1, p2, initialPoints)    
    for order in range(len(initialPoints)):
        cp = initialPoints[order] 
        drawLine(cp, p3)
     

initialPoints = [] 


win_width   = 960
win_height  = 540    
win_x_coord = 480
win_y_coord = 270 


glutInit()  
glutInitDisplayMode(GLUT_RGBA)  
glutInitWindowPosition(win_x_coord,win_y_coord)  
glutInitWindowSize(win_width,win_height)  
glutCreateWindow("Lab2c - Ucgen Doldurma")  
initializeGL() 
glutDisplayFunc(displayGL)  
glutMainLoop() 