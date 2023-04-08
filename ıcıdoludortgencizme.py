import OpenGL, math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from Shapes import Point2D

# drawFilledQuad, findPoints, drawLine, drawPoint fonk kullanılır 

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
    p2 = Point2D([200, 200])
    p3 = Point2D([600, 100])
    p4 = Point2D([600, 500])

    drawFilledQuad(p1,p2,p3,p4)
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

# alternatif çizgi çizme
""" 
def drawLine(p1, p2):
    glColor3f(p1.color[0], p1.color[1], p1.color[2])
    glLineWidth(p1.size)
    glBegin(GL_LINES)
    glVertex2f(p1.x, p1.y)
    glVertex2f(p2.x, p2.y)
    glEnd() 
"""

def findPoints(p1, p2, plist):
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


def drawFilledQuad(p1, p2, p3, p4): # dörtgen çizmede kullanılır
    findPoints(p1, p2, initialPoints)
    findPoints(p3, p4, endingPoints)      
    if( len(initialPoints)==len(endingPoints)):
        print("Initial and ending points are equal")
        lsize = len(initialPoints)
        for order in range(lsize):
            cp1 = initialPoints[order]
            cp2 = endingPoints[order]
            drawLine(cp1, cp2)
    elif(len(initialPoints)>len(endingPoints)):
        isize = len(initialPoints)
        esize = len(endingPoints)
        for order in range(esize):
            cp1 = initialPoints[order]
            cp2 = endingPoints[order]
            drawLine(cp1, cp2) 
        cp2 = endingPoints[esize-1] 
        for order in range(esize, isize):
            cp1 = initialPoints[order]
            drawLine(cp1, cp2) 
    elif(len(initialPoints)<len(endingPoints)):
        isize = len(initialPoints)
        esize = len(endingPoints)
        for order in range(isize):
            cp1 = initialPoints[order]
            cp2 = endingPoints[order]
            drawLine(cp1, cp2) 
        cp1 = initialPoints[isize-1] 
        for order in range(isize, esize):
            cp2 = endingPoints[order]
            drawLine(cp1, cp2)

# alternatif dikdörtgen çizme
""" 
def drawQuad(p1, p2, p3, p4): 
    glBegin(GL_QUADS)
    glColor3f(p1.color[0], p1.color[1], p1.color[2])
    glVertex2f(p1.x, p1.y) 
    glColor3f(p2.color[0], p2.color[1], p2.color[2])
    glVertex2f(p2.x, p2.y) 
    glColor3f(p4.color[0], p4.color[1], p4.color[2])
    glVertex2f(p4.x, p4.y)
    glColor3f(p3.color[0], p3.color[1], p3.color[2])
    glVertex2f(p3.x, p3.y)
    glEnd() 
"""
win_width   = 960
win_height  = 540    
win_x_coord = 480
win_y_coord = 270 


initialPoints = []
endingPoints = [] 

glutInit()  
glutInitDisplayMode(GLUT_RGBA)  
glutInitWindowPosition(win_x_coord,win_y_coord)  
glutInitWindowSize(win_width,win_height)  
glutCreateWindow("Lab2d - Dortgen Doldurma")  
initializeGL() 
glutDisplayFunc(displayGL)  
glutMainLoop() 