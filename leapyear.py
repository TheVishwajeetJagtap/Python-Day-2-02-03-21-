year=int(input("Enter Year: "))
if(year>999):
    if(year%4 == 0):
        if(year%100 == 0):
            if(year%400 == 0):
                print(year," is a Leap Year")
            else:
                print(year," is Not the Leap Year because its a centurial year")
        else:
            print(year," is a Leap Year")
    else:
        print(year," is Not the Leap Year")
else:
    print("Wrong Entry")
