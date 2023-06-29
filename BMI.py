weight_kg = input("enter your weight in kgs")
height_me = input("Enter your height in metres")
weight = float(weight_kg)
height = float(height_me)
result = weight / (height * height)
if result <= 18:
    print(result, "underweight")
elif result <= 29:
    print(result, "normal weight")
elif result <= 34:
    print(result, "overweight")
elif result >= 34.1:
    print(result, "obese")
else:
    print("invalid")
