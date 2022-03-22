import math
import numpy as np

# Constants

SQRT3 = math.sqrt( 3)
MARGIN = 5
MARGIN_ARR = np.array([MARGIN, MARGIN])
HEIGHT = 180
WIDTH_UNITS = 84
WIDTH = WIDTH_UNITS*0.5*SQRT3

Z_UNIT = np.array([0, -2])/2
H_UNIT = np.array([-SQRT3,0])/2
X_UNIT = np.array([-SQRT3,1])/2
Y_UNIT = np.array([-SQRT3,-1])/2

# X_UNIT = H_UNIT-0.5*Z_UNIT
# Y_UNIT = H_UNIT+0.5*Z_UNIT

ZERO = np.array([0, 0])

neonpink = "#f03a88"
neonyellow = "#fff300"
neonorange = "#ff5f1f"

BLACK     = "#000000"
GREY      = "#808080"
DARK_GREY = "#4d4d4d"
WHITE     = "#FFFFFF"
BLUE      = "#0000FF"
RED       = "#FF0000"
GREEN     = "#00FF00"
YELLOW    = "#FFFF00"
GOLD      = "#FFD700"

BLUE = neonpink
RED = neonyellow 
GREEN = neonorange

# Functions

def print_shape_tuple(color, shape_tuple: tuple, fill_opacity = 1):
    # fill_opacity=0.3
    string = "<path\n style=\"fill:" + color + ";fill-rule:evenodd; fill-opacity:" + str(fill_opacity) + ";stroke:#000000;stroke-linejoin=round;stroke-width:0.2;stroke-linecap:round\"\nd=\""
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
 
    path1 = "m", center, "m",  ZERO       , "l", -Y_UNIT*len2, "l",  X_UNIT*len2, "l",  Y_UNIT*len2, "l", -X_UNIT*len2, "m", -Z_UNIT*len5, "l", -Y_UNIT*len3, "l",  X_UNIT*len3, "l",  Y_UNIT*len3, "l", -X_UNIT*len3
    path2 = "m", center, "m",  ZERO       , "l",  Z_UNIT*len2, "l", -Y_UNIT*len2, "l", -Z_UNIT*len2, "l",  Y_UNIT*len2, "m", -X_UNIT*len5, "l",  Z_UNIT*len3, "l", -Y_UNIT*len3, "l", -Z_UNIT*len3, "l",  Y_UNIT*len3
    path3 = "m", center, "m",  ZERO       , "l",  Z_UNIT*len2, "l",  X_UNIT*len2, "l", -Z_UNIT*len2, "l", -X_UNIT*len2, "m",  Y_UNIT*len5, "l",  Z_UNIT*len3, "l",  X_UNIT*len3, "l", -Z_UNIT*len3, "l", -X_UNIT*len3
    path4 = "m", center, "m", -X_UNIT*len5, "l", -X_UNIT*len5, "l", -Y_UNIT*len4, "l", -Z_UNIT*len5, "l",  Y_UNIT*len3
    path6 = "m", center, "m", -X_UNIT*len5, "l", -X_UNIT*len5, "l",  Z_UNIT*len4, "l",  Y_UNIT*len5, "l", -Z_UNIT*len3
    path5 = "m", center, "m",  Y_UNIT*len5, "l",  Y_UNIT*len5, "l",  X_UNIT*len4, "l", -Z_UNIT*len5, "l", -X_UNIT*len3
    path7 = "m", center, "m",  Y_UNIT*len5, "l",  Y_UNIT*len5, "l",  Z_UNIT*len4, "l", -X_UNIT*len5, "l", -Z_UNIT*len3
    path8 = "m", center, "m", -X_UNIT*len6, "l",  Z_UNIT*len4, "l", -Y_UNIT*len4, "l", -Z_UNIT*len4, "l",  Y_UNIT*len4
    path9 = "m", center, "m",  Y_UNIT*len6, "l",  Z_UNIT*len4, "l",  X_UNIT*len4, "l", -Z_UNIT*len4, "l", -X_UNIT*len4
    path10 ="m", center, "m",  Z_UNIT*len2, "l", -Y_UNIT*len2, "l", -X_UNIT*len5, "l",  Y_UNIT*len1, "l",  X_UNIT*len1, "l", -Y_UNIT*len5, "l",-X_UNIT*len2
    path11 ="m", center, "m", -Z_UNIT*len5, "l", -Y_UNIT*len3, "l",  X_UNIT*len5, "l",  Y_UNIT*len4, "l",  Z_UNIT*len5
    path12 ="m", center, "m", -Z_UNIT*len5, "l",  X_UNIT*len3, "l", -Y_UNIT*len5, "l", -X_UNIT*len4, "l",  Z_UNIT*len5
    path13 ="m", center, "m", -Z_UNIT*len6, "l", -Y_UNIT*len4, "l",  X_UNIT*len4, "l",  Y_UNIT*len4, "l", -X_UNIT*len4
    path14 ="m", center, "m", -Y_UNIT*len2, "l",  Z_UNIT*len2, "l", -X_UNIT*len5, "l", -Z_UNIT*len1, "l",  X_UNIT*len1, "l",  Z_UNIT*len5, "l", -X_UNIT*len2
    path15 ="m", center, "m",  X_UNIT*len2, "l",  Z_UNIT*len2, "l",  Y_UNIT*len5, "l", -Z_UNIT*len1, "l", -Y_UNIT*len1, "l",  Z_UNIT*len5, "l",  Y_UNIT*len2
 
    file_string += print_shape_tuple(GREY,  path8)
    file_string += print_shape_tuple(GREY,  path9)
    file_string += print_shape_tuple(GREY,  path13)
 
    file_string += print_shape_tuple(BLUE,  path6)
    file_string += print_shape_tuple(RED,   path4)
    file_string += print_shape_tuple(RED,   path5)
 
    file_string += print_shape_tuple(GREEN, path7)
    file_string += print_shape_tuple(GREEN, path11)
    file_string += print_shape_tuple(BLUE,  path12)
 
    file_string += print_shape_tuple(BLUE,  path14)
    file_string += print_shape_tuple(GREEN, path15)
    file_string += print_shape_tuple(RED,   path10)
    file_string += print_shape_tuple(RED,   path1)
    file_string += print_shape_tuple(GREEN, path2)
    file_string += print_shape_tuple(BLUE,  path3)
 
    return file_string

def print_outer_cube(center, short_length, long_length, fill_opacity = 1):
    file_string = ""

    if (short_length>long_length):
        temp = long_length
        long_length = short_length
        short_length = temp
    if (3*short_length > long_length):
        return print_cube(center, long_length, fill_opacity)
    
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

    npath1 = "m", center, "m",   ZERO , "l",  Y_UNIT*len1, "l", -X_UNIT*len1, "l", -Y_UNIT*len1, "l",  X_UNIT*len1, "m",  Z_UNIT*len5, "l",  Y_UNIT*len25, "l", -X_UNIT*len25, "l", -Y_UNIT*len25, "l",  X_UNIT*len25
    npath2 = "m", center, "m",   ZERO , "l", -Z_UNIT*len1, "l",  Y_UNIT*len1, "l",  Z_UNIT*len1, "l", -Y_UNIT*len1, "m",  X_UNIT*len5, "l", -Z_UNIT*len25, "l",  Y_UNIT*len25, "l",  Z_UNIT*len25, "l", -Y_UNIT*len25
    npath3 = "m", center, "m",   ZERO , "l", -Z_UNIT*len1, "l", -X_UNIT*len1, "l",  Z_UNIT*len1, "l",  X_UNIT*len1, "m", -Y_UNIT*len5, "l", -Z_UNIT*len25, "l", -X_UNIT*len25, "l",  Z_UNIT*len25, "l",  X_UNIT*len25

    npath4 = "m", center, "m",  Z_UNIT*len5, "l",  Y_UNIT*len3, "l", -X_UNIT*len3, "l", -Y_UNIT*len3, "l",  X_UNIT*len3
    npath5 = "m", center, "m",  X_UNIT*len5, "l", -Z_UNIT*len3, "l",  Y_UNIT*len3, "l",  Z_UNIT*len3, "l", -Y_UNIT*len3
    npath6 = "m", center, "m", -Y_UNIT*len5, "l", -Z_UNIT*len3, "l", -X_UNIT*len3, "l",  Z_UNIT*len3, "l",  X_UNIT*len3

    npath7 = "m", center, "m",  Z_UNIT*len2, "l", -Y_UNIT*len25, "l",  X_UNIT*len5, "l",  Y_UNIT*len3, "l",  Z_UNIT*len5
    npath8 = "m", center, "m",  Z_UNIT*len2, "l",  X_UNIT*len25, "l", -Y_UNIT*len5, "l", -X_UNIT*len3, "l",  Z_UNIT*len5

    npath9  = "m", center, "m",  -Y_UNIT*len2, "l", Y_UNIT*len5, "l",  X_UNIT*len3, "l", -Z_UNIT*len5, "l", -X_UNIT*len25
    npath10 = "m", center, "m",  -Y_UNIT*len2, "l", Y_UNIT*len5, "l",  Z_UNIT*len3, "l", -X_UNIT*len5, "l", -Z_UNIT*len25

    npath11 = "m", center, "m",  X_UNIT*len2, "l", -X_UNIT*len5, "l", -Y_UNIT*len3, "l", -Z_UNIT*len5, "l",  Y_UNIT*len25
    npath12 = "m", center, "m",  X_UNIT*len2, "l", -X_UNIT*len5, "l",  Z_UNIT*len3, "l",  Y_UNIT*len5, "l", -Z_UNIT*len25

    file_string += print_shape_tuple(RED,   npath1, fill_opacity)
    file_string += print_shape_tuple(GREEN, npath2, fill_opacity)
    file_string += print_shape_tuple(BLUE,  npath3, fill_opacity)

    file_string += print_shape_tuple(GREY,  npath4, fill_opacity)
    file_string += print_shape_tuple(GREY,  npath5, fill_opacity)
    file_string += print_shape_tuple(GREY,  npath6, fill_opacity)

    file_string += print_shape_tuple(GREEN, npath7, fill_opacity)
    file_string += print_shape_tuple(BLUE,  npath8, fill_opacity)

    file_string += print_shape_tuple(RED, npath9, fill_opacity)
    file_string += print_shape_tuple(GREEN,  npath10, fill_opacity)

    file_string += print_shape_tuple(RED, npath11, fill_opacity)
    file_string += print_shape_tuple(BLUE,  npath12, fill_opacity)

    return file_string

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

def draw_grid_of_mid_design():
    func_string = ""
    for i in range(-2, 10):
        for j in range(-2, 10):
            func_string += print_mid_design(np.array([SQRT3*(j*45)       , (52.5+(i*45))      ]))
            func_string += print_mid_design(np.array([SQRT3*((j*45)+22.5), (52.5+22.5)+(i*45) ]))
    return func_string

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

def print_mid_design(pos):
    file_string = ""
    offset_plane = ZERO, (-Y_UNIT-X_UNIT), (Z_UNIT-X_UNIT)
    offset_internal_array = -2*X_UNIT, 2*Y_UNIT,  -2*Z_UNIT
    
    depth_of_cubes = 3
    short_length = 1
    max_long_length = (depth_of_cubes-1)*5+5
    center = pos

    for j in range(3):
        planpos = offset_plane[j]*max_long_length
        for i in reversed(range(depth_of_cubes)):
            looppos = (offset_internal_array[j])*(depth_of_cubes-i-1)
 
            long_length = (i)*5+5
            cube_pos= center + looppos + planpos
            circle_pos =center + planpos
            circle_pos2 =center + planpos - (X_UNIT*max_long_length)
            # + granpos + planepos + looppos
            
            file_string += print_inner_cube(cube_pos, short_length, long_length)
    return file_string

def print_bot_design(center):
    svg_string= ""
    svg_string += print_outer_cube(center          , 1, 15, 1)
    svg_string += print_outer_cube(center+15*Z_UNIT, 1, 10, 1)
    svg_string += print_outer_cube(center+15*X_UNIT, 1, 10, 1)
    svg_string += print_outer_cube(center-15*Y_UNIT, 1, 10, 1)
    svg_string += print_outer_cube(center-6*X_UNIT , 1, 5, 1)
    svg_string += print_outer_cube(center+6*Y_UNIT , 1, 5, 1)
    svg_string += print_outer_cube(center-6*Z_UNIT , 1, 5, 1)
    return svg_string

def print_top_design(center):
    return print_start_triple_recursive([5, 10, 15], [7, 12], center);
# svg_string += print_start_triple_recursive([5, 10, 22], [7, 14], center);
# svg_string += print_start_triple_recursive([1, 5, 10, 22], [2, 7, 14], MARGIN_ARR -40*Z_UNIT -42*H_UNIT);
# svg_string += print_start_triple_recursive([5, 10, 20], [7, 12], MARGIN_ARR -35*Z_UNIT -42*H_UNIT);

# svg_string += print_compass()
svg_string = ""
# svg_string += draw_guidelines(WIDTH_UNITS, HEIGHT)
svg_string += print_top_design(MARGIN_ARR -40*Z_UNIT -42*H_UNIT)
svg_string += print_mid_design(MARGIN_ARR -97.5*Z_UNIT -27*H_UNIT)
svg_string += print_bot_design(MARGIN_ARR -Z_UNIT*135 -42*H_UNIT)

svg_string += print_inner_cube(MARGIN_ARR -Z_UNIT*135 -42*H_UNIT+15*Z_UNIT, 1, 10)
svg_string += print_inner_cube(MARGIN_ARR -Z_UNIT*135 -42*H_UNIT+15*X_UNIT, 1, 10)
svg_string += print_inner_cube(MARGIN_ARR -Z_UNIT*135 -42*H_UNIT-15*Y_UNIT, 1, 10)

write_svg(WIDTH+2*MARGIN, 1*HEIGHT+2*MARGIN, svg_string)

def write_saved_designs():
    write_svg(450, 450, draw_grid(), "GridMidDesign.svg")
    write_svg(20+SQRT3*42, 200 , draw_guidelines(84, 180) + print_mid_design(np.array([10+13.5*SQRT3,10+97.5])) + print_bot_design(np.array([10+21*SQRT3,10+135])), "FullBoard.svg")

    n=6
    sizes = [5* 2**i for i in range(n)]
    offsets = [7* 2**i for i in range(n-1)]
    area = 7* 2**n
    write_svg(area, area, print_start_triple_recursive(sizes, offsets,  np.array([area/2, area/2])), "fractalTopDesign.svg")