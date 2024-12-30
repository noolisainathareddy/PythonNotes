import numpy as np

val = np.array([10,20,30,50,40,50,60,70,50])

x = np.where(val == 50)

print(x)

y = np.where(val == 5)

print(y)

z = np.searchsorted(val, 200)

print(z)