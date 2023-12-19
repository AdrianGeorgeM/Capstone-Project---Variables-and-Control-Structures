# User selection
choice = input("Choose 'investment' or 'bond': ").lower()

# Investment calculator
if choice == "investment":
    amount = float(input("How much are you depositing? "))
    rate = float(input("Interest rate (as a percentage): ")) / 100
    years = int(input("Number of years investing: "))
    interest_type = input("Type 'simple' or 'compound' interest: ").lower()

    if interest_type == "simple":
        total = amount * (1 + rate * years)
    else:  # Assuming compound interest
        total = amount * ((1 + rate) ** years)

    print(f"Total amount after {years} years: {total}")

# Bond calculator
elif choice == "bond":
    house_value = float(input("Value of the house: "))
    interest_rate = float(input("Annual interest rate (as a percentage): ")) / 100 / 12
    months = int(input("Repayment period in months: "))

    repayment = house_value * interest_rate / (1 - (1 + interest_rate) ** -months)
    print(f"Monthly repayment: {repayment}")

else:
    print("Invalid choice. Please type 'investment' or 'bond'.")
