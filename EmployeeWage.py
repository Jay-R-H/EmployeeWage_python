'''
@Author: Jayanand

@Date: 19-01-2022

@Last Modified by: Jayanand

@Last Modified time: 19-01-2022

@Title : Employee Attendance status check
'''

from random import randint


employee_status = randint(0,1)

if employee_status == 0:
    print("Employee is absent")
else:
    print("Employee is present")