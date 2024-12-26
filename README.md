# Python-Conditional-and-Looping-statements
Basic python conditional and looping statements.

## Exercise-1
## Name your file: MonthNames.py Write a program that reads an integer value between 1 and 12 from the user and prints output the corresponding month of the year.

code:

    month_no=int(input("Enter the month :"))
    month=["January","February","March","April","May","June","July","August","September","October","November","December"]
    if 1<= month_no <=12:
    print(month[month_no-1])
    else:
    print("enter valid month number")

Explanation:
  
  * if 1 <= month_no <= 12: This condition checks if the entered month number is within the valid range (1 to 12).
  * print(months[month_no - 1]): If the month number is valid, it accesses the corresponding month name from the list using index (month_no - 1) and prints it.
  * else: If the month number is invalid, it prints an error message.

Result:
  ![Screenshot (235)](https://github.com/user-attachments/assets/92ce8a17-e6a5-48c6-94b5-c13d11743ce0)
