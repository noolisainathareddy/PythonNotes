print("Enter your scores below : ")
n = int(input())
arr = map(int, input().split())
nums = list(arr)

nums.sort()

print(nums)
lenArr = n
while n > 0:
    y = nums[n - 1]
    x = nums[n - 2]
    if x < y:
        print(x)
        break
    n = n - 1
    y = nums[n - 1]
    x = nums[n - 2]
