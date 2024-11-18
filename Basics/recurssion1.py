
#
# print(sys.getrecursionlimit())
#
# sys.setrecursionlimit(2000)
#
#
#
# print(sys.getrecursionlimit())

# def greet():
#     print("hello")
#     greet()
#
# greet()

def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)

result = fact(10)
print(result)





