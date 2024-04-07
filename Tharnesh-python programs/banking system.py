username1="Tharnesh"
password1=2003
username=str(input("Enter the username:"))
password=eval(input("Enter the password:"))
acbalance=0
def bank_ac():
    acbalance=0
    if(username==username1 and password==password1):
        print("your account was logged in successfully")
        print("1.check bank balance")
        print("2.deposit")
        print("3.withdraw")
        opt=eval(input("what do you want do do?"))
        if opt==2:
            deposit=eval(input("Enter the amount:"))
            ac_balance1=0+deposit
            print("After deposit your account balance is:",deposit)
            bank_ac()
        elif opt==3:
            withdraw=eval(input("Enter the amount to withdraw:"))
            if withdraw>ac_balance1:
                print("no sufficient amount please enter another amount")
            else:
                print("The amount is withdrawn successfully")
                withdrawal=acbalance-withdraw
                print("After withdrawal the balance is:",withdrawal)
                return acbalance
                bank_ac()
        else:
            ac_balance1=0+deposit
            print("your account balance is:",acbalance1)
bank_ac()
        
    


