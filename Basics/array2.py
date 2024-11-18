import numpy as np

arr = np.array([10,20,30,40])

i=0
print(len(arr))
while i < len(arr):
    # print("inside while loop")
    arr[i] = arr[i] + 5
    i +=1
 

print(arr)

arr = arr + 1

print(arr)