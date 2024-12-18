# Function to generate the multiplication table
def print_table(number):
    print(f"Multiplication Table for {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Input from the user
num = int(input("Enter a number to get its multiplication table: "))

# Call the function
print_table(num)
