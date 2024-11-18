a=5
b=0

try:
    print(a/b)
except Exception as e:
    print("You can't divided by zero", e)

print("bye")

try:
    print(a/b)

except ZeroDivisionError as e:
    print("It can't be divided by zero")

except ValueError as e:
    print("Please provide value")

except Exception as e:
    print(e)

finally:
    print("Close all files")