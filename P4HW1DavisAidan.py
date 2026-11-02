#Aidan Davis
#11/1/2026
#P4HW1
#Using loops to collect and validate scores as well as calculating grades

#Asking the user how many scores they want to enter and making it an integer
num_scores = int(input("How many scores do you want to enter? "))

#Setting up our while loop
score_amount = 1
#Setup for our list
grade_list = []
#Running the loop the amount of times the user input at the beginning
while score_amount<= num_scores:
    grade_score = float(input(f"Enter Score #{score_amount}: "))
#Fallback loop incase user enters an invalid number
    while grade_score > 100 or grade_score < 0:
        print("Invalid score")
        print("Score should be between 0 and 100:")
        grade_score = float(input(f"Enter Score #{score_amount} again: "))
#Adding each inputted number into out grade list    
    grade_list += [grade_score]
#Adds +1 to the score amount so the loop knows when to stop
    score_amount += 1

#Printing a line to separate the input from the results
print("------------Results------------")
#Now the program will print the lowest score, the list without the lowest grade in it, the average of all the scores, and the letter grade
#Printing the lowest grade in the list
smallest = min(grade_list)
print(f"Lowest Score:{smallest}")

#Printing the modified list without the lowest score
grade_list.remove(smallest)
print(f"Modified List: {grade_list}")

#Finding the average of the modified list and printing it
average = sum(grade_list) / len(grade_list)
print(f"Scores Average:{average}")

#Figuring out which letter grade the average is with an if elif else statement

if average >= 90:
    grade = "A"
elif average >= 80:
    grade ="B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"
#Printing the determined letter grade
print(f"Grade:{grade}")

#Printing a final dash line to clean everything up
print("-------------------------------")

















#======================================
#AI USAGE REPORT
#======================================
#
#Item 1: I could not figure out how to remove the smallest number from a list when i didn't know what was going to be in the list
#I Checked the notebook and could not for the life of me figure it out, so i asked chatgpt the proper syntax to remove an item from an unknown list
#Date 11/1/2026
#Service: ChatGPT-5.6 sol
#Prompt: how do i remove the smallest float from a list titled grade_list when i already assigned a variable to the smallest float in that list called "smallest"
#Response: It told me to use grade_list.remove(smallest) and then provided an example
# Used in submission: On line 34
# #====================================