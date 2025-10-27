def fact(sum):
    if sum==1:
        return 1
    return sum*fact(sum-1)
sum=int(input("Enter a number: "))
print(fact(sum))