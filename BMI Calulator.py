#BMI Calulator
weight = float(input("What is your weight? "))
height = float(input("How tall are you in metres?  "))
height *= height
bmi = weight/height

if bmi < 18.5:
    print("You are underweight.")
elif bmi >= 18.5 and bmi < 25.0:
    print("You are normal.")
elif bmi >=25.0 and bmi < 30.0:
    print("You are overweight")
else:
    print("You are Obese")