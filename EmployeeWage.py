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

employee_status = randint(0,2)

def employeeCheckFunc(Status):
    workingHrs = {
        1 : 8,
        2 : 4
    }
    return workingHrs.get(Status,0)


if employeeCheckFunc(employee_status) == 0:
    print("Employee is absent")
elif employeeCheckFunc(employee_status) == 1:
    print("Employee is present and works full time")
else:
    print("Employee is present and works part time")

wage = employeeCheckFunc(employee_status) * wage_per_hour
print("Wage earned =",wage)
