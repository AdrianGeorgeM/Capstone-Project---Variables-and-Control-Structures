import math

# User selection
choice = input("Choose 'investment' or 'bond': ").lower()

# Investment calculator
if choice == "investment":
    P = float(input("Enter the amount of money you are depositing: "))
    r = float(input("Enter the interest rate (as a percentage): ")) / 100
    t = int(input("Enter the number of years you plan on investing: "))
    interest_type = input("Do you want 'simple' or 'compound' interest?: ").lower()

    if interest_type == "simple":
        A = P * (1 + r * t)
    else:  # Assuming compound interest
        A = P * math.pow((1 + r), t)

    print(f"Total amount after {t} years: {A}")

# Bond calculator
elif choice == "bond":
    P = float(input("Enter the value of the house: "))
    i = float(input("Enter the annual interest rate (as a percentage): ")) / 100 / 12
    n = int(input("Enter the number of months to repay the bond: "))

    repayment = P * i / (1 - math.pow((1 + i), -n))
    print(f"Monthly repayment: {repayment}")

else:
    print("Invalid choice. Please type 'investment' or 'bond'.")


# Testing Instructions

# Investment Calculator:
# 1. Run the script and choose 'investment' when prompted.
# 2. Enter the deposit amount (e.g., 1000).
# 3. Enter the interest rate as a percentage (e.g., 8 for 8%).
# 4. Enter the number of years for the investment (e.g., 5).
# 5. Choose 'simple' or 'compound' for the type of interest.
# 6. The script will display the total amount after the investment period.
# Formula for simple interest: A = P * (1 + r * t)
# Formula for compound interest: A = P * ((1 + r) ** t)

# Home Loan Repayment Calculator:
# 1. Run the script and choose 'bond' when prompted.
# 2. Enter the present value of the house (e.g., 100000).
# 3. Enter the annual interest rate as a percentage (e.g., 7).
# 4. Enter the number of months for repayment (e.g., 120).
# 5. The script will calculate and display the monthly repayment amount.
# Formula used: Repayment = (i * P) / (1 - (1 + i) ** -n)
# Where: P = Present value of the house, i = Monthly interest rate, n = Repayment period in months

# Example Tests:
# For the investment calculator, with an amount of 1000, interest rate of 8%, and a period of 5 years,
# the script should correctly calculate the total amount for both simple and compound interest.
# For the home loan calculator, with a house value of 100000, interest rate of 7%, and a repayment period of 120 months,
# the script should correctly calculate the monthly repayment amount.

