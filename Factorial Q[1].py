# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Input from the user
number = int(input("Enter a number to find its factorial: "))

# Checking if the number is negative
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Call the factorial function and display the result
    print(f"The factorial of {number} is {factorial(number)}")
