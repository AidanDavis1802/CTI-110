# Aidan Davis
# 10/31/2026
#P4LAB2
# Using loops to create a multiplication table

#Get an integer from the user
#Display the multiplication table up to 12 for the users integer
#If user gives negative integer, tell them negatives are not supported
#Ask the user if they would like to run the program again, if yes run again, if no, exit the program

#Setting up our while loop
answer =''
while answer != "no":
#Getting the integer from the user
   user_number = int(input("Enter a number here: "))
#If the integer is greater tha or equal to 0 the program runs and multiplies each number 1 through 12 by the users integer
   if user_number >= 0:
    for loop_num1 in range(1,12+1):
        print(f"{user_number} * {loop_num1} = {user_number * loop_num1}")
#If the user enters a negative number they are given this error
   else:
        print("This Program does not handle negative numbers")
#Updating the answer variable to determine if the while loop runs again or not
   answer = input("Would you like to run the program again? ")

print("Exiting program...")



