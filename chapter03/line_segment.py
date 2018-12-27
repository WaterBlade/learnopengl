from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0.0, 200.0, 0.0, 150.0)


def line_segment():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.4, 0.2)
    glBegin(GL_LINES)
    glVertex2i(180, 15)
    glVertex2i(10, 145)
    glEnd()

    glFlush()


if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(50, 100)
    glutInitWindowSize(400, 300)
    glutCreateWindow("OpenGL")

    init()
    glutDisplayFunc(line_segment)
    glutMainLoop()
