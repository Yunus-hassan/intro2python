def weight():
    weight = float(input("enter weight in kg"))
    height = float(input("enter height in metres"))
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




weight()
