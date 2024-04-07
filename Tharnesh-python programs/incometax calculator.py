income=45000
if income<=10000:
    tax=0
elif income<=20000:
    x=income-10000
    tax=(x*10)/100
else:
    tax=10000*10/100
    tax+=(income-20000)*20/100
print(tax)
