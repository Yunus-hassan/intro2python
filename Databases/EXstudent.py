from database import Student

users = Student.select()
#use forlop to display
for user in Student:
    print(user.name,user.phonenumber,user.age,user.gender,user.studentcode)