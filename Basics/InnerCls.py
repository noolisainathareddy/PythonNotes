class Student:

    def __init__(self, name, age):
        self.name=name
        self.age=age
        self.lap=self.Laptop


    def show(self):
        print(self.name, self.age)
      

    class Laptop:

        def __init__(self, brand, ram):
            self.brand=brand
            self.ram=ram

        def show(self):
            print(self.brand, self.ram)

s1 = Student("sai", 27)

s1.show()

s2 = Student.Laptop("Mac", "16gb")
s2.show()
