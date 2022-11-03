import math
import numpy as np
from constants import *
from functions import *

HEIGHT = 400
WIDTH_UNITS = 400
WIDTH = WIDTH_UNITS*0.5*SQRT3
CENTER_ARR = np.array([MARGIN+WIDTH*0.5, MARGIN+HEIGHT*0.5])

#Rotate 90 degrees
#Z -> X
#X -> -Y
#Y -> -Z

def print_generic_section(rotationNum, center, short_length, long_length, fill_opacity = 1):
    file_string = ""
    unit1=Z_UNIT
    unit2=X_UNIT
    unit3=Y_UNIT
    color1=GREEN
    color2=BLUE
    color3=RED
    if(rotationNum == 2):
            unit1=X_UNIT
            unit2=-Y_UNIT
            unit3=-Z_UNIT
            color1=BLUE
            color2=RED
            color3=GREEN
    if(rotationNum == 3):
            unit1=-Y_UNIT
            unit2=Z_UNIT
            unit3=-X_UNIT
            color1=RED
            color2=GREEN
            color3=BLUE

    path1 = "m", center, "m", ZERO, "l", unit1*long_length, "l", -unit2*short_length, "l", -unit1*long_length, "l",unit2*short_length
    path2 = "m", center, "m", ZERO, "l", unit1*long_length, "l", unit2*short_length, "l", -unit1*long_length, "l", -unit2*short_length
    file_string += print_shape_tuple(color3, path1, fill_opacity, 0)
    file_string += print_shape_tuple(color1, path2, fill_opacity, 0)
    file_string += print_line(center, center+unit1*long_length, BLACK, 0.2)
    file_string += print_line(center-unit2*short_length, center-unit2*short_length+unit1*long_length, BLACK, 0.2)
    file_string += print_line(center+unit2*short_length, center+unit2*short_length+unit1*long_length, BLACK, 0.2)

    return file_string

def print_generic_corner(rotationNum, center, short_length, long_length, fill_opacity = 1):
    file_string = ""
    unit1=Z_UNIT
    unit2=X_UNIT
    unit3=Y_UNIT
    color1=GREEN
    color2=BLUE
    color3=RED
    if(rotationNum == 2):
            unit1=X_UNIT
            unit2=-Y_UNIT
            unit3=-Z_UNIT
            color1=BLUE
            color2=RED
            color3=GREEN
    if(rotationNum == 3):
            unit1=-Y_UNIT
            unit2=Z_UNIT
            unit3=-X_UNIT
            color1=RED
            color2=GREEN
            color3=BLUE

    path2 = "m", center, "m", ZERO, "l", unit1*long_length, "l", unit1*short_length, "l", unit2*(long_length+short_length), "l", -unit3*short_length, "l", -unit2*(long_length-short_length), "l", -unit1*long_length
    path3 = "m", center, "m", unit1*long_length + unit2*short_length , "l", unit2*(long_length-short_length), "l", -unit3*short_length, "l", -unit2*(long_length-2*short_length), "l", unit1*short_length
    path4 = "m", center, "m", ZERO, "l", unit1*long_length, "l", unit1*short_length, "l", -unit3*short_length, "l", -unit1*long_length

    file_string += print_shape_tuple(color1, path2, fill_opacity, 0)
    file_string += print_shape_tuple(color2, path3, fill_opacity, 0)
    file_string += print_shape_tuple(color3, path4, fill_opacity, 0)

    p1=center
    p2=p1+unit1*long_length
    file_string += print_line(p1, p2, BLACK, 0.2)
    p1=p2
    p2=p1+unit1*short_length
    file_string += print_line(p1, p2, BLACK, 0.2)
    p1=p2
    p2=p1+unit2*(long_length+short_length)
    file_string += print_line(p1, p2, BLACK, 0.2)
    p1=p2
    p2=p1+-unit3*short_length
    p1=p2
    p2=p1+-unit2*(long_length-short_length)
    file_string += print_line(p1, p2, BLACK, 0.2)
    p1=p2
    p2=p1+-unit1*long_length
    file_string += print_line(p1, p2, BLACK, 0.2)
    p1=center+unit1*(long_length-short_length) + unit2*short_length
    p2=p1+unit2*(long_length-2*short_length)
    file_string += print_line(p1, p2, BLACK, 0.2)
    p1=center-unit2*short_length
    p2=p1+unit1*long_length
    file_string += print_line(p1, p2, BLACK, 0.2)
    p1=p2
    p2=p1+unit3*short_length
    file_string += print_line(p1, p2, BLACK, 0.2)
    return file_string

def print_penrose_triangle(center, short_length, long_length, fill_opacity = 1):
    file_string = ""

    pos=center
    file_string += print_generic_corner(1, pos, short_length, long_length, fill_opacity)

    pos=pos+Z_UNIT*long_length+X_UNIT*long_length
    file_string += print_generic_section(2, pos, short_length, long_length, fill_opacity)

    pos=pos+X_UNIT*long_length
    file_string += print_generic_corner(2, pos, short_length, long_length, fill_opacity)

    pos=pos+X_UNIT*long_length-Y_UNIT*long_length
    file_string += print_generic_section(3, pos, short_length, long_length, fill_opacity)

    pos=pos-Y_UNIT*long_length
    file_string += print_generic_corner(3, pos, short_length, long_length, fill_opacity)

    pos=pos+Z_UNIT*long_length-Y_UNIT*long_length
    file_string += print_generic_section(1, pos, short_length, long_length, fill_opacity)

    return file_string

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



def print_start_triple_recursive(list_sizes: list, list_offsets: list, previous_center):
    size = list_sizes.pop()
    return print_outer_cube(previous_center, 1, size) + print_triple_recursive(list_sizes, list_offsets, previous_center)

def print_triple_recursive(list_sizes: list, list_offsets: list, previous_center):
    size = list_sizes.pop()
    offset = list_offsets.pop()

    svg_string = ""
    dirvec = [Z_UNIT, -Y_UNIT, X_UNIT]
    for der_i in dirvec:
        layer_center = previous_center+offset*der_i
        svg_string += print_outer_cube(layer_center, 1, size)
    if (len(list_offsets) == 0):
        return svg_string 
    for der_i in dirvec:
        layer_center = previous_center+offset*der_i
        svg_string += print_outer_cube(layer_center, 1, size) + print_triple_recursive(list_sizes.copy(), list_offsets.copy(), layer_center)
    return svg_string 

# Designs


# svg_string += print_start_triple_recursive([5, 10, 22], [7, 14], center);
# svg_string += print_start_triple_recursive([1, 5, 10, 22], [2, 7, 14], MARGIN_ARR -40*Z_UNIT -42*H_UNIT);
# svg_string += print_start_triple_recursive([5, 10, 20], [7, 12], MARGIN_ARR -35*Z_UNIT -42*H_UNIT);

svg_string = ""
svg_string += print_compass()

# svg_string += draw_guidelines(WIDTH_UNITS, HEIGHT)
# svg_string += print_cube(MARGIN_ARR -40*Z_UNIT -42*H_UNIT, 20, 0.5)
# svg_string += print_outer_cube(MARGIN_ARR-WIDTH_UNITS*H_UNIT ,1,  5, 0.5)


#=======Grid=======
# for i in range(29):
#     gap = 7
#     svg_string += print_z_section(MARGIN_ARR-i*2*gap*H_UNIT ,1, -400, 0.5)
#     svg_string += print_x_section(MARGIN_ARR-i*2*gap*Z_UNIT ,1, -400, 0.5)
#     svg_string += print_y_section(MARGIN_ARR-i*2*gap*Z_UNIT+gap*Z_UNIT ,1, -400, 0.5)
#=======    =======

i=3
gap = 1
svg_string += print_penrose_triangle(CENTER_ARR ,1, 5, 0.5)

svg_string += print_generic_corner(1, CENTER_ARR+Z_UNIT*10, 1, 5)
svg_string += print_circle(CENTER_ARR+Z_UNIT*10, 0.1, GOLD, "")

svg_string += print_circle(CENTER_ARR-10*H_UNIT, 0.1, GOLD, "")
# svg_string += print_z_section(CENTER_ARR-10*H_UNIT ,1,  5)

# pos=CENTER_ARR+Z_UNIT*10
# svg_string += print_top_corner(pos ,1, 5, 0.5)
# svg_string += print_circle(pos, 0.1, GOLD, "")
# pos=CENTER_ARR+-Z_UNIT*10
# svg_string += print_left_corner(pos ,1, 5, 0.5)
# svg_string += print_circle(pos, 0.1, GOLD, "")
# pos=CENTER_ARR+-Z_UNIT*10+X_UNIT*10
# svg_string += print_bottom_corner(pos ,1, 5, 0.5)
# svg_string += print_circle(pos, 0.1, GOLD, "")

# svg_string += print_z_section(CENTER_ARR ,1, 5, 0.5)
# # svg_string += print_z_section(CENTER_ARR ,1, -5, 0.5)
# svg_string += print_x_section(CENTER_ARR ,1, 5, 0.5)
# svg_string += print_y_section(CENTER_ARR ,1, 5, 0.5)


# svg_string += print_x_section(CENTER_ARR ,1,  5)
# svg_string += print_outer_cube(MARGIN_ARR -44*Z_UNIT -44*H_UNIT,1,  20, 0.5)
# svg_string += print_top_design(MARGIN_ARR -40*Z_UNIT -42*H_UNIT)
# svg_string += print_mid_design(MARGIN_ARR -97.5*Z_UNIT -27*H_UNIT)
# svg_string += print_bot_design(MARGIN_ARR -Z_UNIT*135 -42*H_UNIT)

# svg_string += print_inner_cube(MARGIN_ARR -Z_UNIT*35 -42*H_UNIT+15*Z_UNIT, 1, 10)
# svg_string += print_inner_cube(MARGIN_ARR -Z_UNIT*35 -42*H_UNIT+15*X_UNIT, 1, 10)
# svg_string += print_inner_cube(MARGIN_ARR -Z_UNIT*35 -42*H_UNIT-15*Y_UNIT, 1, 10)

write_svg(WIDTH+2*MARGIN, 1*HEIGHT+2*MARGIN, svg_string)