from database import Student

try:
    name = input("enter name\n")
    phone = input("enter phone number\n")
    age = input("enter age\n")
    gender = input("enter gender\n")
    student = input("enter studentcode\n")

    Student.create(name=name, phonenumber=phone, age=age, gender=gender, studentcode=student)
    print("User created successfully")
except:
    print("Failed to create user")
