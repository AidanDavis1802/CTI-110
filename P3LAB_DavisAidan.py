# Aidan Davis
# 10/16/2026
# P3LAB
# A simple program that does calculations on money


# Asking a user to enter an ammount of money as a float
change = float(input("Enter an amount of money: $"))

print (f"Change amount:{change}")

#Changing the float to an integer
# Changing the variable name instead of using just change again as it works better in my head
change_as_int = round(change*100)
print (f"Change amount:{change_as_int}")

#Determining how many coins are needed
num_dollars = change_as_int // 100
remaining_after_dollars = change_as_int - (num_dollars*100)

num_quarters = remaining_after_dollars // 25
remaining_after_quarters = remaining_after_dollars - (num_quarters*25)


num_dimes = remaining_after_quarters // 10
remaining_after_dimes = remaining_after_quarters - (num_dimes*10)

num_nickels = remaining_after_dimes // 5
remaining_after_nickels = remaining_after_dimes - (num_nickels*5)

num_pennies = remaining_after_nickels 

#Display the fewest dollars and coins needed for the entered amount
#If the number of dollars is bigger than 0 AND equals 1 print the ammount of dollars followed by the word "Dollar"
#If the above condition is not met print the number of dollars followed by the word "Dollars"
#The same logic is applied to quarters, dimes, nickels, and pennies
if num_dollars > 0:
    if num_dollars == 1:
        print (f"{num_dollars} Dollar")
    else:
        print (f"{num_dollars} Dollars")


if num_quarters > 0:
    if num_quarters == 1:
        print (f"{num_quarters} Quarter")
    else:
        print (f"{num_quarters} Quarters") 


if num_dimes > 0:
    if num_dimes == 1:
        print (f"{num_dimes} Dime")
    else:
        print (f"{num_dimes} Dimes")


if num_nickels > 0:
    if num_nickels == 1:
        print (f"{num_nickels} Nickel")
    else:
        print (f"{num_nickels} Nickels")


if num_pennies > 0:
    if num_pennies == 1:
        print (f"{num_pennies} Penny")
    else:
        print (f"{num_pennies} Pennies")