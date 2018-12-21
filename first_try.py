from OpenGL.GL import (glClear,
                       GL_COLOR_BUFFER_BIT,
                       glPointSize,
                       glColor3f,
                       glBegin,
                       GL_POINTS,
                       glVertex2f,
                       glEnd,
                       glFlush,
                       glClearColor)
from OpenGL.GLUT import (glutInit, glutInitDisplayMode,
                         glutInitWindowPosition,
                         GLUT_SINGLE,
                         GLUT_RGB,
                         glutInitWindowSize,
                         glutCreateWindow,
                         glutDisplayFunc,
                         glutMainLoop)
from OpenGL.GLU import gluOrtho2D
import math
from typing import List, Tuple


def circle(x: float, y: float, r: float, n: int)->Tuple[List[float], List[float]]:
    x_lst = list()  # type: List[float]
    y_lst = list()  # type: List[float]
    for i in range(n):
        x_lst.append(x+r*math.cos(i*2*math.pi/n))
        y_lst.append(y+r*math.sin(i*2*math.pi/n))

    return x_lst, y_lst


def plot():
    glClear(GL_COLOR_BUFFER_BIT)

    glPointSize(3.0)
    glColor3f(1.0, 0.0, 0.0)

    glBegin(GL_POINTS)

    x_lst, y_lst = circle(0, 0, 1, 100)
    for x, y in zip(x_lst, y_lst):
        glVertex2f(x, y)

    glEnd()

    glFlush()


if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(100, 100)
    glutInitWindowSize(900, 600)
    glutCreateWindow(b"Funciont Plotter")
    glutDisplayFunc(plot)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-5.0, 5.0, -5.0, 5.0)
    glutMainLoop()
