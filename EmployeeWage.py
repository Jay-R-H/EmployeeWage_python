'''
@Author: Jayanand

@Date: 19-01-2022

@Last Modified by: Jayanand

@Last Modified time: 19-01-2022

@Title : Employee wage computation for part time and full time.
'''

from random import randint

wage_per_hour = 20
full_day_workingHrs = 8
part_time_workingHrs = 4

employee_status = randint(0,2)

if employee_status == 0:
    print("Employee is absent")
    workingHrs = 0
elif employee_status == 1:
    print("Employee is present and works full time")
    workingHrs = 8
else:
    print("Employee is present and works part time")
    workingHrs = 4

wage = workingHrs * wage_per_hour
print("Wage earned =",wage)