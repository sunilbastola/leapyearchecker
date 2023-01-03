check_year = int(input("Please enter the year you want to check: "))

if check_year % 4 == 0:
    if check_year % 100 == 0:
        if check_year % 400 == 0:
            print("Is a leap year")
        else:
            print("Not a leap year.")
    else: print(f"{check_year} is a Leap year.")        
else:
    print("Not a leap year.")
