uid=int(input("enter your card no:"))
pasword=int(input("enter your possword"))
if uid==12345678 and pasword==2020:
    print("Select operation.")
    print("1. English")
    print("2. Tamil")
    print("3. Hindi")
    print("4. Telugu")

    a = input("Select a language:")

    print("What method do you want to use?")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Balance checking")

    balance = 100000
    print("Your current balance is:", balance)

    choice = int(input("Select 1/2/3: "))
    if choice == 1:
        withdraw = int(input("Enter the amount to withdraw: "))
        if withdraw <= balance:
            print("Withdraw amount:", withdraw, "$")
            balance -= withdraw
            print("Remaining balance:", balance)
        elif choice == 2:
            deposit = int(input("Enter the amount to deposit: "))
            print("Deposit amount:", deposit, "$")
            balance += deposit
            print("New balance:", balance)
        else:
            print("Your current balance is:", balance)
else:
    print ("login credentials are incorrect")