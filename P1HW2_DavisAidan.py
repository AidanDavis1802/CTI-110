# Aidan Davis
# 09/17/2026
# P1HW2.py
# A basic program that calculates budgets


# Gathering the information needed
print("This program calculates and displays travel expenses")
print()
budget = int (input("enter your budget: "))
destination = (input("enter your travel destination: "))
gas = int(input("How much will you spend on gas?: "))
hotel= int(input("How much will you spend on hotels?: "))
food = int (input("Last, how much do you need for food?: "))

#Displaying information
print("----------Travel Expenses----------")
print ()
print("Location:", destination)
print ("Initial Budget:", budget)
print ()
print ("Gas:", gas)
print ("Hotel:", hotel)
print ("Food:", food)
#Now adding up the actual expenses
expenses = gas + hotel + food
#Now calculating the remaning money
result = budget - expenses
print("Remaning Balance:", result)



