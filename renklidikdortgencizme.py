import OpenGL, math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from Shapes import Point2D

def initializeGL():
    glClearColor(1.0, 1.0, 1.0, 0.0)  
    glShadeModel(GL_SMOOTH)  # renkli olmasını sağladı

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
    p2.color=[0.0, 1.0, 0.0]
    p3 = Point2D([600, 200])
    p3.color=[0.0, 0.0, 1.0]
    p4 = Point2D([400, 500])
    p4.color=[1.0, 1.0, 0.0]
    drawQuad(p1,p2,p3,p4)


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


win_width   = 960
win_height  = 540    
win_x_coord = 480
win_y_coord = 270 

 

glutInit()  
glutInitDisplayMode(GLUT_RGBA)  
glutInitWindowPosition(win_x_coord,win_y_coord)  
glutInitWindowSize(win_width,win_height)  
glutCreateWindow("Lab2e - OpenGL Fonksiyonlari ile Cizim ve Doldurma")  
initializeGL() 
glutDisplayFunc(displayGL)  
glutMainLoop() 