month_no=int(input("Enter the month :"))
month=["January","February","March","April","May","June","July","August","September","October","November","December"]
if 1<= month_no <=12:
    print(month[month_no-1])
else:
    print("enter valid month number")