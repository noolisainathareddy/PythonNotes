class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram=ram

    def mac(self):
        print(self.cpu, self.ram)


saimac = Computer("M1", 16)

hemamac = Computer("M2", 8)


saimac.mac()
hemamac.mac()