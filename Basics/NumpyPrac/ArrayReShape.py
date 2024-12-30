import numpy as np

val = np.array([10,20,30,40,50,60,70,80,90,100])



x = val.reshape(1,5,2)

y = val.reshape(2,5)
print(x)
print(y)

# Flattening array -> converting multi-dimentional array to 1D
z = x.reshape(-1)
print(z)