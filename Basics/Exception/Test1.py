a= 7
b=0

try:
   print(7/0)


except Exception as e:
    print("Exception : ", e)
finally:
    print("close all tabs")