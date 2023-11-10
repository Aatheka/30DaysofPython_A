#Fahrenheit to Celsius and Celsius to Fahrenheit

choice=int(input("1.Convert from From Fahrenheit to Celsius.\n2.Convert from Celsius to Fahrenheit.\nEnter you Choice:"))


if choice==1:
    fah=eval(input("Enter the temperature in Fahrenheit: "))
    cel=(fah-32)*5/9
    print(fah," degrees Fahrenheit is equal to",cel,"degrees Celsius")

elif choice==2:
    cel=eval(input("Enter the temperature in Celsius: "))
    fah=(cel*9/5)+32
    print(cel," degrees Celsius is equal to",fah,"degrees Fahrenheit")

else:
    print("Enter a valid choice.")
