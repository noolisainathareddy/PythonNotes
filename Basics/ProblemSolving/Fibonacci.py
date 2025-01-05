
x = 1
y = 1
z = 0
for a in range(10):
    if z  < 1 :
        print("0, 1", end=", ")
    z = x + y
    print(z)
    x  , y = y,  z
