from StudExCurr import StudExCurr
from TeacherDetails import TeacherDetail
ColCode=input('Enter College Code: ')
ColName=input('Enter College Name: ')
"""
rollNo = int(input("Enter roll no: "))
sname = input("Enter student name: ")
m1 = int(input("Enter mark 1: "))
m2 = int(input("Enter mark 2: "))
m3 = int(input("Enter mark 3: "))
exm1=int(input("Enter exam 1: "))
exm2=int(input("Enter exam 2: "))

student= StudExCurr(colcode,colcode,rollNo,sname,m1,m2,m3,exm1,exm2)

print(f'{student.display()[0]} \t {student.display()[1]}')
print(f'RollNo: {student.get_rollNo()} \nName: {student.get_sname()}\nTotal: {student.Calc_total()}\n'f'Average: {student.calc_avg()}')
print(f'{student.calc_extot()}')"""

TeacherId = int(input("Enter Teacher ID: "))
TeacherName = input("Enter Teacher Name: ")
Dept = input("Enter Dept ID: ")
teacher = TeacherDetail(ColCode,ColName,TeacherId,TeacherName,Dept)
teacher.display()