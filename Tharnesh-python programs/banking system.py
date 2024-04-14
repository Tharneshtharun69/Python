username1 = "Tharnesh"
password1 = 2003
def bank_ac():
    acbalance = 0
    username = input("Enter your username: ")
    password = int(input("Enter your password: "))
    if username == username1 and password == password1:
        print("Your account was logged in successfully")
        while True:
            print("1. Check bank balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            opt = int(input("What do you want to do? "))
            if opt == 1:
                print("Your account balance is:", acbalance)
            elif opt == 2:
                deposit = int(input("Enter the amount to deposit: "))
                acbalance += deposit
                print("After deposit, your account balance is:", acbalance)
            elif opt == 3:
                withdraw = int(input("Enter the amount to withdraw: "))
                if withdraw > acbalance:
                    print("Insufficient funds")
                else:
                    acbalance -= withdraw
                    print("The amount is withdrawn successfully")
                    print("After withdrawal, the balance is:", acbalance)
            elif opt == 4:
                print("Thank you for using our banking system")
                break
            else:
                print("Invalid option")
    else:
        print("Invalid username or password")
bank_ac()
