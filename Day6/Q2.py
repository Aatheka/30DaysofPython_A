#Printing first n integers

n= int(input("Enter the number: "))

if int(n)>0:
    for i in range(n):
        if i==n-1:
            print(i)
        else:
            print(i,end=",")
else:
    print("Enter a positive integer.")
