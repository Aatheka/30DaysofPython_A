#Check if a year is a Century year

year= input("Enter any year: ")

if (year[2:]=="00"):
    print("The year",year, "is a Century year")
else:
    print("The year",year, "is not a Century year")
    
