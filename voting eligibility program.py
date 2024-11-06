#a program to check if one is eligible to vote
age=int(input("Please enter your age:"))
if age>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")



# A program to grade students based on their marks
marks=int(input("Enter your marks:"))
if marks>80 and marks<=100:
    print("You have an A")
elif marks<=79 and marks>=60:
    print("You have a B")
elif marks<=59 and marks>=40:
    print("You have a C")
elif marks==0 and marks<=39:
    print("You have failed")
else:
    print("Invalid marks")



# Taking user inputs for weight and height
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculating BMI
bmi = weight / (height ** 2)

# Display the calculated BMI
print(f"Your BMI is: {bmi:.2f}")

# Conditional checks based on the calculated BMI
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 24.9:
    print("Normal weight")
elif 25 <= bmi < 29.9:
    print("Overweight")
else:
    print("Obesity")
