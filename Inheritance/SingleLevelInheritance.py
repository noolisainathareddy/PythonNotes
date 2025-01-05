#This is single level Inheritance
class A:
    def feature1(self):
        print("This is feature 1")

    def feature2(self):
        print("This is feature 2")


class B(A):
    def feature3(self):
        print("This is feature 3")

    def feature4(self):
        print("This is feature 4")

obj = B()

obj.feature1()
obj.feature2()
obj.feature3()
obj.feature4()
