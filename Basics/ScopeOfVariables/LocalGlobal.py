
global a
a = "this is global a "
print(a)
print(a)
def hello():
    a= "This is a"
    print(a)


hello()
print(a)
a = " This is at the end"

print(a)
hello()
print(a)

print("---------------------------------")
b = "This is b"
print(b)
def bye():
    global b
    b = " Inside b"
    print(b)

bye()
print(b)

def bye2():
    global b
    b = "Thi is bye2"
    print(b)

bye2()
print(b)




