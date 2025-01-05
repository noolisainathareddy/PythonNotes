from Basics.Revision1.AnonymusFunc import result


def greet(text):
    print(text)

def wish(text):
    print(text)

def receive(func):
    warm = func("Welcome my dear")
    print(warm)

receive(wish)
receive(greet)


def add(x):
    def mul(y):
        return x*y
    return mul

result1 = add(5)

print(result1(30))

