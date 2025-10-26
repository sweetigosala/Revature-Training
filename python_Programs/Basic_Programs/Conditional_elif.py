'''Date : 25-10-2025
Author : Gosala Sweeti
Description : Conditional statements '''

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
if num1==num2:
    print("Both numbers are same")
elif num1 > num2:
    print(f'{num1} is greater than {num2}')
else:
    print("{} is less than {}".format(num1,num2))

