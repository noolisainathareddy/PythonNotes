def greet():
    print("Hello, this is my first function")
    print("Welcome to python")



greet()

def add(a,b):
    print(a+b)

add(5,6)


def mul(a,b):
    return a*b

result = mul(2,4)

print(result)


def add_mul(a,b):
    return a+b, a*b

result1, result2 = add_mul(4,5)

print(result1)
print(result2)