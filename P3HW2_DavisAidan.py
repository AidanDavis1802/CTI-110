# Aidan Davis
# 10/17/2026
# P3HW2
# Program calculating pay and overtime pay for an employee 

#Gathering information from the employee
#Asking for their name with the input function and storing it in a variable
name = input("Enter Employee's Name: ")
#Saving the hours worked and pay rate in separate variables as a float
hours = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter Employee's Pay Rate: "))

#Separating line
print("----------------------------------")

#Determining if an employee worked overtime
#if their hours are more than 40 then the overtime they worked = their hours - 40
#if they worked 40 or less then they did not work overtime
if hours > 40:
    overtime = hours - 40
else:
    overtime = 0

#Figuring out the amount of overtime money the employee needs paid
#If their overtime is greater than 0 hours (as determined above)
#Then the overtime money = the extra hours worked multiplied by the result of 1.5 times  their hourly pay
if overtime > 0:
    overtime_money = overtime * (1.5 * pay_rate)
else:
    overtime_money = 0

#Calculating the base payment not including overtime
#So if overtime is greater than 0, we subtract it from our hours before multiplying by their pay rate
#And if their overtime is 0 then we just do hours * pay rate to figure out how much they need paid without overtime (because there is no overtime to be paid)
if overtime > 0:
    pay = (hours - overtime) * pay_rate
else:
    pay = hours * pay_rate

#Combining overtime money and their base pay to calculate total gross pay
total_gross = pay + overtime_money

#Printing the employee name using f string formatting
print(f"{'Employee name:' :<20}{name}")
print()

#Printing all the necessary information names using f string formatting
print(f"{'Hours Worked' :<20}{'Pay Rate' :<19}{'OverTime' :<19}{'OverTime Pay' :<20}{'RegHour Pay' :<20}{'Gross Pay'}")

#Separating line
print("--" * 52)
#Finally, printing the actual information to go with the above strings
print(f"{hours :<20.1f}{pay_rate :<19.1f}{overtime :<19.1f}{overtime_money :<20.2f}{pay :<20.2f}{total_gross :.2f}")


