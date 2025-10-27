def anagram(str1,str2):
    str1=str1.lower()
    str2=str2.lower()
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False
str1=input("Enter a string: ")
str2=input("Enter another string: ")
print(anagram(str1,str2))