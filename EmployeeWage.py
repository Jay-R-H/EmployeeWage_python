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
max_working_days = 20
worked_days = 0
total_wage = 0

def employeeCheckFunc(Status):
        workingHrs = {
        1 : 8,
        2 : 4
        }
        return workingHrs.get(Status,0)

while worked_days <= max_working_days: 
    
    employee_status = randint(0,2)
    
    if employeeCheckFunc(employee_status) == 0:
        print("Employee is absent")
    else:
        if employeeCheckFunc(employee_status) == 1:
            print("Employee is present and works full time")
            worked_days+=1
        else:
            print("Employee is present and works part time")
            worked_days+=1

    wage = employeeCheckFunc(employee_status) * wage_per_hour
    total_wage += wage

print("Total Wage earned =",total_wage)
