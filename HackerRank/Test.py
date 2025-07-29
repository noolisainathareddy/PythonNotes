from Basics.Revision1.Decorators.Prac3 import smart_div



def add(a,b):
    print(a/b)

def smart_div(func):

    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

add = smart_div(2,4)

