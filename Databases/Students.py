from database import Student

try:
    nam = input("enter name\n")
    phone = input("enter phone number\n")
    age = input("enter age\n")
    gender = input("enter gender\n")
    student = input("enter studentcode\n")

    Student.create(name=nam, contact=phone, age=age, gender=gender, studentcode=student)
    print("User created successfully")
except:
    print("Failed to create user")
