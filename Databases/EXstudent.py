from database import Student

users = Student.select()
# use forlop to display
for users in Student:
    print(users.name, users.contact, users.age, users.gender, users.studentcode)
