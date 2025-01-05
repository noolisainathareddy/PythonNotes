s1="abc"

s2 = lambda func : func.upper()
print(s2(s1))


f = lambda a : a*a
print(f(5))

j = lambda a,b: a+b

result = j(10,20)

print(result)

n = lambda x:"Positive" if x>1 else "Negative" if x < 0 else "zero"

print(n(5))

n =[10,15,20,30,35,45,50]

evens = list(filter(lambda x: x%2 ==0, n))
print(evens)