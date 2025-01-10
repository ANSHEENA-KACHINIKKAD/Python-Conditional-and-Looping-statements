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

