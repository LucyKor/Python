print("Welcome and find out your BMI.")
height = float(input("What is your height in meters? "))
weight = int(input("What is your weight in kilograms? "))

result = weight / (height ** 2)

if result < 18.5:
    print(f"Your BMI is {result}, you are underweight.")
elif result >= 18.5 and result < 25:
    print(f"Your BMI is {result}, you have a normal weight.")
elif result >= 25 and result < 30:
    print(f"Your BMI is {result}, you are slightly overweight.")
elif result >= 30 and result < 35:
    print(f"Your BMI is {result}, you are obese.")
else:
    print(f"Your BMI is {result}, you are clinically obese.")