# nums = [23, 56, "sai", "hema"]
#
# print(nums)
#
# print(type(nums))
#
# city = ["kadapa", "vempalli", "pdtr"]
#
#
# mis= [nums, city]
#
# print(mis)
#
# print(type(mis))

fruits = ["apple", "banana", "Papaya"]
nums = [23, 56, "sai", "hema"]
#
# print(fruits)

fruits.append("Pineapple")

fruits.append("apple")
#
# print(fruits)

fruits.extend(nums)
print(fruits)

# fruits.clear()
# print(fruits, "list of values")

vals = fruits.copy()

print(vals)

fruits.append("siva")

print(id(vals))

print(id(fruits))

print(fruits.count("apple"))

print(fruits.index("banana"))
print(fruits.index("apple"))

fruits.insert(0,"Watermelon")

print(fruits)

fruits.pop()
print(fruits)

fruits.remove("apple")
print(fruits)


marks = ["sai", "sas", "sai", "a", "b"]

marks.sort()

print(marks)