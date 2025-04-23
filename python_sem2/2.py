# part1
basic = float(input("Enter the salary: "))
print("User's basic salary", basic)

# Calculating allowances
da = 0.7 * basic   # Dearness Allowance (70%)
ta = 0.3 * basic   # Travel Allowance (30%)
hra = 0.1 * basic  # House Rent Allowance (10%)

# Gross salary calculation
gross = basic + da + ta + hra

# Display the salary breakdown
print("\n Salary breakdown!")
print("Dearness allowance: ", da)
print("Travel allowance: ", ta)
print("House rent allowance: ", hra)
print("Net salary of employee is: ", gross)

# part2

# Arthmetic Operators
# taking input
number1 = int(input("enter first number: "))
number2 = int(input("enter second number: "))
# Result of arithmetic operations
print("Addition", number1+number2)
print("Subtraction", number1-number2)
print("Multiplication", number1*number2)
print("Division", number1/number2)
print("Modulus", number1%number2)