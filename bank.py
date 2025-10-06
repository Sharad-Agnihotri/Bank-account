# Ask user for balance and deposit
initial_balance = float(input("Enter Initial Balance: "))
deposit = float(input("Enter Deposit Amount: "))

# Calculate new balance
new_balance = initial_balance + deposit

# Display results
print("Initial Balance:", initial_balance)
print("Deposit:", deposit)
print("New Balance after deposit:",new_balance)



# Ask user for balance, deposit, and withdrawal
initial_balance = float(input("Enter Initial Balance: "))
deposit = float(input("Enter Deposit Amount: "))

# Calculate balance after deposit
balance_after_deposit = initial_balance + deposit
print("Initial Balance:", initial_balance)
print("Deposit:", deposit)
print("New Balance after deposit:", balance_after_deposit)

# Withdrawal feature
withdraw = float(input("Enter Withdrawal Amount: "))

# Check if sufficient funds
if withdraw <= balance_after_deposit:
    new_balance = balance_after_deposit - withdraw
    print("Amount Withdrawn:", withdraw)
    print("New Balance after withdrawal:", new_balance)
else:
    print("Insufficient balance!")