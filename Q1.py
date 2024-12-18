#Q1] WAP to calculate simple interest

#Constant value
rate_of_interest=5

#Input values
principal = float(input("Enter the principal amount: "))

time = float(input("Enter the time in years: "))

#Calculation
simple_interest = (principal*rate_of_interest*time)/100

#Output
print("The simple interest is: ",simple_interest)
