import numpy as np

val = np.array([10,20,30,40,50,60,70])

print(val)

for i in val:
    print(i)

print(np.__version__)

print(type(val))

num = np.array((10,20,30,40))

print(type(num))

twoDim = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(type(twoDim))

print(twoDim.ndim)

threeDim = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])


fiveDim = np.array([10,20,30,40,50], ndmin=5)

print(fiveDim)



























print(threeDim.ndim)