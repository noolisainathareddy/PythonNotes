class Laptop:
    def execute(self):
        print("Hello world")
        print("Welcome to my world")

class Mac:
    def execute(self):
        print("Hello world")
        print("Welcome to my world")
        print("This is mac")
        print("More advanced version of Mac")

class Student:
    def info(self, ide):
        ide.execute()

m = Mac()
lap = Laptop()
s = Student()

s.info(m)
