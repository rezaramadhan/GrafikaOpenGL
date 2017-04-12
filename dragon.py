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

def draw_legs():
    vertices = [(386,481), (392,455), (404,471)]
    color = [255,255,255]
    draw_polygon(vertices,color)

    vertices = [(399,455), (402,488), (415,464)]
    color = [255,255,255]
    draw_polygon(vertices,color)

    vertices = [(405,451), (409,447), (418,458)]
    color = [255,255,255]
    draw_polygon(vertices,color)

    vertices = [(441,448), (447,443), (459,458)]
    color = [255,255,255]
    draw_polygon(vertices,color)


    vertices = [(452,443),(458,436), (470,452)]
    color = [255,255,255]
    draw_polygon(vertices,color)

    vertices = [(356,444),(357,435), (365,450), (365,445)]
    color = [255,255,255]
    draw_polygon(vertices,color)

    vertices = [(356,434),(357,430), (364,439)]
    color = [255,255,255]
    draw_polygon(vertices,color)


    vertices = [(268,458),(282,455), (4282,467)]
    color = [255,255,255]
    draw_polygon(vertices,color)

    vertices = [(283,455),(291,451), (300,466)]
    color = [255,255,255]
    draw_polygon(vertices,color)

    vertices = [(294,451),(302,446), (308,461)]
    color = [255,255,255]
    draw_polygon(vertices,color)

    vertices = [(266,457),(302,446), (292,436), (256, 445)]
    color = [202,30,37]
    draw_polygon(vertices,color)

    vertices = [(266,457),(247,455), (246,440), (269, 428), (285, 439)]
    color = [235,27,39]
    draw_polygon(vertices,color)

    vertices = [(246, 440),(238,384), (243, 358), (270, 342), (287, 361), (269,428)]
    color = [207,34,40]
    draw_polygon(vertices,color)

    vertices = [(204, 434), (246, 440), (226,449)]
    color = [150,31,32]
    draw_polygon(vertices,color)

    vertices = [(204, 434), (212, 391), (239,384), (246,440)]
    color = [176,29,35]
    draw_polygon(vertices,color)

    vertices = [(212, 391), (243, 359), (239,384)]
    color = [153,30,32]
    draw_polygon(vertices,color)

    vertices = [(440, 449), (417, 448), (422,431), (440,411), (450, 430), (464, 433), (459, 439), (446, 432), (438,439)]
    color = [147,20,26]
    draw_polygon(vertices,color)

    vertices = [(212, 391), (446, 441), (438,439)]
    color = [149,17,16]
    draw_polygon(vertices,color)

    vertices = [(425, 443), (458, 435), (447,432), (442,438)]
    color = [149,17,16]
    draw_polygon(vertices,color)

    vertices = [(417, 448), (401, 434), (409,328), (442, 329), (440, 412)]
    color = [149,26,28]
    draw_polygon(vertices,color)

    vertices = [(409, 329), (414, 324), (437,297), (446, 263), (454, 296), (442, 329)]
    color = [155,10,19]
    draw_polygon(vertices,color)

    vertices = [(364, 447), (346, 438), (337,446)]
    color = [159,31,39]
    draw_polygon(vertices,color)

    vertices = [(354, 444), (356, 435), (349,438)]
    color = [159,31,39]
    draw_polygon(vertices,color)

    vertices = [(356, 434), (356, 430), (347,432)]
    color = [159,31,39]
    draw_polygon(vertices,color)

    vertices = [(337, 446), (323, 445), (334,425), (350, 431), (437, 432), (350, 437), (349, 438)]
    color = [156,33,26]

    vertices = [(323, 445), (306, 417), (334,425)]
    color = [138,21,22]
    draw_polygon(vertices,color)

    vertices = [(306, 417), (334,425), (321, 401)]
    color = [144,26,32]
    draw_polygon(vertices,color)

    vertices = [(334,425), (321, 401), (339, 387),(350, 372), (360, 417), (335, 424)]
    color = [174,28,35]
    draw_polygon(vertices,color)

    vertices = [(385, 481), (391,455), (386, 450), (378, 451)]
    color = [175,45,47]
    draw_polygon(vertices,color)

    vertices = [(395, 455), (403,449), (389, 447), (388, 452)]
    color = [175,45,47]
    draw_polygon(vertices,color)

    vertices = [(405, 450), (409,446), (406, 441), (396, 440), (395, 446)]
    color = [175,45,47]
    draw_polygon(vertices,color)

    vertices = [(378, 451), (364,459), (366, 444), (385, 442), (392, 429), (396, 441), (389, 447), (391, 445), (386, 450)]
    color = [193,26,33]
    draw_polygon(vertices,color)

    vertices = [(366, 444), (336,306), (385, 337), (389, 362), (385, 442)]
    color = [198,23,30]
    draw_polygon(vertices,color)

    vertices = [(203, 432), (213,390), (138, 436)]
    color = [180,188,177]
    draw_polygon(vertices,color)

    vertices = [(268, 425), (286,361), (328, 328), (338, 316), (351, 370), (339, 387), (321, 399)]
    color = [0xb9,0xb5,0xac]
    draw_polygon(vertices,color)

def draw_body():
    vertices = [(90, 466), (40,467), (16, 455), (26, 430), (116, 390), (69, 425),(136, 437), (50, 447)]
    color = [227,30,39]
    draw_polygon(vertices,color)

    vertices = [(116, 390), (69, 425),(136, 437)]
    color = [198,33,39]
    draw_polygon(vertices,color)

    vertices = [(116, 390),(136, 437), (212,390)]
    color = [214,30,39]
    draw_polygon(vertices,color)

    vertices = [(116, 390), (212,390), (269, 341), (197, 352)]
    color = [188,22,22]
    draw_polygon(vertices,color)

    vertices = [(197, 352), (268, 341), (256, 307)]
    color = [182,31,27]
    draw_polygon(vertices,color)

    vertices = [(268, 341), (256, 307), (282, 275), (285, 364)]
    color = [223,30,34]
    draw_polygon(vertices,color)

    vertices = [(282, 275), (285, 364), (339, 313), (324, 279)]
    color = [200,33,40]
    draw_polygon(vertices,color)

    vertices = [(337, 305), (384, 337), (397, 304), (385, 243), (346, 233), (325, 263), (324, 279)]
    color = [208,32,37]
    draw_polygon(vertices,color)

    vertices = [(282, 275), (325, 278), (324, 279), (346, 233), (343, 219), (319, 198)]
    color = [210,26,34]
    draw_polygon(vertices,color)

    vertices = [(319, 198), (343, 219), (398, 216), (356, 135)]
    color = [193,32,37]
    draw_polygon(vertices,color)

    vertices = [(319, 198), (356, 135), (328, 162)]
    color = [134,14,21]
    draw_polygon(vertices,color)

    vertices = [(356, 135),(398, 216), (394, 143)]
    color = [188,18,26]
    draw_polygon(vertices,color)

def draw_chest():
    vertices = [(385, 340),
    (415,324),
    (436,300),
    (395,287),
    (397,305)
    ]
    color = [0xd1,0xd2,0xcc]
    draw_polygon(vertices,color)

    vertices = [
    (436,300),
    (395,287),
    (384,248),
    (400,215)
    ]
    color = [0xc3,0xb3,0xbb]
    draw_polygon(vertices,color)

    vertices = [
    (436,300),
    (400,215),
    (425,205),
    (450,250)
    ]
    color = [0xd3,0xd0,0xd1]
    draw_polygon(vertices,color)

    vertices = [
    (400,215),
    (425,205),
    (418,170),
    (426,144),
    (392,147),
    ]
    color = [0xd3,0xd0,0xd1]
    draw_polygon(vertices,color)

def draw_head():
    vertices = [(295,49),(331,74),(335,61)]
    color = [242,232,230]
    draw_polygon(vertices,color)

    vertices = [(331,74),(335,61),(384,70),(392,93)]
    color = [240,240,240]
    draw_polygon(vertices,color)

    vertices = [(384,70),(392,93),(432,107),(406,75)]
    color = [246,222,235]
    draw_polygon(vertices,color)

    vertices = [(356,50),(384,70),(438,85)]
    color = [187,173,172]
    draw_polygon(vertices,color)

    vertices = [(425,108),(436,109),(428,111)]
    color = [233,223,222]
    draw_polygon(vertices,color)

    vertices = [(484,105),(470,116),(471,146)]
    color = [233,223,222]
    draw_polygon(vertices,color)

    vertices = [(426,145),(464,159),(435,168)]
    color = [233,223,222]
    draw_polygon(vertices,color)

    vertices = [(464,159),(449,172),(459,172)]
    color = [215,190,193]
    draw_polygon(vertices,color)

    vertices = [(464,159),(455,181),(469,171),(474,162),(473,155)]
    color = [209,201,198]
    draw_polygon(vertices,color)

    vertices = [(406,76),(432,106),(472,115),(439,84)]
    color = [204,20,30]
    draw_polygon(vertices,color)

    vertices = [(472,115),(439,84),(454,76),(507,56),(482,105)]
    color = [172,8,9]
    draw_polygon(vertices,color)

    vertices = [(483,101),(506,56),(556,52),(525,66)]
    color = [162,12,14]
    draw_polygon(vertices,color)

    vertices = [(431,106),(470,116),(470,150),(442,126)]
    color = [206,26,35]
    draw_polygon(vertices,color)

    vertices = [(464,120),(469,125),(470,126),(464,123)]
    color = [39,5,7]
    draw_polygon(vertices,color)

    vertices = [(470,150),(442,126),(426,145),(463,160)]
    color = [201,32,39]
    draw_polygon(vertices,color)

    vertices = [(442,126),(426,145),(407,119)]
    color = [182,33,37]
    draw_polygon(vertices,color)

    vertices = [(431,106),(442,126),(407,119),(392,93)]
    color = [210,25,33]
    draw_polygon(vertices,color)

    vertices = [(407,109),(426,145),(392,144),(376,127)]
    color = [201,22,26]
    draw_polygon(vertices,color)

    vertices = [(392,93),(407,119),(381,111)]
    color = [171,35,35]
    draw_polygon(vertices,color)

    vertices = [(381,111),(407,119),(376,126)]
    color = [206,29,37]
    draw_polygon(vertices,color)

    vertices = [(392,93),(380,101),(357,133),(361,142)]
    color = [184,32,29]
    draw_polygon(vertices,color)


def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
    refresh2d(width, height)

    # draw polygon
    draw_wing()
    draw_wing_bone()
    draw_legs()
    draw_body()
    draw_head()
    draw_chest()

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
