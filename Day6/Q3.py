#Factors of n

n= int(input("Enter the number: "))
print(f"The factors of {n} are:")

if int(n)>0:
    for i in range(1,n+1):
        if n%i==0:
            print(i)
else:
    print("Enter a positive integer.")
