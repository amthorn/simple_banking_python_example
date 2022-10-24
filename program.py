# Set balance to 0 initially. Will reset when program terminates
balance = 0

while True:
    print("What would you like to do?")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    selection = input("Please enter the number of your selection: ")

    if not selection.isdigit() or int(selection) < 1 or int(selection) > 4:
        print("That is not a valid selection. Please select a number between 1 and 4.")
        continue
    
    selection = int(selection)
    if selection == 1:
        print("Balance is: $", balance)
    elif selection == 2:
        while True:
            amount = input("> How much would you like to deposit? ")
            if not amount.isdigit() or int(amount) < 1 or int(amount) > 999:
                print("That is not a valid amount. Please choose a number between 1 and 999")
                continue
            
            amount = int(amount)
            
            balance += amount
            print("New balance is: $", balance)
            break
    elif selection == 3:
        while True:
            amount = input("> How much would you like to withdraw? ")
            if not amount.isdigit() or int(amount) < 1 or int(amount) > 999:
                print("That is not a valid amount. Please choose a number between 1 and 999")
                continue
            elif int(amount) > balance:
                print("You do not have enough funds! Please withdraw equal to or less than: $", balance)
                continue
            amount = int(amount)
            
            balance -= amount
            print("New balance is: $", balance)
            break
    else:
        break