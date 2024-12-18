# Function to find the maximum of two numbers
def find_maximum(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

# Input from the user
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Call the function and display the result
maximum = find_maximum(number1, number2)
print(f"The maximum of {number1} and {number2} is {maximum}")
