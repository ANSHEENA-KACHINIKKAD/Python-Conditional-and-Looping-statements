# Python Conditional and Looping statements
Basic python conditional and looping statements.

## Exercise-1
Name your file: MonthNames.py Write a program that reads an integer value between 1 and 12 from the user and prints output the corresponding month of the year.

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


## Exercise-2
A certain cinema currently sells tickets for a full price of 6 pounds, but always sells tickets for half price to people who are less than 16 years old, and for a third of the price for people who are 60 years old or more.

code:

    print("Cinema Tickets! ")
    price=6
    age=int(input("enter your age:"))
    if age <16:
    print("Your ticket price is",price/2,"pounds")
    elif 16 < age < 60:
    print("Your ticket price is ",price,"pounds")
    else:
    print("Your ticket price is",price//3,"pounds")

Explanation:

  * print("Cinema Tickets! "): This line simply prints the message "Cinema Tickets!" to the console.
  * price=6: This line declares a variable named price and assigns the value 6 to it. This represents the standard ticket price.
  * age=int(input("enter your age:")): This line prompts the user to enter their age. The input() function gets the user's input as a string. The int() function converts the input string to an integer, as 
    age is expected to be a whole number.
  * if age <16:: This is the first condition. If the user's age is less than 16:
    print("Your ticket price is",price/2,"pounds"): This line calculates the discounted price by dividing the price by 2 (i.e., half the price) and prints the discounted price.
  * elif 16 < age < 60:: This is the second condition. If the user's age is greater than 16 and less than 60:
    print("Your ticket price is ",price,"pounds"): This line prints the standard price for adults.
  * else:: This is the default condition. If none of the above conditions are met (i.e., if age is 60 or older):print("Your ticket price is",price//3,"pounds"): This line calculates the senior citizen 
    discount by using integer division (//). Integer division results in an integer by discarding any remainder. So, price//3 calculates the price divided by 3 and rounds it down to the nearest whole 
    number.

Result:
  ![Screenshot (236)](https://github.com/user-attachments/assets/46122588-2a77-409b-8283-34351ed50c0e)
  ![Screenshot (237)](https://github.com/user-attachments/assets/2fe97315-c4e8-4ee9-82d2-ef48adf6e467)
  ![Screenshot (238)](https://github.com/user-attachments/assets/5ff6f607-c501-483d-8eba-ac20bacca629)




  
