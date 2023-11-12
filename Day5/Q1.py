#Sharing gold coins

n=int(input("Enter the number of gold coins with you: "))
a=int(input("Enter the no.of coins given to 1st friend: "))
b=int(input("Enter the no.of coins given to 2nd friend: "))
c=int(input("Enter the no.of coins given to 3rd friend: "))

if a!=b!=c!=0:
    if(n==(a+b+c)):
        print("Fair")
    else:
        print("Unfair")
else:
        print("Unfair")


