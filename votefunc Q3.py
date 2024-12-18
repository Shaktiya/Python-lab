# Function to check voting eligibility
def can_vote(age):
    if age >= 18:
        return True
    else:
        return False

# Input from the user
age = int(input("Enter your age: "))

# Check eligibility and display the result
if can_vote(age):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
