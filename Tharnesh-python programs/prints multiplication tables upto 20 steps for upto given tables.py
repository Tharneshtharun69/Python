upto_nth_table=eval(input("Enter upto which table you want to print:"))
upto_nth_steps=eval(input("Enter upto which step you want to print:"))
for i in range(1,upto_nth_table+1):
    for j in range(1,upto_nth_steps+1):
        result=j*i
        print(j,'x',i,'=',result)
