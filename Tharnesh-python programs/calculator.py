def calculator():
    operator=eval(input("what do you want to do:"))
    operators=('+','-','*','/','%')
    if operator not in operators:
        print("Invalid operator! please enter another operator")
        calculator()
    else:
        if operator=='+':
            a=eval(input("Enter the value for a:"))
            b=eval(input("Enter the value for b:"))
            c=a+b
            print("Sum of the two numbers is:",c)
            calculator()
        elif operator=='-':
            a=eval(input("Enter the value for a:"))
            b=eval(input("Enter the value for b:"))
            c=a-b
            print("Difference between two numbers is:",c)
            calculator()
        elif operator=='*':
            a=eval(input("Enter the value for a:"))
            b=eval(input("Enter the value for b:"))
            c=a*b
            print("Multiplication of two numbers is:",c)
            calculator()
        elif operator=='/':
            a=eval(input("Enter the value for a:"))
            b=eval(input("Enter the value for b:"))
            c=a/b
            print("Division of two numbers is:",c)
            calculator()
        else:
            a=eval(input("Enter the value for a:"))
            b=eval(input("Enter the value for b:"))
            c=a%b
            print("modulo of two numbers is:",c)
            calculator()
calculator()


