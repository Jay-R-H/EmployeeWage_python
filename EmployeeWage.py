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
max_working_hrs = 100
worked_hrs = 0

def getWorkingHrs(status):
    workingHrs = {
        1 : 8,
        2 : 4
        }
    return workingHrs.get(status,0)

while (worked_days < max_working_days) and (worked_hrs < max_working_hrs): 
    
    employee_status = randint(0,2)

    emp_Hrs = getWorkingHrs(employee_status)

    if emp_Hrs == 0:
        print("Employee is absent")
    else:
        if emp_Hrs == 1:
            print("Employee is present and works full time")
            worked_days+=1
            if worked_hrs + emp_Hrs > 100:
                break
            else:
                worked_hrs += emp_Hrs
        else:
            print("Employee is present and works part time")
            worked_days+=1
            if worked_hrs + emp_Hrs > 100:
                break
            else:
                worked_hrs += emp_Hrs

    wage = getWorkingHrs(employee_status) * wage_per_hour
    total_wage += wage
    print("Daily wage",wage,"Total wage",total_wage)
  

print("Total Wage earned =",total_wage)
print("Total hrs worked" , worked_hrs,"Total days worked",worked_days)
