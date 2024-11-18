class Hello:
    def __init__(self, cpu, ram):
        self.cpu=cpu
        self.ram=ram


    def gree(self):
        print(self.cpu, self.ram)


comp1 = Hello('i5', '16gb')
comp2 = Hello('i7', '8gb')


comp1.gree()
comp2.gree()
