class A:

    def __init__(self):
        print("In A init")

    def feature1(self):
        print("This is feature1")


class B(A):

    def __init__(self):
        super().__init__()
        print("In B init")

    def feature2(self):
        print("This is feature 2")

obj = B()


#Method resolution order --> Left to Right
#C(A,B)