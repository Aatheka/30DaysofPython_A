#Time of the day

T=int(input("Enter the time: "))

if T<0:
    print("Invalid")
elif 0<=T<=5:
    print("Night")
elif 6<=T<=11:
    print("Morning")
elif 12<=T<=17:
    print("Afternoon")
elif 18<=T<=23:
    print("Evening")
elif 24<=T:
    print("Invalid")
    
    
