'''Date : 25-10-2025
Author : Gosala Sweeti
Description : Conditional statements'''

num1 = int(input('Enter First Number:'))
num2 = int(input('Enter Second Number:'))
num3 = int(input('Enter Third Number:'))
if num1 > num2:
    if num1 > num3:
        print(f"{num1} is Greater number")
    else:
        print(f"{num3} is Greater number")
else:
    if num2 > num3:
        print(f"{num2} is Greater number")
    else:
        print(f"{num3} is Greater number")
