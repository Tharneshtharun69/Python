str=str(input("Enter the string:"))
strlen=len(str)
for i in range(0,strlen - 1,2):
    print("index[",i,"]",str[i])
