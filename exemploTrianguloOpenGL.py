from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def display():
    glClear(GL_COLOR_BUFFER_BIT)
###
#GL_POINTS , GL_LINES , GL_LINE_STRIP 
#, GL_LINE_LOOP , GL_TRIANGLES , GL_TRIANGLE_STRIP , 
# GL_TRIANGLE_FAN , GL_QUADS , GL_QUAD_STRIP , and GL_POLYGON
###
    glBegin(GL_POLYGON)  # GL_TRIANGLES , GL_QUADS
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.0, 0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(-0.5, 0.0)
    glVertex2f(0.5, 1.0)
    glEnd()

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(400, 400)
    glutCreateWindow("Triangulo")
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
