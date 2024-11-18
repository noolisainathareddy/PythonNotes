from functools import reduce

nums = [10,15,20,25,30,35,40]


result = list(filter(lambda a: a%2==0, nums))

print(result)
 

val = [20,40,60,50,90,45,93,21]

output = list(map(lambda a:a+2, val))

print(output)


red = reduce(lambda a,b:a+b, val)
print(red)