import numpy as np
#
# val = np.array([1,2,3,])
#
# num = np.array([4,5,6])
#
#
# arr = np.concatenate((val, num))
#
# print(arr)
#


val1 = np.array([[1,2,3],[4,5,6]])

num1 = np.array([[7,8,9],[10,11,12]])

arr1 = np.concatenate((val1,num1), axis=1)

st = np.hstack((val1, num1))

st2 = np.vstack((val1, num1))

st3 = np.dstack((val1, num1))

print(st3)

