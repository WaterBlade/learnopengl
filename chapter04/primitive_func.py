from OpenGL.GL import (glClearColor, glMatrixMode, GL_PROJECTION,
                       glClear, GL_COLOR_BUFFER_BIT, glBegin, GL_POINTS,
                       glVertex2i, glVertex2iv, glVertex3f, glEnd,
                       GL_LINE_LOOP, glFlush, GL_POLYGON)
from OpenGL.GLU import (gluOrtho2D)
from OpenGL.GLUT import (glutInit, glutInitWindowPosition, glutInitDisplayMode,
                         GLUT_SINGLE, GLUT_RGB, glutInitWindowSize,
                         glutCreateWindow, glutDisplayFunc, glutMainLoop)
from typing import List


def vector(end, start):
    if len(end) > 1:
        return [end[0] - start[0], end[1] - start[1]]


def cross_product(vec1, vec2):
    return [0, 0, vec1[0]*vec2[1] - vec1[1]*vec2[0]]


def identify_concave(pts: list)->bool:
    sign = cross_product(vector(pts[2], pts[1]), vector(pts[1], pts[0]))
    for i in range(2, len(pts) - 2):
        if sign * cross_product(vector(pts[i+2], pts[i+1]), vector(pts[i+1], pts[i]))[2] < 0:
            return False
    return True


def init():
    glClearColor(0, 0, 0, 0.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0.0, 300, 0.0, 300)


def plot_func():
    glClear(GL_COLOR_BUFFER_BIT)
    p1 = [20, 20]
    p2 = [80, 90]
    p3 = [79, 42]
    p4 = [150, 180]
    p5 = [70, 220]

    glBegin(GL_POINTS)
    glVertex2i(50, 100)
    glVertex2i(75, 150)
    glVertex2i(100, 200)

    glVertex2iv([100, 100])

    glVertex3f(78.5, 109.2, -1)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glVertex2iv(p1)
    glVertex2iv(p2)
    glVertex2iv(p3)
    glVertex2iv(p4)
    glVertex2iv(p5)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2i(50, 50)
    glVertex2i(75, 25)
    glVertex2i(125, 25)
    glVertex2i(150, 50)
    glVertex2i(125, 75)
    glVertex2i(75, 75)
    glEnd()

    glFlush()


if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(50, 100)
    glutInitWindowSize(400, 300)
    glutCreateWindow("OpenGL")

    init()
    glutDisplayFunc(plot_func)
    glutMainLoop()
