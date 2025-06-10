
pin = "1234"
balance = 1000.0
transactions = []


print("\n🚀 Welcome to Simple ATM 🏦")
print("---------------------------")


attempts = 3
while attempts > 0:
    user_pin = input("Enter your 4-digit PIN: ")
    if user_pin == pin:
        break
    attempts -= 1
    print(f"Wrong PIN! {attempts} attempts left.")
    
if attempts == 0:
    print("Too many wrong attempts. Card blocked.")
    exit()


while True:
    print("\nWhat would you like to do?")
    print("1. Check Balance 💰")
    print("2. Deposit Money 🏦")
    print("3. Withdraw Money 💸")
    print("4. Exit 🚪")
    
    choice = input("Enter choice (1-4): ")
    
   
    if choice == '1':
        print(f"\nYour balance: ${balance:.2f}")
        transactions.append("Checked balance")
    
   
    elif choice == '2':
        try:
            amount = float(input("Enter deposit amount: $"))
            if amount > 0:
                balance += amount
                print(f"\nDeposited ${amount:.2f} successfully!")
                transactions.append(f"Deposited ${amount:.2f}")
            else:
                print("Amount must be positive!")
        except:
            print("Invalid amount!")
    
  
    elif choice == '3':
        try:
            amount = float(input("Enter withdrawal amount: $"))
            if amount > balance:
                print("Not enough money!")
            elif amount > 0:
                balance -= amount
                print(f"\nWithdrew ${amount:.2f} successfully!")
                transactions.append(f"Withdrew ${amount:.2f}")
            else:
                print("Amount must be positive!")
        except:
            print("Invalid amount!")
    
   
    elif choice == '4':
        print("\nThank you for using our ATM!")
        if transactions:
            print("\nLast few transactions:")
            for t in transactions[-3:]:  
                print(f"- {t}")
        break
    
    
    else:
        print("Please enter 1-4!")