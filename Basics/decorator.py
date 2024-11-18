def div(a,b):
    return a/b


def smart_dev(func):
    def inner(a,b):
        if a < b:
            a,b=b,a
        return func(a,b)
    return inner

div = smart_dev(div)

print(div(2,4))