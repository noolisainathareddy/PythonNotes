#-------- Functional arguments---------------
#Formal arguments
def addtwo(a,b):
    print(a+b)

#Actual argument
addtwo(5,6)

#Keyword arguments
def addthree(a=10, b=20, c=30):
    print(a+b+c)

addthree()
addthree(70)
addthree(50,50)
addthree(50,50,50)

#Variable arguments
def mul(a, *b):
    print("Mul", a*b)

mul(2,3,4,5)

def info(name, **data):
    print(data)

info("sai", age=27, place="Austin", Company="Infosys" )