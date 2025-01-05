from tkinter.font import names


class Student:

    def __init__(self):
        self.name="sai"

    def student_name(self):
        print("My name is", self.name)

    def set_student_name(self,name):
        self.name = name

student = Student()
student.student_name()
student.set_student_name("Hema")
student.student_name()




