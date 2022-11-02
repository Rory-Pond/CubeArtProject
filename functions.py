import math
import numpy as np
from constants import *

#======= Functions =======

def print_shape_tuple(color, shape_tuple: tuple, fill_opacity = 1, stroke_width = 0.2):
    # fill_opacity=0.3
    string = "<path\n style=\"fill:" + color + ";fill-rule:evenodd; fill-opacity:" + str(fill_opacity) + ";stroke:#000000;stroke-linejoin=round;stroke-width:" + str(stroke_width) + ";stroke-linecap:round\"\nd=\""
    list_offset = ZERO
    offset_or_vlue = True
    for svg_val in shape_tuple:
        if (type(svg_val) is str):
            string += svg_val  + " "
            offset_or_vlue = (svg_val == "m")

        if (type(svg_val) is np.ndarray):
            string += str(svg_val[0]) + "," + str(svg_val[1]) + " "

    string += "\"\n/>\n" 
    return string

def print_circle(center, size, color, text):
    val = "<circle style=\"fill:" + color + "\" cx=\"" + str(center[0]) +"\" cy=\""+ str(center[1]) +"\" r=\"" + str(size) + "\"/> \n"
    val += "<text x=\"" + str(center[0]) +"\" y=\""+ str(center[1]) +"\" dominant-baseline=\"middle\" text-anchor=\"middle\" style=\"fill:GREEN;font: 0.7px sans-serif;\">"+text+"</text> \n"
    # print(text + ": " + str(center))
    return val

def print_line(center, center2, color = BLACK, stroke_width = 0.05):
    val = "<line x1=\"" + str(center[0]) +"\" y1=\"" + str(center[1]) +"\" x2=\"" + str(center2[0]) +"\" y2=\"" + str(center2[1]) +"\" style=\"stroke-width:" + str(stroke_width) + ";\" stroke=\"" + color + "\" />\n"
    # val = "<circle style=\"fill:" + color + "\" cx=\"" + str(center[0]) +"\" cy=\""+ str(center[1]) +"\" r=\"" + str(size) + "\"/> \n"
    # val += "<text x=\"" + str(center[0]) +"\" y=\""+ str(center[1]) +"\" dominant-baseline=\"middle\" text-anchor=\"middle\" style=\"fill:RED;font: 1px sans-serif;\">"+text+"</text> \n"
    # print(text + ": " + str(center))
    return val

def write_svg(sizeX, sizeY, string_to_print, file_string = "workfile.svg"):
    f = open(file_string, 'w')

    f.write("<svg viewBox=\" 0 0 " + str(sizeX) + " " + str(sizeY) + "\" xmlns=\"http://www.w3.org/2000/svg\">\n")
    f.write(string_to_print)
    f.write("</svg>")

    f.close()

def print_compass():
    func_string = print_circle(np.array([3,3]), 1, GOLD, "")
    func_string += print_circle(np.array([3,3])+X_UNIT, 0, GOLD, "X")
    func_string += print_circle(np.array([3,3])+Y_UNIT, 0, GOLD, "Y")
    func_string += print_circle(np.array([3,3])+Z_UNIT, 0, GOLD, "Z")
    func_string += print_circle(np.array([3,3])+H_UNIT, 0, GOLD, "H")
    func_string += print_line(np.array([3,3]),np.array([3,3])+X_UNIT)
    func_string += print_line(np.array([3,3]),np.array([3,3])+Y_UNIT)
    func_string += print_line(np.array([3,3]),np.array([3,3])+Z_UNIT)
    func_string += print_line(np.array([3,3]),np.array([3,3])+H_UNIT)

    func_string += print_circle(np.array([3,3])-X_UNIT, 0, GOLD, "-X")
    func_string += print_circle(np.array([3,3])-Y_UNIT, 0, GOLD, "-Y")
    func_string += print_circle(np.array([3,3])-Z_UNIT, 0, GOLD, "-Z")
    func_string += print_circle(np.array([3,3])-H_UNIT, 0, GOLD, "-H")
    func_string += print_line(np.array([3,3]),np.array([3,3])-X_UNIT)
    func_string += print_line(np.array([3,3]),np.array([3,3])-Y_UNIT)
    func_string += print_line(np.array([3,3]),np.array([3,3])-Z_UNIT)
    func_string += print_line(np.array([3,3]),np.array([3,3])-H_UNIT)
    return func_string

def print_cube(center, length, fill_opacity = 1):
    return print_simple_cube(center, length, length, length, fill_opacity)

def print_simple_cube(center, length_X, length_Z, length_Y, fill_opacity = 1):
    path1  = "m", center, "m", ZERO , "l",  Y_UNIT*length_Y, "l", -X_UNIT*length_X, "l", -Y_UNIT*length_Y, "l",  X_UNIT*length_X
    path2 = "m", center, "m", ZERO , "l", -Z_UNIT*length_Z, "l",  Y_UNIT*length_Y, "l",  Z_UNIT*length_Z, "l", -Y_UNIT*length_Y
    path3 = "m", center, "m", ZERO , "l", -Z_UNIT*length_Z, "l", -X_UNIT*length_X, "l",  Z_UNIT*length_Z, "l",  X_UNIT*length_X

    file_string = ""
    file_string += print_shape_tuple(RED,   path1, fill_opacity)
    file_string += print_shape_tuple(GREEN, path2, fill_opacity)
    file_string += print_shape_tuple(BLUE,  path3, fill_opacity)

    return file_string

def draw_guidelines(width: int, length: int, background = True):
    file_print = ""
    background  = "m", MARGIN_ARR, "l", -H_UNIT*width, "l",  -length*Z_UNIT, "l", H_UNIT*width, "l",  length*Z_UNIT
    if (background):
        file_print += print_shape_tuple(DARK_GREY,  background)

    for i in range(width):
        line_color = "#FF0000" if (i%10==5) else "#808080" 
        file_print += print_line(MARGIN_ARR  - (i*H_UNIT), MARGIN_ARR - length*Z_UNIT - (i*H_UNIT), line_color)

    for i in range(0, int(length+width/2)):
        line_color = "#FF0000" if (i%10==0) else "#808080"
        start = MARGIN_ARR - i*Z_UNIT                if (i<length)  else MARGIN_ARR - length*Z_UNIT - (i-length)*2*H_UNIT
        end   = MARGIN_ARR - width*X_UNIT - i*Z_UNIT if (i>width/2) else MARGIN_ARR - i*2*H_UNIT
        file_print += print_line(start, end, line_color)

    for i in range(int(0-width/2), length):
        line_color = "#FF0000" if (i%10==0) else "#808080"
        start = MARGIN_ARR - i*Z_UNIT                if(i>0)                else MARGIN_ARR + i*2*H_UNIT
        end   = MARGIN_ARR - width*Y_UNIT - i*Z_UNIT if(i<(length-width/2)) else MARGIN_ARR - length*Z_UNIT+ (i-(length))*2*H_UNIT 
        file_print += print_line(start, end, line_color)

    file_print += print_line(MARGIN_ARR, MARGIN_ARR-length*Z_UNIT, BLACK,0.1)
    file_print += print_line(MARGIN_ARR-H_UNIT*width, MARGIN_ARR-length*Z_UNIT-H_UNIT*width, BLACK,0.1)
    file_print += print_line(MARGIN_ARR, MARGIN_ARR-H_UNIT*width, BLACK,0.1)
    file_print += print_line(MARGIN_ARR-length*Z_UNIT, MARGIN_ARR-length*Z_UNIT-H_UNIT*width, BLACK,0.1)
    return file_print