# Ask user for balance and deposit
initial_balance = float(input("Enter Initial Balance: "))
deposit = float(input("Enter Deposit Amount: "))

# Calculate new balance
new_balance = initial_balance + deposit

# Display results
print("Initial Balance:", initial_balance)
print("Deposit:", deposit)
print("New Balance after deposit:",new_balance)