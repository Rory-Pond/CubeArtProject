import math
import numpy as np
from constants import *
from functions import *

HEIGHT = 40
WIDTH_UNITS = 70
WIDTH = WIDTH_UNITS*0.5*SQRT3
CENTER_ARR = np.array([MARGIN+WIDTH*0.5, MARGIN+HEIGHT*0.5])

UNIT_1 = [Z_UNIT,  X_UNIT, -Y_UNIT, -Z_UNIT,  Y_UNIT, -Y_UNIT]
UNIT_2 = [X_UNIT, -Y_UNIT,  Z_UNIT, -X_UNIT, -Z_UNIT,  Z_UNIT]
UNIT_3 = [Y_UNIT, -Z_UNIT, -X_UNIT, -Y_UNIT,  X_UNIT, -X_UNIT]

COLOR_1 = [GREEN,  BLUE,   RED,  BLUE,   RED,   RED]
COLOR_2 = [ BLUE,   RED, GREEN, GREEN,  BLUE,  BLUE]
COLOR_3 = [  RED, GREEN,  BLUE,   RED, GREEN, GREEN]

OFFSET = [ZERO, ZERO, ZERO, Z_UNIT+X_UNIT, Z_UNIT-Y_UNIT, ZERO]
OFFSET_SECTION = [ZERO, ZERO, ZERO, Z_UNIT, -Y_UNIT, ZERO]

CORNER_DIR = [Z_UNIT+X_UNIT, X_UNIT-Y_UNIT, Z_UNIT-Y_UNIT, Z_UNIT+X_UNIT, Z_UNIT-Y_UNIT, ZERO]
SECTION_DIR = [Z_UNIT, X_UNIT, -Y_UNIT, Z_UNIT, -Y_UNIT, -X_UNIT]

#Rotate 90 degrees
#Z -> X
#X -> -Y
#Y -> -Z

def print_generic_section(rN, center, short_length, long_length, fill_opacity = 1):
    file_string = ""
    localCenter = center + + OFFSET_SECTION[rN]*long_length
    path1 = "m", localCenter, "m", ZERO, "l", UNIT_1[rN]*long_length, "l", -UNIT_2[rN]*short_length, "l", -UNIT_1[rN]*long_length, "l",UNIT_2[rN]*short_length
    path2 = "m", localCenter, "m", ZERO, "l", UNIT_1[rN]*long_length, "l", UNIT_2[rN]*short_length, "l", -UNIT_1[rN]*long_length, "l", -UNIT_2[rN]*short_length
    file_string += print_shape_tuple(COLOR_3[rN], path1, fill_opacity, 0)
    file_string += print_shape_tuple(COLOR_1[rN], path2, fill_opacity, 0)
    file_string += print_line(localCenter, localCenter+UNIT_1[rN]*long_length, BLACK, 0.2)
    file_string += print_line(localCenter-UNIT_2[rN]*short_length, localCenter-UNIT_2[rN]*short_length+UNIT_1[rN]*long_length, BLACK, 0.2)
    file_string += print_line(localCenter+UNIT_2[rN]*short_length, localCenter+UNIT_2[rN]*short_length+UNIT_1[rN]*long_length, BLACK, 0.2)

    return file_string

def print_generic_corner2(rN, center, short_length, long_length, fill_opacity = 1):
    file_string = ""

    localCenter = center + OFFSET[rN]*long_length

    path1 = "m", localCenter, "m", -UNIT_2[rN]*short_length, "l", UNIT_1[rN]*long_length, "l", UNIT_2[rN]*(long_length+short_length), "l", -UNIT_3[rN]*short_length, "l", -UNIT_2[rN]*(long_length-short_length), "l", -UNIT_1[rN]*(long_length-short_length)
    path2 = "m", localCenter, "m", UNIT_1[rN]*long_length -UNIT_2[rN]*short_length , "l", UNIT_3[rN]*short_length, "l", UNIT_2[rN]*(long_length+short_length),  "l", -UNIT_3[rN]*short_length,
    path3 = "m", localCenter, "m", UNIT_2[rN]*short_length, "l", UNIT_1[rN]*(long_length-short_length), "l", -UNIT_2[rN]*short_length, "l", -UNIT_1[rN]*(long_length-short_length)

    file_string += print_shape_tuple(COLOR_1[(rN+2)%6], path1, fill_opacity, 0)
    file_string += print_shape_tuple(COLOR_2[(rN+2)%6], path2, fill_opacity, 0)
    file_string += print_shape_tuple(COLOR_3[(rN+2)%6], path3, fill_opacity, 0)

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
    return file_string

def print_generic_corner(rN, center, short_length, long_length, fill_opacity = 1):
    file_string = ""
    localCenter = center + OFFSET[rN]*long_length

    path1 = "m", localCenter, "m", ZERO, "l", UNIT_1[rN]*long_length, "l", UNIT_1[rN]*short_length, "l", UNIT_2[rN]*(long_length+short_length), "l", -UNIT_3[rN]*short_length, "l", -UNIT_2[rN]*(long_length-short_length), "l", -UNIT_1[rN]*long_length
    path2 = "m", localCenter, "m", UNIT_1[rN]*long_length + UNIT_2[rN]*short_length , "l", UNIT_2[rN]*(long_length-short_length), "l", -UNIT_3[rN]*short_length, "l", -UNIT_2[rN]*(long_length-2*short_length), "l", UNIT_1[rN]*short_length
    path3 = "m", localCenter, "m", ZERO, "l", UNIT_1[rN]*long_length, "l", UNIT_1[rN]*short_length, "l", -UNIT_3[rN]*short_length, "l", -UNIT_1[rN]*long_length

    file_string += print_shape_tuple(COLOR_1[rN], path1, fill_opacity, 0)
    file_string += print_shape_tuple(COLOR_2[rN], path2, fill_opacity, 0)
    file_string += print_shape_tuple(COLOR_3[rN], path3, fill_opacity, 0)

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
    return file_string

def print_penrose_triangle(center, short_length, long_length, sidelength = 1, fill_opacity = 1):
    file_string = ""

    pos=center
    file_string += print_generic_corner(0, pos, short_length, long_length, fill_opacity)
    pos=pos+Z_UNIT*long_length+X_UNIT*long_length
    
    for i in range(sidelength):
        file_string += print_generic_section(1, pos, short_length, long_length, fill_opacity)
        pos=pos+X_UNIT*long_length

    file_string += print_generic_corner(1, pos, short_length, long_length, fill_opacity)
    pos=pos+X_UNIT*long_length-Y_UNIT*long_length

    for i in range(sidelength):
        file_string += print_generic_section(2, pos, short_length, long_length, fill_opacity)
        pos=pos-Y_UNIT*long_length

    file_string += print_generic_corner(2, pos, short_length, long_length, fill_opacity)
    pos=pos+Z_UNIT*long_length-Y_UNIT*long_length

    for i in range(sidelength):
        file_string += print_generic_section(0, pos, short_length, long_length, fill_opacity)
        pos=pos+Z_UNIT*long_length
    
    file_string += print_generic_section(0, pos, short_length, long_length, fill_opacity)
    
    return file_string

def print_penrose_tie(center, short_length, long_length, sidelength = 1, fill_opacity = 1):
    file_string = ""

    pos=center
    file_string += print_generic_corner(0, pos, short_length, long_length, fill_opacity)
    pos += CORNER_DIR[0]*long_length
    
    file_string += print_generic_section(1, pos, short_length, long_length, fill_opacity)
    pos += SECTION_DIR[1]*long_length
    
    file_string += print_generic_section(1, pos, short_length, long_length, fill_opacity)
    pos += SECTION_DIR[1]*long_length
    
    file_string += print_generic_corner2(3, pos, short_length, long_length, fill_opacity)
    pos += CORNER_DIR[3]*long_length


    file_string += print_generic_corner2(4, pos, short_length, long_length, fill_opacity)
    pos += CORNER_DIR[4]*long_length

    file_string += print_generic_section(4, pos, short_length, long_length, fill_opacity)
    pos += SECTION_DIR[4]*long_length

    file_string += print_generic_section(4, pos, short_length, long_length, fill_opacity)
    pos += SECTION_DIR[4]*long_length

    file_string += print_generic_corner(2, pos, short_length, long_length, fill_opacity)
    pos += CORNER_DIR[2]*long_length

    return file_string


# Designs

svg_string = ""
svg_string += print_compass()

# svg_string += print_generic_corner3(5, CENTER_ARR+Z_UNIT*10-H_UNIT*15, 1, 3)

svg_string += print_penrose_triangle(CENTER_ARR+Z_UNIT*10+H_UNIT*15, 1, 3)

svg_string += print_penrose_tie(CENTER_ARR+Z_UNIT*10, 1, 3)
svg_string += print_circle(CENTER_ARR+Z_UNIT*10, 0.1, GOLD, "")


pos = CENTER_ARR+H_UNIT*0.5*WIDTH_UNITS-Z_UNIT*5
for i in range(6):
    svg_string += print_circle(pos, 1, WHITE, "")
    svg_string += print_circle(pos+CORNER_DIR[i]*5, 1, BLACK, "")
    svg_string += print_generic_corner(i, pos, 1, 5)


    svg_string += print_circle(pos-Z_UNIT*7, 1, WHITE, "")
    svg_string += print_circle(pos-Z_UNIT*7+SECTION_DIR[i]*5, 1, BLACK, "")
    svg_string += print_generic_section(i, pos-Z_UNIT*7, 1, 5)

    svg_string += print_circle(pos-Z_UNIT*14, 1, WHITE, "")
    svg_string += print_circle(pos-Z_UNIT*14+CORNER_DIR[i]*5, 1, BLACK, "")
    svg_string += print_generic_corner2(i, pos-Z_UNIT*14, 1, 5)
    pos-=H_UNIT*13





write_svg(WIDTH+2*MARGIN, 1*HEIGHT+2*MARGIN, svg_string)

def draw_guidelines(width: int, length: int, background = True):
    file_print = ""
    background  = "m", MARGIN_ARR, "l", -H_UNIT*width, "l",  -length*Z_UNIT, "l", H_UNIT*width, "l",  length*Z_UNIT
    if (background):
        file_print += print_shape_tuple(DARK_GREY,  background)

    for i in range(width):
        line_color = "#FF0000" if (i%15==12) else "#808080" 
        file_print += print_line(MARGIN_ARR  - (i*H_UNIT), MARGIN_ARR - length*Z_UNIT - (i*H_UNIT), line_color)

    for i in range(0, int(length+width/2)):
        line_color = "#FF0000" if (i%15==6) else "#808080"
        start = MARGIN_ARR - i*Z_UNIT                if (i<length)  else MARGIN_ARR - length*Z_UNIT - (i-length)*2*H_UNIT
        end   = MARGIN_ARR - width*X_UNIT - i*Z_UNIT if (i>width/2) else MARGIN_ARR - i*2*H_UNIT
        file_print += print_line(start, end, line_color)

    for i in range(int(0-width/2), length):
        line_color = "#FF0000" if (i%15==9) else "#808080"
        start = MARGIN_ARR - i*Z_UNIT                if(i>0)                else MARGIN_ARR + i*2*H_UNIT
        end   = MARGIN_ARR - width*Y_UNIT - i*Z_UNIT if(i<(length-width/2)) else MARGIN_ARR - length*Z_UNIT+ (i-(length))*2*H_UNIT 
        file_print += print_line(start, end, line_color)

    file_print += print_line(MARGIN_ARR, MARGIN_ARR-length*Z_UNIT, BLACK,0.1)
    file_print += print_line(MARGIN_ARR-H_UNIT*width, MARGIN_ARR-length*Z_UNIT-H_UNIT*width, BLACK,0.1)
    file_print += print_line(MARGIN_ARR, MARGIN_ARR-H_UNIT*width, BLACK,0.1)
    file_print += print_line(MARGIN_ARR-length*Z_UNIT, MARGIN_ARR-length*Z_UNIT-H_UNIT*width, BLACK,0.1)
    return file_print