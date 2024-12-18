# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Using conditional statement to find the greatest number
if num1 > num2:
    print(f"The greatest number is {num1}")
elif num2 > num1:
    print(f"The greatest number is {num2}")
else:
    print("Both numbers are equal.")
