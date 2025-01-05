
#Filter prints only true values in the output

val = [2,4,5,6,7,8,9,10]

even = filter(lambda x: x%2==0, val)

print(list(even))

mul = map(lambda x: x*2, val)

print(list(mul))