class Car:
    #staic/class variable
    wheels = 8

    def __init__(self):
        #instance variables
        self.mil = 28
        self.brand = "BMW"

c1=Car()

print(c1.wheels)
print(Car.wheels)
print(c1.mil)
print(c1.brand)