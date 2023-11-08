#Swapping two numbers
a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))

print("The numbers before swapping: ")
print("1st Number: ",a)
print("2nd Number: ",b)

a=a+b
b=a-b
a=a-b

print("The numbers after swapping: ")
print("1st Number: ",a)
print("2nd Number: ",b)

