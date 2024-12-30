import numpy as np

val = np.array([[10,30,50],[20,40,60]])
#
# # for i in val:
# #     print(i)
#
# for i in val:
#     for j in i:
#         print(j)



for x in np.nditer(val):
    print(x)


for idx, y in np.ndenumerate(val):
    print(idx, y)