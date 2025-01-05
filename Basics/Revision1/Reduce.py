from functools import reduce

val = [10,20,30,40]

sum = reduce(lambda x,y: x*y, val)

print(sum)