#Sum of integers divisible by a and b

a=int(input("Enter a value: "))
b=int(input("Enter b value: "))
sum=0

for i in range(1000,2001):
    if i%a==0 and i%b==0:
        sum+=i

print(f"The sum of all integers divisible by {a} and {b} is {sum}")
