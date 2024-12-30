import numpy as np
from numpy.ma.core import append

val = np.array([1,2,4,5,6,7,8,9,10])

# filter_arr = []
#
# for i in val:
#     if i%2==0:
#         filter_arr.append(True)
#     else:
#         filter_arr.append(False)
#
# newArr = val[filter_arr]
#
# print(newArr)

filterArr = val > 5

newArr = val[filterArr]

print(filterArr)
print(newArr)