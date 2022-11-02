import math
import numpy as np

# Constants

SQRT3 = math.sqrt( 3)
MARGIN = 5
MARGIN_ARR = np.array([MARGIN, MARGIN])
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
# BLUE = WHITE
# RED = WHITE 
# GREEN = WHITE
