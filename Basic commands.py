Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
5 and 9
9
5 or 9
5
not 5
False
not 9
False
5 & 9
1
5 | 9
13
5^9
12
5<<3
40
5<<4
80
5>>2
1
num1=19
type(num1)
<class 'int'>
type(num1) is int
True
type(num1) is not str
True
type('str') is not str
False
>>> print('hi'+'hello')
hihello
>>> print(num1+30)
49
>>> print('hi'+'10')
hi10
>>> print('sum :',num1+10)
sum : 29
>>> print('sum: '+'\n',50_60)
sum: 
 5060
>>> print('sum: '+'\n',50+60)
sum: 
 110
>>> int(input('enter a num'))
enter a num9
9
>>> float(input('enter a num'))
enter a num 6
6.0
>>> bool(input('enter a num'))
enter a num0
True
>>> str1='sweeti'
>>> str1
'sweeti'
>>> print(str1)
sweeti
>>> len(str1)
6
>>> len('hello world')
11
>>> print(str1[3])
e
>>> print(str1[-5])
w
list1=[1,2,3,4,5]
print(list1)
[1, 2, 3, 4, 5]
id(list1)
1778027025536
list1.append(6)
list1
[1, 2, 3, 4, 5, 6]
id(list1)
1778027025536
>>> list[2]
list[2]
>>> list1[2]
3
>>> list1.count(10)
0
>>> list1[3]=100
>>> list1
[1, 2, 3, 100, 5, 6]
>>> list1.index(100)
3
>>> list1.insert(4,50)
>>> list1
[1, 2, 3, 100, 50, 5, 6]
>>> list1.remove(100)
>>> list1
[1, 2, 3, 50, 5, 6]
>>> list1.pop()
6
>>> list1.pop(-2)
50
>>> list1.reverse()
>>> list1
[5, 3, 2, 1]
>>> list1.sort()
>>> list1
[1, 2, 3, 5]
>>> list1.sort(reverse=True)
>>> list1
[5, 3, 2, 1]
>>> list1.extend([60,70])
>>> list1
[5, 3, 2, 1, 60, 70]
