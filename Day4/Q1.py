#Check type of triangle

a=int(input("Enter length of 1st side: "))
b=int(input("Enter length of 2nd side: "))
c=int(input("Enter length of 3rd side: "))

if (a==b==c):
    print("The triangle is an Equilateral Triangle.")
elif (a==b or b==c or c==a):
    print("The triangle is an Isosceles Triangle.")
else:
    print("The triangle is a Scalene Triangle.")
