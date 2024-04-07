str=str(input("Enter a string:"))
str_list=("break","case","continue","default","defer","else","for","func","goto","if","map","range","return","struct","type","var")
if str in str_list:
    print(str,"is a keyword")
else:
    print(str,"is not a keyword")
