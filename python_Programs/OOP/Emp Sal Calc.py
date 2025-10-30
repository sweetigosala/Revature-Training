from OOP.Employee import Employee


empId = int(input('Enter Employee ID : '))
empName = input('Enter Employee Name : ')
bp = float(input('Enter Basic pay : '))
emp = Employee(empId, empName, bp)

print(f'EmpId : {empId}')
print(f'Employee Name : {empName}')
print(f'Basic pay : {bp}')
print(f'Gross Pay :{emp.calc_grosspay()}')
print(f'Net Pay :{emp.calc_netpay()}')

