import math
import numpy as np
from constants import *
from functions import *

HEIGHT = 100
WIDTH_UNITS = 120
# HEIGHT = 30
# WIDTH_UNITS = 30
WIDTH = WIDTH_UNITS*0.5*SQRT3
CENTER_ARR = np.array([MARGIN+WIDTH*0.5, MARGIN+HEIGHT*0.5])

UNIT_1 = [Z_UNIT,  X_UNIT, -Y_UNIT]
UNIT_2 = [X_UNIT, -Y_UNIT,  Z_UNIT]
UNIT_3 = [Y_UNIT, -Z_UNIT, -X_UNIT]

COLOR_1 = [GREEN,   RED, BLUE]
COLOR_2 = [ BLUE, GREEN,  RED]
COLOR_3 = [  RED,  BLUE,GREEN]

OFFSET = [ZERO, ZERO, ZERO, Z_UNIT+X_UNIT, Z_UNIT-Y_UNIT, ZERO]
OFFSET_SECTION = [ZERO, ZERO, ZERO, Z_UNIT, -Y_UNIT, ZERO]

CORNER_DIR = [Z_UNIT+1.5*X_UNIT, X_UNIT-1.5*Y_UNIT, 1.5*Z_UNIT-Y_UNIT]
SECTION_DIR = [Z_UNIT, X_UNIT, -Y_UNIT]

#Rotate 90 degrees
#Z -> X
#X -> -Y
#Y -> -Z

def print_generic_section(rN, colorMod, center, short_length, long_length, fill_opacity = 1):
    file_string = ""
    localCenter = center + + OFFSET_SECTION[rN]*long_length
    path1 = "m", localCenter, "m", ZERO, "l", UNIT_1[rN]*long_length, "l", -UNIT_2[rN]*short_length, "l", -UNIT_1[rN]*long_length, "l",UNIT_2[rN]*short_length
    path2 = "m", localCenter, "m", ZERO, "l", UNIT_1[rN]*long_length, "l", UNIT_2[rN]*short_length, "l", -UNIT_1[rN]*long_length, "l", -UNIT_2[rN]*short_length

    file_string += print_shape_tuple(COLOR_3[(rN+colorMod)%3], path1, fill_opacity, 0)
    file_string += print_shape_tuple(COLOR_1[(rN+colorMod)%3], path2, fill_opacity, 0)

    file_string += print_line(localCenter, localCenter+UNIT_1[rN]*long_length, BLACK, 0.2)
    file_string += print_line(localCenter-UNIT_2[rN]*short_length, localCenter-UNIT_2[rN]*short_length+UNIT_1[rN]*long_length, BLACK, 0.2)
    file_string += print_line(localCenter+UNIT_2[rN]*short_length, localCenter+UNIT_2[rN]*short_length+UNIT_1[rN]*long_length, BLACK, 0.2)

    return file_string

def print_generic_corner2(rN, colorMod, center, short_length, fill_opacity = 1):
    file_string = ""
    short_length = -short_length

    localCenter = center - CORNER_DIR[rN]*(2*short_length)

    path1 = "m", localCenter, "m", -UNIT_2[rN]*short_length, "l", UNIT_1[rN]*(2*short_length), "l", UNIT_2[rN]*4*short_length, "l", -UNIT_3[rN]*short_length, "l", -UNIT_2[rN]*2*short_length, "l", -UNIT_1[rN]*((2*short_length)-short_length)
    path2 = "m", localCenter, "m", UNIT_1[rN]*(2*short_length) -UNIT_2[rN]*short_length , "l", UNIT_3[rN]*short_length, "l", UNIT_2[rN]*((3*short_length)+short_length),  "l", -UNIT_3[rN]*short_length,
    path3 = "m", localCenter, "m", UNIT_2[rN]*short_length, "l", UNIT_1[rN]*((2*short_length)-short_length), "l", -UNIT_2[rN]*short_length, "l", -UNIT_1[rN]*((2*short_length)-short_length)

    file_string += print_shape_tuple(COLOR_1[(rN+colorMod)%3], path1, fill_opacity, 0)
    file_string += print_shape_tuple(COLOR_2[(rN+colorMod)%3], path2, fill_opacity, 0)
    file_string += print_shape_tuple(COLOR_3[(rN+colorMod)%3], path3, fill_opacity, 0)

    p1=localCenter
    p2=p1+UNIT_1[rN]*((2*short_length)-short_length)
    file_string += print_line(p1, p2, BLACK, 0.2)
    p1=localCenter+UNIT_2[rN]*(short_length)
    p2=p1+UNIT_1[rN]*((2*short_length)-short_length)
    file_string += print_line(p1, p2, BLACK, 0.2)
    p1=localCenter-UNIT_2[rN]*(short_length)
    p2=p1+UNIT_1[rN]*((2*short_length))
    file_string += print_line(p1, p2, BLACK, 0.2)
    p1=localCenter+UNIT_1[rN]*((2*short_length)-short_length)
    p2=p1+UNIT_2[rN]*((3*short_length)-short_length)
    file_string += print_line(p1, p2, BLACK, 0.2)
    p1=localCenter+UNIT_1[rN]*((2*short_length))-UNIT_2[rN]*(short_length)
    p2=p1+UNIT_2[rN]*((3*short_length)+short_length)
    file_string += print_line(p1, p2, BLACK, 0.2)
    p1=localCenter+UNIT_1[rN]*((2*short_length))-UNIT_2[rN]*(short_length)
    p2=p1+UNIT_3[rN]*(short_length)
    file_string += print_line(p1, p2, BLACK, 0.2)
    p1=localCenter+UNIT_1[rN]*((2*short_length))-UNIT_2[rN]*(short_length)+UNIT_3[rN]*(short_length)
    p2=p1+UNIT_2[rN]*((3*short_length)+short_length)
    file_string += print_line(p1, p2, BLACK, 0.2)

    file_string += print_line(p1, p2, BLACK, 0.2)

    # file_string += print_line(localCenter, localCenter+UNIT_1[rN]*(2*short_length), YELLOW, 0.5)
    # file_string += print_line(localCenter+UNIT_1[rN]*(2*short_length), localCenter+UNIT_1[rN]*(2*short_length)+UNIT_2[rN]*(2*short_length), YELLOW, 0.5)
    return file_string

def print_generic_corner(rN, colorMod, center, short_length, fill_opacity = 1):
    file_string = ""
    localCenter = center + OFFSET[rN]*(2*short_length)

    path1 = "m", localCenter, "m", ZERO, "l", UNIT_1[rN]*(3*short_length), "l", UNIT_2[rN]*4*short_length, "l", -UNIT_3[rN]*short_length, "l", -UNIT_2[rN]*2*short_length, "l", -UNIT_1[rN]*2*short_length
    path2 = "m", localCenter, "m", UNIT_1[rN]*(2*short_length) + UNIT_2[rN]*short_length , "l", UNIT_2[rN]*2*short_length, "l", -UNIT_3[rN]*short_length, "l", -UNIT_2[rN]*short_length, "l", UNIT_1[rN]*short_length
    path3 = "m", localCenter, "m", ZERO, "l", UNIT_1[rN]*(2*short_length), "l", UNIT_1[rN]*short_length, "l", -UNIT_3[rN]*short_length, "l", -UNIT_1[rN]*(2*short_length)

    file_string += print_shape_tuple(COLOR_1[(rN+colorMod)%3], path1, fill_opacity, 0)
    file_string += print_shape_tuple(COLOR_2[(rN+colorMod)%3], path2, fill_opacity, 0)
    file_string += print_shape_tuple(COLOR_3[(rN+colorMod)%3], path3, fill_opacity, 0)

    p1=localCenter
    p2=p1+UNIT_1[rN]*(2*short_length)
    file_string += print_line(p1, p2, BLACK, 0.2)
    p1=p2
    p2=p1+UNIT_1[rN]*short_length
    file_string += print_line(p1, p2, BLACK, 0.2)
    p1=p2
    p2=p1+UNIT_2[rN]*4*short_length
    file_string += print_line(p1, p2, BLACK, 0.2)
    p1=p2
    p2=p1+-UNIT_3[rN]*short_length
    p1=p2
    p2=p1+-UNIT_2[rN]*2*short_length
    file_string += print_line(p1, p2, BLACK, 0.2)
    p1=p2
    p2=p1+-UNIT_1[rN]*(2*short_length)
    file_string += print_line(p1, p2, BLACK, 0.2)
    p1=localCenter+UNIT_1[rN]*((2*short_length)-short_length) + UNIT_2[rN]*short_length
    p2=p1+UNIT_2[rN]*((2*short_length)-2*short_length)
    file_string += print_line(p1, p2, BLACK, 0.2)
    p1=localCenter-UNIT_2[rN]*short_length
    p2=p1+UNIT_1[rN]*(2*short_length)
    file_string += print_line(p1, p2, BLACK, 0.2)
    p1=p2
    p2=p1+UNIT_3[rN]*short_length
    file_string += print_line(p1, p2, BLACK, 0.2)
    p1=localCenter+UNIT_3[rN]*short_length
    p2=p1+UNIT_2[rN]*short_length
    file_string += print_line(p1, p2, BLACK, 0.2)

    # file_string += print_line(localCenter, localCenter+UNIT_1[rN]*(2*short_length), YELLOW, 0.5)
    # file_string += print_line(localCenter+UNIT_1[rN]*(2*short_length), localCenter+UNIT_1[rN]*(2*short_length)+UNIT_2[rN]*(2*short_length), YELLOW, 0.5)
    return file_string


def print_penrose_triangle_arm(center, short_length, long_length, fill_opacity = 1):
    file_string = ""
    length2 = 10
    file_string += print_generic_section(2, 2, center+Y_UNIT*short_length*0, short_length, -length2, fill_opacity)
    file_string += print_generic_section(1, 1, center+X_UNIT*short_length*5-Y_UNIT*short_length*5, short_length, -length2, fill_opacity)
    file_string += print_generic_section(0, 0, center+X_UNIT*short_length*4+Y_UNIT*short_length*1-Z_UNIT*short_length*1, short_length, -length2, fill_opacity)
    
    file_string += print_penrose_triangle(center, short_length, long_length, fill_opacity)
    return file_string

def print_penrose_triangle(center, short_length, long_length, fill_opacity = 1):
    file_string = ""
    pos=center-Z_UNIT*2*short_length

    file_string += print_generic_corner(0, 0, pos, short_length, fill_opacity)
    pos += CORNER_DIR[0]*2*short_length


    file_string += print_generic_section(1, 1, pos, short_length, long_length, fill_opacity)
    pos += SECTION_DIR[1]*long_length


    file_string += print_generic_corner(1, 1, pos, short_length, fill_opacity)
    pos += CORNER_DIR[1]*2*short_length

    file_string += print_generic_section(2, 2, pos, short_length, long_length, fill_opacity)
    pos += SECTION_DIR[2]*long_length

    file_string += print_generic_corner(2, 2, pos, short_length, fill_opacity)
    pos += CORNER_DIR[2]*2*short_length

    file_string += print_generic_section(0, 3, pos, short_length, long_length, fill_opacity)
    pos += SECTION_DIR[0]*long_length

    return file_string

def print_penrose_tie(center, short_length, long_length, sidelength = 1, fill_opacity = 1, turn = 0):
    file_string = ""

    a=(0+turn)%3
    b=(1+turn)%3
    c=(2+turn)%3
    pos=center-SECTION_DIR[0]*2*short_length

    file_string += print_generic_corner(a, a, pos, short_length, fill_opacity)
    pos += CORNER_DIR[a]*2*short_length


    file_string += print_generic_section(b, b, pos, short_length, long_length*2+4*short_length, fill_opacity)
    pos += SECTION_DIR[b]*(long_length*2+4*short_length)

    file_string += print_generic_corner2(a, a, pos, short_length, fill_opacity)
    pos += CORNER_DIR[a]*2*short_length

    file_string += print_generic_section(a, a, pos, short_length, long_length, fill_opacity)
    pos += SECTION_DIR[a]*long_length

    file_string += print_generic_corner2(c, c, pos, short_length, fill_opacity)
    pos += CORNER_DIR[c]*2*short_length

    file_string += print_generic_section(c, c, pos, short_length, long_length*2+6*short_length, fill_opacity)
    pos += SECTION_DIR[c]*(long_length*2+6*short_length)

    file_string += print_generic_corner(c, c, pos, short_length, fill_opacity)
    pos += CORNER_DIR[c]*2*short_length

    file_string += print_generic_section(a, a, pos, short_length, long_length, fill_opacity)
    pos += SECTION_DIR[a]*long_length

    return file_string

def pattern_bigTri(center):
    # Pattern of triangles
    shortleng = 1
    longLeng = 30
    opacity = 1
    file_string = ""
    file_string += print_penrose_triangle(center, shortleng, longLeng, opacity)
    file_string += print_penrose_triangle(center-H_UNIT*(30)-Z_UNIT*5, shortleng, longLeng, opacity)
    file_string += print_penrose_triangle(center-H_UNIT*(10)-Z_UNIT*25, shortleng, longLeng, opacity)
    file_string += print_penrose_triangle(center-H_UNIT*(-20)-Z_UNIT*20, shortleng, longLeng, opacity)
    file_string += print_penrose_triangle(center-H_UNIT*(40)-Z_UNIT*30, shortleng, longLeng, opacity)
    file_string += print_penrose_triangle(center-H_UNIT*(20)-Z_UNIT*(-20), shortleng, longLeng, opacity)
    
    longLeng = 0
    file_string += print_penrose_triangle_arm(center+H_UNIT*10-Z_UNIT*15, shortleng, longLeng, opacity)
    file_string += print_penrose_triangle_arm(center-H_UNIT*20-Z_UNIT*20, shortleng, longLeng, opacity)
    file_string += print_penrose_triangle_arm(center-Z_UNIT*40, shortleng, longLeng, opacity)

    longLeng = 10
    file_string += print_penrose_tie(startPlace+H_UNIT*10-Z_UNIT*25, shortleng, longLeng, 1, opacity)
    file_string += print_penrose_tie(startPlace-H_UNIT*7-Z_UNIT*34.5, shortleng, longLeng, 1, opacity, 1)
    file_string += print_penrose_tie(startPlace-H_UNIT*8-Z_UNIT*17, shortleng, longLeng, 1, opacity, 2)
    return file_string


# Designs

file_string = ""
# file_string += print_compass()
# file_string += draw_guidelines(WIDTH_UNITS, HEIGHT)
startPlace = MARGIN_ARR-H_UNIT*(12)

# file_string += print_penrose_triangle_arm(startPlace-Z_UNIT*4, 1, 0, 0.3)


startPlace += -H_UNIT*(53) -Z_UNIT*(27.5)

shortleng = 1
longLeng = 30

file_string += print_circle(startPlace, 0.1, GOLD, "")
# file_string += print_penrose_triangle(startPlace, shortleng, longLeng, 0.3)

longLeng = 10
# file_string += print_circle(startPlace-H_UNIT*20, 0.5, GOLD, "")
# file_string += print_penrose_tie(startPlace-H_UNIT*20, shortleng, longLeng, 1, 0.3)


file_string += pattern_bigTri(startPlace)
# file_string += print_circle(startPlace+H_UNIT*20, 0.1, GOLD, "")
# file_string += print_generic_corner(0, 0, startPlace+H_UNIT*20, shortleng, 0.3)
# file_string += print_circle(startPlace+H_UNIT*30, 0.1, GOLD, "")
# file_string += print_generic_corner2(0, 0, startPlace+H_UNIT*30, shortleng, 0.3)
# for i in range(15):
#     file_string += print_penrose_triangle(startPlace-H_UNIT*6*i, shortleng, longLeng, 0.3)


# file_string += print_generic_section(0, 1, startPlace, 1, -100)



# for j in range(3):
#     pos = CENTER_ARR+H_UNIT*0.5*WIDTH_UNITS-Z_UNIT*5-Z_UNIT*10*j
#     for i in range(3):
#         longLeng = 4
#         file_string += print_circle(pos, 1, WHITE, "")
#         file_string += print_circle(pos+CORNER_DIR[i]*longLeng, 1, BLACK, "")
#         file_string += print_generic_corner(i, j, pos, 1,)

#         file_string += print_circle(pos-H_UNIT*3, 1, WHITE, "")
#         file_string += print_circle(pos-H_UNIT*3+SECTION_DIR[i]*longLeng, 1, BLACK, "")
#         file_string += print_generic_section(i, 0, pos-H_UNIT*3, 1, longLeng)
#         # file_string += print_circle(pos-Z_UNIT*6, 1, WHITE, "")
#         # file_string += print_circle(pos-Z_UNIT*6+CORNER_DIR[i]*5, 1, BLACK, "")
#         # file_string += print_generic_corner2(i, j, pos-Z_UNIT*6, 1,)
#         pos-=H_UNIT*13



write_svg(WIDTH+2*MARGIN, 1*HEIGHT+2*MARGIN, file_string)

