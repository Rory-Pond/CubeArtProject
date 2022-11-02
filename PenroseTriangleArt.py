import math
import numpy as np
from constants import *
from functions import *

HEIGHT = 70
WIDTH_UNITS = 70
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

CORNER_DIR = [Z_UNIT+X_UNIT, X_UNIT-Y_UNIT, Z_UNIT-Y_UNIT]
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

def print_generic_corner2(rN, colorMod, center, short_length, long_length, fill_opacity = 1):
    file_string = ""
    long_length = -long_length
    short_length = -short_length

    localCenter = center - CORNER_DIR[rN]*long_length


    path1 = "m", localCenter, "m", -UNIT_2[rN]*short_length, "l", UNIT_1[rN]*long_length, "l", UNIT_2[rN]*(long_length+short_length), "l", -UNIT_3[rN]*short_length, "l", -UNIT_2[rN]*(long_length-short_length), "l", -UNIT_1[rN]*(long_length-short_length)
    path2 = "m", localCenter, "m", UNIT_1[rN]*long_length -UNIT_2[rN]*short_length , "l", UNIT_3[rN]*short_length, "l", UNIT_2[rN]*(long_length+short_length),  "l", -UNIT_3[rN]*short_length,
    path3 = "m", localCenter, "m", UNIT_2[rN]*short_length, "l", UNIT_1[rN]*(long_length-short_length), "l", -UNIT_2[rN]*short_length, "l", -UNIT_1[rN]*(long_length-short_length)

    file_string += print_shape_tuple(COLOR_1[(rN+colorMod)%3], path1, fill_opacity, 0)
    file_string += print_shape_tuple(COLOR_2[(rN+colorMod)%3], path2, fill_opacity, 0)
    file_string += print_shape_tuple(COLOR_3[(rN+colorMod)%3], path3, fill_opacity, 0)

    p1=localCenter
    p2=p1+UNIT_1[rN]*(long_length-short_length)
    file_string += print_line(p1, p2, BLACK, 0.2)
    p1=localCenter+UNIT_2[rN]*(short_length)
    p2=p1+UNIT_1[rN]*(long_length-short_length)
    file_string += print_line(p1, p2, BLACK, 0.2)
    p1=localCenter-UNIT_2[rN]*(short_length)
    p2=p1+UNIT_1[rN]*(long_length)
    file_string += print_line(p1, p2, BLACK, 0.2)
    p1=localCenter+UNIT_1[rN]*(long_length-short_length)
    p2=p1+UNIT_2[rN]*(long_length-short_length)
    file_string += print_line(p1, p2, BLACK, 0.2)
    p1=localCenter+UNIT_1[rN]*(long_length)-UNIT_2[rN]*(short_length)
    p2=p1+UNIT_2[rN]*(long_length+short_length)
    file_string += print_line(p1, p2, BLACK, 0.2)
    p1=localCenter+UNIT_1[rN]*(long_length)-UNIT_2[rN]*(short_length)
    p2=p1+UNIT_3[rN]*(short_length)
    file_string += print_line(p1, p2, BLACK, 0.2)
    p1=localCenter+UNIT_1[rN]*(long_length)-UNIT_2[rN]*(short_length)+UNIT_3[rN]*(short_length)
    p2=p1+UNIT_2[rN]*(long_length+short_length)
    file_string += print_line(p1, p2, BLACK, 0.2)

    file_string += print_line(p1, p2, BLACK, 0.2)

    # file_string += print_line(localCenter, localCenter+UNIT_1[rN]*long_length, YELLOW, 0.5)
    # file_string += print_line(localCenter+UNIT_1[rN]*long_length, localCenter+UNIT_1[rN]*long_length+UNIT_2[rN]*long_length, YELLOW, 0.5)
    return file_string

def print_generic_corner(rN, colorMod, center, short_length, long_length, fill_opacity = 1):
    file_string = ""
    localCenter = center + OFFSET[rN]*long_length

    path1 = "m", localCenter, "m", ZERO, "l", UNIT_1[rN]*long_length, "l", UNIT_1[rN]*short_length, "l", UNIT_2[rN]*(long_length+short_length), "l", -UNIT_3[rN]*short_length, "l", -UNIT_2[rN]*(long_length-short_length), "l", -UNIT_1[rN]*long_length
    path2 = "m", localCenter, "m", UNIT_1[rN]*long_length + UNIT_2[rN]*short_length , "l", UNIT_2[rN]*(long_length-short_length), "l", -UNIT_3[rN]*short_length, "l", -UNIT_2[rN]*(long_length-2*short_length), "l", UNIT_1[rN]*short_length
    path3 = "m", localCenter, "m", ZERO, "l", UNIT_1[rN]*long_length, "l", UNIT_1[rN]*short_length, "l", -UNIT_3[rN]*short_length, "l", -UNIT_1[rN]*long_length

    file_string += print_shape_tuple(COLOR_1[(rN+colorMod)%3], path1, fill_opacity, 0)
    file_string += print_shape_tuple(COLOR_2[(rN+colorMod)%3], path2, fill_opacity, 0)
    file_string += print_shape_tuple(COLOR_3[(rN+colorMod)%3], path3, fill_opacity, 0)

    p1=localCenter
    p2=p1+UNIT_1[rN]*long_length
    file_string += print_line(p1, p2, BLACK, 0.2)
    p1=p2
    p2=p1+UNIT_1[rN]*short_length
    file_string += print_line(p1, p2, BLACK, 0.2)
    p1=p2
    p2=p1+UNIT_2[rN]*(long_length+short_length)
    file_string += print_line(p1, p2, BLACK, 0.2)
    p1=p2
    p2=p1+-UNIT_3[rN]*short_length
    p1=p2
    p2=p1+-UNIT_2[rN]*(long_length-short_length)
    file_string += print_line(p1, p2, BLACK, 0.2)
    p1=p2
    p2=p1+-UNIT_1[rN]*long_length
    file_string += print_line(p1, p2, BLACK, 0.2)
    p1=localCenter+UNIT_1[rN]*(long_length-short_length) + UNIT_2[rN]*short_length
    p2=p1+UNIT_2[rN]*(long_length-2*short_length)
    file_string += print_line(p1, p2, BLACK, 0.2)
    p1=localCenter-UNIT_2[rN]*short_length
    p2=p1+UNIT_1[rN]*long_length
    file_string += print_line(p1, p2, BLACK, 0.2)
    p1=p2
    p2=p1+UNIT_3[rN]*short_length
    file_string += print_line(p1, p2, BLACK, 0.2)

    # file_string += print_line(localCenter, localCenter+UNIT_1[rN]*long_length, YELLOW, 0.5)
    # file_string += print_line(localCenter+UNIT_1[rN]*long_length, localCenter+UNIT_1[rN]*long_length+UNIT_2[rN]*long_length, YELLOW, 0.5)
    return file_string

def print_penrose_triangle(center, short_length, long_length, sidelength = 1, fill_opacity = 1):
    file_string = ""
    pos=center-Z_UNIT*long_length

    file_string += print_generic_corner(0, 0, pos, short_length, long_length, fill_opacity)
    pos += CORNER_DIR[0]*long_length

    for i in range(sidelength):
        file_string += print_generic_section(1, 1, pos, short_length, long_length, fill_opacity)
        pos += SECTION_DIR[1]*long_length


    file_string += print_generic_corner(1, 1, pos, short_length, long_length, fill_opacity)
    pos += CORNER_DIR[1]*long_length

    for i in range(sidelength):
        file_string += print_generic_section(2, 2, pos, short_length, long_length, fill_opacity)
        pos += SECTION_DIR[2]*long_length

    file_string += print_generic_corner(2, 2, pos, short_length, long_length, fill_opacity)
    pos += CORNER_DIR[2]*long_length

    for i in range(sidelength):
        file_string += print_generic_section(0, 3, pos, short_length, long_length, fill_opacity)
        pos += SECTION_DIR[0]*long_length

    return file_string

def print_penrose_tie(center, short_length, long_length, sidelength = 1, fill_opacity = 1):
    file_string = ""
    pos=center-Z_UNIT*long_length

    file_string += print_generic_corner(0, 0, pos, short_length, long_length, fill_opacity)
    pos += CORNER_DIR[0]*long_length
    
    for i in range(2+2*sidelength):
        file_string += print_generic_section(1, 1, pos, short_length, long_length, fill_opacity)
        pos += SECTION_DIR[1]*long_length

    file_string += print_generic_corner2(0, 3, pos, short_length, long_length, fill_opacity)
    pos += CORNER_DIR[0]*long_length

    for i in range(sidelength):
        file_string += print_generic_section(0, 0, pos, short_length, long_length, fill_opacity)
        pos += SECTION_DIR[0]*long_length

    file_string += print_generic_corner2(2, 2, pos, short_length, long_length, fill_opacity)
    pos += CORNER_DIR[2]*long_length

    for i in range(2+2*sidelength):
        file_string += print_generic_section(2, 2, pos, short_length, long_length, fill_opacity)
        pos += SECTION_DIR[2]*long_length

    file_string += print_generic_corner(2, 2, pos, short_length, long_length, fill_opacity)
    pos += CORNER_DIR[2]*long_length

    for i in range(sidelength):
        file_string += print_generic_section(0, 0, pos, short_length, long_length, fill_opacity)
        pos += SECTION_DIR[0]*long_length

    return file_string


# Designs

svg_string = ""
svg_string += print_compass()
svg_string += draw_guidelines(WIDTH_UNITS, HEIGHT)
startPlace = MARGIN_ARR-H_UNIT*(12+15)-Z_UNIT*(7.5)

shortleng = 1
longLeng = 2
repeatNum = 20

svg_string += print_penrose_triangle(startPlace, shortleng, longLeng, repeatNum, 0.3)
for i in range(15):
    svg_string += print_penrose_triangle(startPlace-H_UNIT*6*i, shortleng, longLeng, repeatNum, 0.3)


# svg_string += print_penrose_tie(startPlace+Z_UNIT*15, 1, 5, 2, 0.3)
# svg_string += print_circle(startPlace, 0.1, GOLD, "")

# svg_string += print_generic_corner(0, 0, startPlace+Z_UNIT*31, 1, 3, 0.3)

# for j in range(3):
#     pos = CENTER_ARR+H_UNIT*0.5*WIDTH_UNITS-Z_UNIT*5-Z_UNIT*10*j
#     for i in range(3):
#         longLeng = 4
#         svg_string += print_circle(pos, 1, WHITE, "")
#         svg_string += print_circle(pos+CORNER_DIR[i]*longLeng, 1, BLACK, "")
#         svg_string += print_generic_corner(i, j, pos, 1, longLeng)

#         svg_string += print_circle(pos-H_UNIT*3, 1, WHITE, "")
#         svg_string += print_circle(pos-H_UNIT*3+SECTION_DIR[i]*longLeng, 1, BLACK, "")
#         svg_string += print_generic_section(i, 0, pos-H_UNIT*3, 1, longLeng)
#         # svg_string += print_circle(pos-Z_UNIT*6, 1, WHITE, "")
#         # svg_string += print_circle(pos-Z_UNIT*6+CORNER_DIR[i]*5, 1, BLACK, "")
#         # svg_string += print_generic_corner2(i, j, pos-Z_UNIT*6, 1, 5)
#         pos-=H_UNIT*13


write_svg(WIDTH+2*MARGIN, 1*HEIGHT+2*MARGIN, svg_string)

