def twoSum(nums, target):
    for i in range (0,len(nums)):
        a = i+1
        for j in range (a, len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]



# lst = [10,20,30,40]
# for i in lst:
#     print(format("value {} with index of {}").format(i, lst.index(i)))

# print(twoSum([2,7,11,15], 9))


vals = [10,20,30,40]

for i in range (0, len(vals)):
    print(i)