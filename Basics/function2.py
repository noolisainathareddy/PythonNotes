

def nums(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2==0:
            even +=1
        else :
            odd +=1
    return even, odd


lst = [10,40,61,30,20,71,50,80,91]

even, odd = nums(lst)

print("even : {} , odd : {}".format(even,odd))