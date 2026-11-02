# Aidan Davis
# 11/1/2026
# P4HW2
#Using a sentinel loop to process employees and calculate money

#Creating an employee name variable for our sentinel loop
employee_name = ''
#Assigning variables we will need later
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0
#Starting out while loop
while employee_name != "Done":
    employee_name = input("Enter Employee name or 'Done' to stop: ")
#Now Getting information from the user about the employee if they chose to not end the program
    if employee_name != "Done":
        employee_hours = float(input(f"How many hours did {employee_name} work? "))
        pay_rate = float(input(f"What is {employee_name}'s pay rate? "))
#Calculating amount of overtime worked and payrate without overtime
        if employee_hours > 40:
            overtime = employee_hours - 40
            regular_pay = 40* pay_rate
        else:
            overtime = 0
            regular_pay = employee_hours * pay_rate
#Calculating overtime pay itself
        if overtime > 0:
            overtime_pay = overtime * 1.5 * pay_rate
        else:
            overtime_pay = 0
#Calculating the gross total pay of everything
        gross_pay = overtime_pay + regular_pay

#Adding information to our total variable
        total_overtime_pay += overtime_pay
        total_regular_pay += regular_pay
        total_gross_pay += gross_pay
        employee_count += 1

        

        

#Printing everything out
        print(f"Employee name: {employee_name}")
        print(f"{'Hours Worked' :<20}{'Pay Rate' :<19}{'OverTime' :<19}{'OverTime Pay' :<20}{'RegHour Pay' :<20}{'Gross Pay'}")
        print(f"{employee_hours :<20.1f}{pay_rate :<19.2f}{overtime :<19.1f}${overtime_pay :<19.2f}${regular_pay :<19.2f}${gross_pay :<19.2f}")

#Printing the totals outside of the while loop
print(f"Total number of employees: {employee_count}")
print(f"Total overtime pay: ${total_overtime_pay:.2f}")
print(f"Total regular pay: ${total_regular_pay:.2f}")
print(f"Total gross pay: ${total_gross_pay:.2f}")
    


