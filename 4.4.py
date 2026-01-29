yr = int(input("Enter the year"))
if (yr % 4 == 0):
    if (yr % 100 == 0):
        if (yr % 400 == 0):
            print("year is leap")
        else:
            print("not leap yr")
    else:
        print("year is leap")
else:
    print("not leap yr")
