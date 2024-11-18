#Instance Method
#static Method
#Class Method

class School:

    place = "vempalli"


    def __init__(self):
        self.name = "Chaitanya HS"

    #Instance method
    def getSchoolPlace(self):
        return self.name

    #Class method
    @classmethod
    def SchoolZipcode(cls):
        return "school zipcode is 516349"

    #static method
    @staticmethod
    def schoolActive():
        return "school is active"


s1 = School()

print(s1.getSchoolPlace())

print(School.schoolActive())

print(School.SchoolZipcode())

