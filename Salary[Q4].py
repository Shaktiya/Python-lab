# Taking input for basic salary
basic_salary = float(input("Enter your basic salary: "))

# Check if the salary is more than 50000
if basic_salary > 50000:
    # Calculating DA and HRA
    DA = 0.10 * basic_salary  # 10% DA
    HRA = 0.12 * basic_salary  # 12% HRA
    
    # Calculating total salary
    total_salary = basic_salary + DA + HRA
    
    # Displaying the total salary
    print(f"Dearness Allowance (DA): {DA}")
    print(f"House Rent Allowance (HRA): {HRA}")
    print(f"Total Salary: {total_salary}")
else:
    print("Salary is less than 50,000, no DA and HRA are applied.")
