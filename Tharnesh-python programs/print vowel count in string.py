count=0
a=str(input("Enter a string:"))
for i in a:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        count=count+1
print("There are",count,"vowels present in the string")
