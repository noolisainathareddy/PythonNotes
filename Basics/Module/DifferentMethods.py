class Computer:

    school = 'Narayana'

    def mac(self):
        print("This is from Mac")

    @classmethod
    def getSchoolName(cls):
        print(cls.school)

    @staticmethod
    def info():
        print("This is a static Method")

Computer.getSchoolName()

comp = Computer()

comp.getSchoolName()
comp.mac()

Computer.info()