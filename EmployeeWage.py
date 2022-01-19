'''
@Author: Jayanand

@Date: 19-01-2022

@Last Modified by: Jayanand

@Last Modified time: 19-01-2022

@Title : Employee daily wage computation.
'''

from random import randint

wage_per_hour = 20
full_day_workingHrs = 8

employee_status = randint(0,1)

if employee_status == 0:
    print("Employee is absent")
else:
    print("Employee is present")
    wage = full_day_workingHrs * wage_per_hour
print("Wage earned =",wage)