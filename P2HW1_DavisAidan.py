# Aidan Davis
# 10/04/2026
# P2HW1
# A basic program that calculates budgets


# Gathering the information needed
print("This program calculates and displays travel expenses")
print()
budget = float (input("Enter Budgget: "))
print()
destination = (input("Enter your travel destination: "))
print()
gas = float(input("How much do you think you will spend on gas?: "))
print()
hotel= float(input("Approximately, how much will you need for accomodation/hotel?: "))
print()
food = float (input("Last, how much do you need for food?: "))
print()

#Displaying information
print("------------Travel Expenses------------")
print(f"{'Location:':<20}{destination}")
print (f"{'Initial Budget:':<20}${budget:.2f}")
print (f"{'Fuel:':<20}${gas:.2f}")
print (f"{'Accomodation:':<20}${hotel:.2f}")
print (f"{'Food:':<20}${food:.2f}")
dash = "-"
print (dash * 39)
print()
#Now adding up the actual expenses
expenses = gas + hotel + food
#Now calculating the remaning money
result = budget - expenses
print(f"{'Remaining Balance:':<20}${result:.2f}")


