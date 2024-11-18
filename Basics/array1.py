import array

# val = array.array('i', [10,20,30,10])
#
# for x in val:
#     print(x)
#
# # print(len(val))
#
# # print(val.count(10))
#
# print(type(val))
#
# index=0
#
# while index < len(val):
#     print(val[index])
#     index +=1

val = array.array('i', [])

num = int(input("Enter the length of the array"))

i=0
for i in range(num):
    val.append(int(input("Enter you number")))
    i =+ 1;

print(val)