import numpy as np

values1 = np.array([10,20,30,40,50])

values2 = values1.view()

# print(values1)
# print(values2)
#
# print(id(values1))
# print(id(values2))
print(values1.base)
print(values2.base)

values2.
print(values1.base is values2.base)




