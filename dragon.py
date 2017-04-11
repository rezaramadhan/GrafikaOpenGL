from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0                                             # glut window number
width, height = 1024, 700                               # window size

def draw_polygon(vertices, rgbcolor):
    glColor3ub(rgbcolor[0], rgbcolor[1], rgbcolor[2])
    glBegin(GL_POLYGON)                                  # start drawing a rectangle
    for vertex in vertices:
        glVertex2f(vertex[0], 490 - vertex[1])
    # glVertex2f(x, y)                                   # bottom left point
    # glVertex2f(x + width, y)                           # bottom right point
    # glVertex2f(x + width, y + height)                  # top right point
    # glVertex2f(x + width / 2, y + height * 4/3)
    # glVertex2f(x, y + height)                          # top left point
    glEnd()

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
    refresh2d(width, height)

    # draw polygon
    vertices = [(79,398),
    (83,163),
    (36,380)]
    color = [0xc7,0x20,0x27]
    draw_polygon(vertices,color)
    vertices = [(1,390),
    (83,163),
    (36,380)]
    color = [0xcc,0x14,0x20]
    draw_polygon(vertices,color)
    vertices = [(79,398),
    (83,163),
    (141,144)]
    color = [0xb6,0x1f,0x26]
    draw_polygon(vertices,color)
    vertices = [(79,398),
    (83,163),
    (141,144)]
    color = [0xb6,0x1f,0x26]
    draw_polygon(vertices,color)
    vertices = [(79,398),
    (141,144),
    (186,176),
    (121,345),
    (121,345),
    ]
    color = [0xdf,0x1a,0x23]
    draw_polygon(vertices,color)

    glutSwapBuffers()                                  # important for double buffering


# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow("Naga Indosiar")              # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time
glutMainLoop()                                         # start everything
