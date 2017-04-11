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

def draw_wing():
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

    vertices = [(187,50),
    (83,163),
    (141,144)]
    color = [0xce,0x14,0x17]
    draw_polygon(vertices,color)

    vertices = [(79,398),
    (141,144),
    (186,176),
    (150,237),
    (121,345),
    ]
    color = [0xdf,0x1a,0x23]
    draw_polygon(vertices,color)

    vertices = [(233,97),
    (141,144),
    (186,176),
    ]
    color = [0xc8,0x21,0x28]
    draw_polygon(vertices,color)

    vertices = [(200,66),
    (141,144),
    (233,97),
    ]
    color = [0xdd,0x20,0x26]
    draw_polygon(vertices,color)

    vertices = [(200,66),
    (262,20),
    (233,97),
    ]
    color = [0xbc,0x20,0x23]
    draw_polygon(vertices,color)

    vertices = [(300,35),
    (262,20),
    (233,97),
    ]
    color = [0xcd,0x22,0x28]
    draw_polygon(vertices,color)

    vertices = [(300,35),
    (262,20),
    (358,20),
    ]
    color = [0xbd,0x14,0x16]
    draw_polygon(vertices,color)

    vertices = [(200,66),
    (141,144),
    (187,50),
    ]
    color = [0xd2,0x18,0x21]
    draw_polygon(vertices,color)

    vertices = [(200,66),
    (262,20),
    (187,50),
    ]
    color = [0xdd,0x20,0x26]
    draw_polygon(vertices,color)

def draw_wing_bone():
    vertices = [(233,97),
    (239,127),
    (186,176),
    ]
    color = [0x93,0x16,0x18]
    draw_polygon(vertices,color)

    vertices = [(253,162),
    (239,127),
    (186,176),
    ]
    color = [0x86,0x11,0x18]
    draw_polygon(vertices,color)

    vertices = [(253,162),
    (186,176),
    (241,220),
    (318,198),
    # (283,)
    ]
    color = [0x96,0x18,0x1b]
    draw_polygon(vertices,color)

    vertices = [(241,220),
    (141,267),
    (186,176),
    ]
    color = [0xa6,0x1e,0x22]
    draw_polygon(vertices,color)

    vertices = [(241,220),
    (141,267),
    (194,282),
    ]
    color = [0xa1,0x0c,0x0e]
    draw_polygon(vertices,color)

    vertices = [(241,220),
    (280,274),
    (194,282),
    ]
    color = [0x97,0x16,0x1a]
    draw_polygon(vertices,color)

    vertices = [(121,344),
    (141,267),
    (194,282),
    ]
    color = [0x85,0x12,0x0e]
    draw_polygon(vertices,color)

    vertices = [(121,344),
    (170,333),
    (194,282),
    ]
    color = [0xa1,0x11,0x1a]
    draw_polygon(vertices,color)

    vertices = [(280,274),
    (252,311),
    (170,333),
    (194,282),
    ]
    color = [0x96,0x13,0x1d]
    draw_polygon(vertices,color)

    vertices = [(193,354),
    (252,311),
    (170,333),
    ]
    color = [0x8b,0x1b,0x21]
    draw_polygon(vertices,color)

    vertices = [(280,274),
    (318,198),
    (285,216)
    ]
    color = [0xf5,0xf2,0xec]
    draw_polygon(vertices,color)

    vertices = [(280,274),
    (241,220),
    (285,216)
    ]
    color = [0xa0,0x1c,0x27]
    draw_polygon(vertices,color)

    vertices = [(241,220),
    (318,198),
    (285,216)
    ]
    color = [0x94,0x1b,0x1c]
    draw_polygon(vertices,color)

def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
    refresh2d(width, height)

    # draw polygon
    draw_wing()
    draw_wing_bone()
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
