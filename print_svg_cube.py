import math
 
import numpy as np
from numpy import random

# Constants
 
y = np.array([-math.sqrt(3),-1])/2
x = np.array([-math.sqrt(3),1])/2
z = np.array([0, -2])/2
  
zero = np.array([0, 0])
 
white = "#ffffff"
grey  = "#808080"
blue  = "#0000ff"
green = "#00ff00"
red   = "#ff0000"
yellow= "#ffff00"
gold =  "#FFD700"
 
# grey = white
# blue = white
# green = white
# red = white
 

# Functions

def convert_to_string(color, shape):
    string = "<path\n style=\"fill:" + color + ";fill-rule:evenodd; fill-opacity:0.5;stroke:#000000;stroke-linejoin=round;stroke-width:0.2;stroke-linecap:round\"\nd=\""
    list_offset = zero
    offset_or_vlue = True
    for svg_val in shape:
        if (type(svg_val) is str):
            string += svg_val  + " "
            offset_or_vlue = (svg_val == "m")
                
        if (type(svg_val) is np.ndarray):
            string += str(svg_val[0]) + "," + str(svg_val[1]) + " "
 
 
 
    string += "\"\n/>\n" 
 
    return string
 
def print_circle(center, size, color, text):
    val = "<circle style=\"fill:" + color + "\" cx=\"" + str(center[0]) +"\" cy=\""+ str(center[1]) +"\" r=\"" + str(size) + "\"/> \n"
    val += "<text x=\"" + str(center[0]) +"\" y=\""+ str(center[1]) +"\" dominant-baseline=\"middle\" text-anchor=\"middle\" style=\"fill:green;font: 0.7px sans-serif;\">"+text+"</text> \n"
    print(text + ": " + str(center))
    return val
 
def print_line(center, center2, color):
    val = "<line x1=\"" + str(center[0]) +"\" y1=\"" + str(center[1]) +"\" x2=\"" + str(center2[0]) +"\" y2=\"" + str(center2[1]) +"\" style=\"stroke-width:0.05;\" stroke=\"" + color + "\" />"
    # val = "<circle style=\"fill:" + color + "\" cx=\"" + str(center[0]) +"\" cy=\""+ str(center[1]) +"\" r=\"" + str(size) + "\"/> \n"
    # val += "<text x=\"" + str(center[0]) +"\" y=\""+ str(center[1]) +"\" dominant-baseline=\"middle\" text-anchor=\"middle\" style=\"fill:red;font: 1px sans-serif;\">"+text+"</text> \n"
    # print(text + ": " + str(center))
    return val
 
 
def print_inner_cube(center, short_length, long_length):
    file_string = ""
    
    len1 = long_length
    len2 = long_length - short_length
    if (len2<0):
        len2 = 0
    len3 = long_length - 3*short_length
    if (len3<0):
        len3 = 0
    len4 = long_length - 4*short_length
    if (len4<0):
        len4 = 0
 
    len5 = short_length
    len6 = 2*short_length
 
    path1 = "m", center, "m",  zero  , "l", -y*len2, "l",  x*len2, "l",  y*len2, "l", -x*len2, "m", -z*len5, "l", -y*len3, "l",  x*len3, "l",  y*len3, "l", -x*len3
    path2 = "m", center, "m",  zero  , "l",  z*len2, "l", -y*len2, "l", -z*len2, "l",  y*len2, "m", -x*len5, "l",  z*len3, "l", -y*len3, "l", -z*len3, "l",  y*len3
    path3 = "m", center, "m",  zero  , "l",  z*len2, "l",  x*len2, "l", -z*len2, "l", -x*len2, "m",  y*len5, "l",  z*len3, "l",  x*len3, "l", -z*len3, "l", -x*len3
    path4 = "m", center, "m", -x*len5, "l", -x*len5, "l", -y*len4, "l", -z*len5, "l",  y*len3
    path6 = "m", center, "m", -x*len5, "l", -x*len5, "l",  z*len4, "l",  y*len5, "l", -z*len3
    path5 = "m", center, "m",  y*len5, "l",  y*len5, "l",  x*len4, "l", -z*len5, "l", -x*len3
    path7 = "m", center, "m",  y*len5, "l",  y*len5, "l",  z*len4, "l", -x*len5, "l", -z*len3
    path8 = "m", center, "m", -x*len6, "l",  z*len4, "l", -y*len4, "l", -z*len4, "l",  y*len4
    path9 = "m", center, "m",  y*len6, "l",  z*len4, "l",  x*len4, "l", -z*len4, "l", -x*len4
    path10 ="m", center, "m",  z*len2, "l", -y*len2, "l", -x*len5, "l",  y*len1, "l",  x*len1, "l", -y*len5, "l",-x*len2
    path11 ="m", center, "m", -z*len5, "l", -y*len3, "l",  x*len5, "l",  y*len4, "l",  z*len5
    path12 ="m", center, "m", -z*len5, "l",  x*len3, "l", -y*len5, "l", -x*len4, "l",  z*len5
    path13 ="m", center, "m", -z*len6, "l", -y*len4, "l",  x*len4, "l",  y*len4, "l", -x*len4
    path14 ="m", center, "m", -y*len2, "l",  z*len2, "l", -x*len5, "l", -z*len1, "l",  x*len1, "l",  z*len5, "l", -x*len2
    path15 ="m", center, "m",  x*len2, "l",  z*len2, "l",  y*len5, "l", -z*len1, "l", -y*len1, "l",  z*len5, "l",  y*len2
 
    file_string += convert_to_string(grey,  path8)
    file_string += convert_to_string(grey,  path9)
    file_string += convert_to_string(grey,  path13)
 
    file_string += convert_to_string(blue,  path6)
    file_string += convert_to_string(red,   path4)
    file_string += convert_to_string(red,   path5)
 
    file_string += convert_to_string(green, path7)
    file_string += convert_to_string(green, path11)
    file_string += convert_to_string(blue,  path12)
 
    file_string += convert_to_string(blue,  path14)
    file_string += convert_to_string(green, path15)
    file_string += convert_to_string(red,   path10)
    file_string += convert_to_string(red,   path1)
    file_string += convert_to_string(green, path2)
    file_string += convert_to_string(blue,  path3)
 
    return file_string


def print_outer_cube(center, short_length, long_length):
    file_string = ""

    if (short_length>long_length):
        temp = long_length
        long_length = short_length
        short_length = temp

    len1 = long_length
    len2 = long_length - short_length
    if (len2<0):
        len2 = 0
    len25 = long_length - 2*short_length
    if (len25<0):
        len25 = 0
    len3 = long_length - 3*short_length
    if (len3<0):
        len3 = 0
    len4 = long_length - 4*short_length
    if (len4<0):
        len4 = 0

    len5 = short_length
    len6 = 2*short_length

    npath1 = "m", center, "m",   zero , "l",  y*len1, "l", -x*len1, "l", -y*len1, "l",  x*len1, "m",  z*len5, "l",  y*len25, "l", -x*len25, "l", -y*len25, "l",  x*len25
    npath2 = "m", center, "m",   zero , "l", -z*len1, "l",  y*len1, "l",  z*len1, "l", -y*len1, "m",  x*len5, "l", -z*len25, "l",  y*len25, "l",  z*len25, "l", -y*len25
    npath3 = "m", center, "m",   zero , "l", -z*len1, "l", -x*len1, "l",  z*len1, "l",  x*len1, "m", -y*len5, "l", -z*len25, "l", -x*len25, "l",  z*len25, "l",  x*len25

    npath4 = "m", center, "m",  z*len5, "l",  y*len3, "l", -x*len3, "l", -y*len3, "l",  x*len3
    npath5 = "m", center, "m",  x*len5, "l", -z*len3, "l",  y*len3, "l",  z*len3, "l", -y*len3
    npath6 = "m", center, "m", -y*len5, "l", -z*len3, "l", -x*len3, "l",  z*len3, "l",  x*len3

    npath7 = "m", center, "m",  z*len2, "l", -y*len25, "l",  x*len5, "l",  y*len3, "l",  z*len5
    npath8 = "m", center, "m",  z*len2, "l",  x*len25, "l", -y*len5, "l", -x*len3, "l",  z*len5

    npath9  = "m", center, "m",  -y*len2, "l", y*len5, "l",  x*len3, "l", -z*len5, "l", -x*len25
    npath10 = "m", center, "m",  -y*len2, "l", y*len5, "l",  z*len3, "l", -x*len5, "l", -z*len25

    npath11 = "m", center, "m",  x*len2, "l", -x*len5, "l", -y*len3, "l", -z*len5, "l",  y*len25
    npath12 = "m", center, "m",  x*len2, "l", -x*len5, "l",  z*len3, "l",  y*len5, "l", -z*len25

    file_string += convert_to_string(red,   npath1)
    file_string += convert_to_string(green, npath2)
    file_string += convert_to_string(blue,  npath3)

    # file_string += convert_to_string(grey,  npath4)
    # file_string += convert_to_string(grey,  npath5)
    # file_string += convert_to_string(grey,  npath6)

    file_string += convert_to_string(green, npath7)
    file_string += convert_to_string(blue,  npath8)

    file_string += convert_to_string(red, npath9)
    file_string += convert_to_string(green,  npath10)

    file_string += convert_to_string(red, npath11)
    file_string += convert_to_string(blue,  npath12)

    return file_string

def print_tri_cube(pos):
    file_string = ""
    offset_plane = zero, (-y-x), (z-x)
    offset_internal_array = -2*x, 2*y,  -2*z
 
    depth_of_cubes = 3
    short_length = 1
    max_long_length = (depth_of_cubes-1)*5+5
    center = pos - (x*max_long_length) + (z*max_long_length*0.5)
 
    for j in range(3):
        planpos = offset_plane[j]*max_long_length
        for i in reversed(range(depth_of_cubes)):
            looppos = (offset_internal_array[j])*(depth_of_cubes-i-1)
 
            long_length = (i)*5+5
            cube_pos= center + looppos + planpos
            circle_pos =center + planpos
            circle_pos2 =center + planpos - (x*max_long_length)
            # + granpos + planepos + looppos
            
            file_string += print_inner_cube(cube_pos, short_length, long_length)
    return file_string
 
def draw_grid():
    for i in range(-2, 10):
        for j in range(-2, 10):
            f.write(print_tri_cube(np.array([math.sqrt(3)*(j*45)       , (52.5+(i*45))      ])))
            f.write(print_tri_cube(np.array([math.sqrt(3)*((j*45)+22.5), (52.5+22.5)+(i*45) ])))


def draw_guidelines():
    center = np.array([0, -20])

    set_x = center.copy()
    set_y = center.copy()
    set_z = center.copy() 

    offset_x = center.copy() - 100*x
    offset_y = center.copy() - 100*y
    offset_z = center.copy() - 100*z

    file_print = ""
    for i in range(100):
        set_x = set_x - z
        set_y = set_y - z
        set_z = set_z -np.array([-math.sqrt(3),0])/2
        
        offset_x = offset_x - z
        offset_y = offset_y - z
        offset_z = offset_z - np.array([-math.sqrt(3),0])/2
        
        file_print += print_line(set_x, offset_x, "#808080")
        file_print += print_line(set_y, offset_y, "#808080")
        file_print += print_line(set_z, offset_z, "#808080")
        # center = center - x
        # offset_y = offset_y + y
        # offset_x = offset_x + z
        # # svg_string += print_circle(center, 0.001, gold, str(i+1))
        # svg_string += print_line(center + 100*z, offset_y, "#000000")
        # svg_string += print_line(center - 100*y, offset_x, "#000000")
    return file_print

def write_svg(sizeX, sizeY, string_to_print):
    f = open('workfile.svg', 'w')

    f.write("<svg viewBox=\" 0 0 " + str(sizeX) + " " + str(sizeY) + "\" xmlns=\"http://www.w3.org/2000/svg\">\n")
    f.write(string_to_print)
    f.write("</svg>")

    f.close()


# svg_string = print_tri_cube(np.array([0,52.5]))
 
# center = np.array([52.5, 45])
# center = np.array([0, 45]) - x*15 -y*15

# svg_string += print_circle(center, 0.2, gold, "0")
# temp = random.randint(100)

center = np.array([0, 27]) -27*np.array([-math.sqrt(3),0])/2
svg_string= ""
svg_string += print_outer_cube(center.copy()     , 1, 15)
svg_string += print_outer_cube(center.copy()+16*z, 1, 10)
svg_string += print_outer_cube(center.copy()+16*x, 1, 10)
svg_string += print_outer_cube(center.copy()-16*y, 1, 10)
svg_string += print_outer_cube(center.copy()-6*x , 1, 5)
svg_string += print_outer_cube(center.copy()+6*y , 1, 5)
svg_string += print_outer_cube(center.copy()-6*z , 1, 5)
svg_string += print_outer_cube(center.copy()-16*z-24*x , 1, 5)

# svg_string += draw_guidelines()

# svg_string += print_outer_cube(np.array([15,30]), 2, 10)
# svg_string += print_circle(np.array([3,3]), 1, gold, str(temp))



write_svg(47, 47, svg_string)
# print(list_of_points)
