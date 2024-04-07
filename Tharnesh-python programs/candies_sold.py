n=10
for i in range(10):
    candiessold=int(input("Enter the number of candies sold:"))
    updatedcandy_count=n-candiessold
    if candiessold==10:
        print("The jar is empty")
    else:
        updatedcandy_count=n-candiessold
        print("Number_of_candies_sold=",candiessold)
        print("Number_of_candies_available=",n-candiessold)
        
