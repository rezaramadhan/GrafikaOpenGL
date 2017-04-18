from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0                                             # glut window number
width, height = 824, 700                               # window size

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

def draw_mountain():
    glBegin(GL_POLYGON)
    glColor3ub(0x67, 0x64, 0xa9);
    glVertex2f(453,254);
    glVertex2f(515,391);
    glVertex2f(619,476);
    glColor3ub(0x3a, 0x38, 0x93);
    glVertex2f(691,297);
    glVertex2f(792,174);
    glVertex2f(820,125);
    glVertex2f(820,10);
    # //blue color
    # glColor3f(0.0,0.0,1.0);
    glVertex2f(100,10);
    glVertex2f(100, 100);
    glEnd()

    glBegin(GL_POLYGON);
    # //red color
    glColor3ub(0x67, 0x64, 0xa9);
    glVertex2f(10,10);
    glVertex2f(75,72);
    glVertex2f(145,159);
    glVertex2f(191,229);
    glVertex2f(204,271);
    glColor3ub(0x24, 0x22, 0x7b);
    glVertex2f(239,248);
    glVertex2f(280,192);
    glVertex2f(352,134);
    glVertex2f(493,10);

    glEnd();

def draw_sky():
    glBegin(GL_POLYGON)
    glColor3ub(0xff, 0xcc, 0x00);
    glVertex2f(0,350);
    glVertex2f(0,700);
    glVertex2f(412,700);
    glColor3ub(0xff, 0xff, 0xff);
    glVertex2f(412,350);
    glEnd();

    glBegin(GL_POLYGON)
    glColor3ub(0xff, 0xcc, 0x00);
    glVertex2f(0,350);
    glVertex2f(0,0);
    glVertex2f(412,0);
    glColor3ub(0xff, 0xff, 0xff);
    glVertex2f(412,350);
    glEnd();

    glBegin(GL_POLYGON)
    glColor3ub(0xff, 0xcc, 0x00);
    glVertex2f(824,350);
    glVertex2f(824,700);
    glVertex2f(412,700);
    glColor3ub(0xff, 0xff, 0xff);
    glVertex2f(412,350);
    glEnd();

    glBegin(GL_POLYGON)
    glColor3ub(0xff, 0xcc, 0x00);
    glVertex2f(824,350);
    glVertex2f(824,0);
    glVertex2f(412,0);
    glColor3ub(0xff, 0xff, 0xff);
    glVertex2f(412,350);
    glEnd();

def draw_rainbow():

	glBegin(GL_POLYGON);
	glColor3ub(0x00, 0xff, 0x00);
	glVertex2f(600,410);
	glVertex2f(450,420);
	glVertex2f(300,410);
	glColor3ub(0x00, 0x00, 0xff);
	glVertex2f(300,440);
	glVertex2f(450,450);
	glVertex2f(600,440);
	glEnd();

	glBegin(GL_POLYGON);
	glColor3ub(0xff, 0xff, 0x00);
	glVertex2f(600,380);
	glVertex2f(450,390);
	glVertex2f(300,380);
	glColor3ub(0x00, 0xff, 0x00);
	glVertex2f(300,410);
	glVertex2f(450,420);
	glVertex2f(600,410);
	glEnd();

	glBegin(GL_POLYGON);
	glColor3ub(0xff, 0x00, 0x00);
	glVertex2f(600,350);
	glVertex2f(450,360);
	glVertex2f(300,350);
	glColor3ub(0xff, 0xff, 0x00);
	glVertex2f(300,380);
	glVertex2f(450,390);
	glVertex2f(600,380);
	glEnd();

   

    



    

def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
    refresh2d(width, height)

    # draw polygon
    draw_sky()
    draw_rainbow()
    draw_mountain()

    glutSwapBuffers()                                  # important for double buffering


# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow("Pemandangan Gunung")              # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time
glutMainLoop()                                         # start everything
