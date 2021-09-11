import math
 
import numpy as np

int_val = 5

my_int = int_val
my_int_2 = int_val

my_int += 5
print(my_int)
print(my_int_2)


center = np.array([5, 4])

my_val = center
my_2nd_val = center
my_3rd_val = center.copy()

print(my_val)
print(my_2nd_val)
print(my_3rd_val)

my_val += np.array([5, 4])

print(my_val)
print(my_2nd_val)
print(my_3rd_val)