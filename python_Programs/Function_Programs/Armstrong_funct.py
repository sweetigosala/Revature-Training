def armstrong(num):
    return sum ([int (i) ** len(str(num)) for i in str(num)])==num
num=int(input("Enter a number: "))
print(armstrong(num))