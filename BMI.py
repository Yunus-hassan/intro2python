weight_kg = input("enter your weight in kgs")
height_me = input("Enter your height in metres")
weight = float(weight_kg)
height = float(height_me)
result = weight / (height * height)
print("your BMI is",result)