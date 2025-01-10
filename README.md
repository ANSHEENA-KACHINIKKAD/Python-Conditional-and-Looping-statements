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


## Exercise-3
Name your file: BodyMassIndex.py Write a program to calculate your BMI and give weight status. Body Mass Index (BMI) is an internationally used measurement to check if you are a healthy weight for your height.The metric BMI formula accepts weight in kilograms and height in meters: BMI= weight(kg)/height2(m2) BMI Weight Status Categories table BMI range - kg/m2 Category Below 18.5 Underweight 18.5 -24.9 Normal 25 - 29.9 Overweight 30 & Above Obese 

code:

    weight=float(input("Enter your weight in (kg):"))
    height=float(input("Enter your height in (m):"))
    BMI=weight/(height**2)
    if BMI<18.5:
    print('You are in the "under weight" range')
    elif 18.5<= BMI <=24.9 :
    print('You are in the "normal" range')
    elif 25<= BMI <=29.9 :
    print('You are in the "over wight" range')
    else:
    print('You are in the "obese" range')

Explanation:
  
  * prompts the user to enter their weight in kilograms.
  * prompts the user to enter their height in meters.
  * The formula for BMI is weight (in kilograms) divided by the square of height (in meters).
  * If the if condition (BMI < 18.5) is true, this line prints the message "You are in the "under weight" range".
  * if BMI is greater than or equal to 18.5 and less than or equal to 24.9. prints the message "You are in the "normal" range".
  * if BMI is greater than or equal to 25 and less than or equal to 29.9. print over weight.
  * if BMI is equal or above 30 then it prints obese.

Result:
  ![Screenshot (244)](https://github.com/user-attachments/assets/b6f886bb-f938-4e3e-899d-6aed40223405)



## Exercise-4
Write a Python program to receive 3 numbers from the user and print the greatest among them.

code:

    li=[]
    for i in range(3):
    n=int(input("enter the number:"))
    li.append(n)
    print(max(li))

Explanation:
  
  * creates an empty list named li.
  * The loop will execute three times, with the variable i taking on the values 0, 1, and 2 in each iteration.
  * adds the entered integer (n) to the end of the list li using the append() method.
  * max() is a built-in function in Python that finds the largest value within a list.
  

Result:
  ![Screenshot (245)](https://github.com/user-attachments/assets/aaf35fac-a7ac-44fb-bc1f-3fbbf65eb1f5)



## Exercise-5
Find the factorial of a given number using loops(note the number is received from the user

code:

    n=int(input(" enter the number:"))
    num=n
    fact=1
    while n!=0:
    fact=fact*n
    n=n-1

    print(" factorial of",num,"is",fact)

Explanation:
  
  * takes an integer input from the user and stores it in the variable n.
  * This line initializes a variable fact to 1. This variable will be used to store the calculated factorial.
  * while loop that continues to execute as long as the value of n is not zero.
  * multiplies the current value of fact with the current value of n and updates the fact variable.then decrements the value of n by 1 in each iteration of the loop.
  * prints the calculated factorial. It displays the original number (num) and the calculated factorial (fact).

  

Result:
  ![Screenshot (247)](https://github.com/user-attachments/assets/3c160c5f-dca0-4277-a8ce-a36d337b6e99)



## Exercise-6
 Reverse a number using while loop

code:

    n=int(input("Enter the number:"))
    reverse=0
    while n!=0:
    digit=n%10
    reverse=10*reverse+digit
    n=n//10
    print("reverse of the number is",reverse)

Explanation:
  
  * Get Input.
  * This line initializes a variable fact to 1. This variable will be used to store the calculated factorial.
  * Initialize Reverse.
  * extracts the last digit of the given input number,This appends the extracted digit to the 'reverse' variable,This removes the last digit from input by integer division.
  * Print Result.

  

Result:
  ![Screenshot (246)](https://github.com/user-attachments/assets/f3aa4c19-f360-41f7-b56c-69cd28f8a98d)

  


## Exercise-7
 Finding the multiples of a number using loop

code:

    n=int(input("enter the number:"))
    for i in range(1,11):
    print(i,"*", n ,"=", i*n)

Explanation:
  
  * Get Input.
  * loop iterates 10 times, with the variable 'i' taking values from 1 to 10 in each iteration,and prints the multiplication table of the input number 'n' by multiplying 'n' with each value of 'i' in the 
    loop.
  * Displays the multiplication table of the input number on the console.
  

  

Result:
  ![Screenshot (248)](https://github.com/user-attachments/assets/df62472b-0dea-4684-b978-37bff8ca8d66)




## Exercise-8
 Write a program to print the inputted value as it is and break the loop if the value is 'done'.

code:

    while  True:
    value = input("enter the value:")
    if value!='done':
        print(value)
    else:
        break

Explanation:
  
  * creates an infinite loop that continuously executes the code within it.
  * Then prompts the user to enter a value and stores it in the variable 'value'.
  * Then checks if the entered value is not equal to the string "done".If the condition is True,prints the entered value to the console.
  * If the entered value is equal to "done" then break and exit from the loop and end the programme.
  
  

  

Result:
  ![Screenshot (249)](https://github.com/user-attachments/assets/500ceb93-d1b8-447d-b4e5-bc8f659a4410)



## Exercise-9
Program that prints the numbers from 1 to 10. But for multiples of three print "Fizz" instead of the number and for the multiple of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz"

code:

    for i in range(1,10):
    if i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    elif i%3 and i%5 ==0:
        print("FizzBuzz")
    else:
        print(i)

Explanation:
  
  * creates a  loop that iterates through numbers from 1 to 9 (inclusive).
  * checks if the current number 'i' is divisible by 3, then print "Fuzz"
  * checks if the current number 'i' is divisible by 5,then print "Buzz"
  * checks if the current number 'i' is divisible by 5 and 3,then print "FuzzBuzz"
  * Otherwise print the same number .
    
  
  
  

  

Result:
  ![Screenshot (250)](https://github.com/user-attachments/assets/2245f150-cd53-43a4-9a3f-fca92a9b6099)

