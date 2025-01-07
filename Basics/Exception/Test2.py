def valueValidator(a):
    if a < 0:
        raise ValueError("Value is less than zero")
    else:
        print(a)

try:
    a = -2
    valueValidator(a)
except Exception as e:
    print(e)