num = int(input("Enter a number: "))
x = num
rev = 0
while x > 0:
    d = x % 10
    rev = rev*10+d
    x = x//10
if rev == num:
    print(num,"is a palindrome")
else:
    print(num,"is not a palindrome")