n = 5

# for i in range(n):
#     print("i",i)
#     if i==2:
#         continue
#     print("Last line i", i)

m=5
for i in range(n):
    print("i",i)
    for j in range(m):
        print('j',j)
        if j ==2:
            break
        print("Last line in J", j)
    print("Last line i", i)