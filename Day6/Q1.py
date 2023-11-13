#Sum of digits in a number

n= input("Enter the number: ")
sum=0

if int(n)>0:
    for i in range(len(n)):
        digit= int(n[i])
        sum+=digit
    print("The sum of the digits of the given number is",sum)
else:
    print("Enter a positive integer.")
