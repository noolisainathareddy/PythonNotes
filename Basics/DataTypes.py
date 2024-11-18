#This is my comment
print("Hello World!")
print('Welcome Sai!')


#Strings
first_name ="sai"
print(first_name)
print(f"Hello {first_name}")
email= "sai123@gmail.com"


#Integers

age=23
quantity=3.5
num_of_students=30


#float
price=10.99
gpa=3.47
distance=2.5

#boolean

is_human = True
is_null = False

if is_human:
    print("He is a human")
else:
    print("He is not a human")

if is_human:
    print("He is human")
else:
    if is_null:
        print("It not a null value")
    else:
        print("Nothing matched")

if is_human:
    print("He is not a human")
elif is_null:
    print("It's a null value")
else:
    print("No matched records/value")