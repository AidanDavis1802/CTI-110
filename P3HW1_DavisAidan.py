# Aidan Davis
#10/17/2026
#P3HW1
#Debugging code


# This program takes 6 number grades , determines average and displays letter grade for average.
#As well as displaying the max, min, and sum of the grades


# Enter grades for six modules
#making each input a float so python knows its a number and not astring of text

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

#Separating line
print("------------Results------------")

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# determine lowest, highest , sum and average for grades
#using min to determine the lowest number in the grade list
#max to determine the biggest number in the list
#grade sum variable is applied to the entire list added together
#avg variable applied to grade sum divided by the length of the list
low = min(grades)
high = max(grades)
grade_sum = grades [0] + grades [1] + grades [2] + grades [3] + grades [4] + grades [5]
avg = grade_sum / len(grades)

#Displaying the above variables
print(f"{'Lowest Grade:' :<20}{low:.1f}")
print(f"{'Highest Grade:' :<20}{high:.1f}")
print(f"{'Sum of Grades' :<20}{grade_sum:.1f}")
print(f"{'Average:' :<20}{avg:.2f}")

#Printing a separating line
print("----------------------------------")

# determine letter grade for average
#using if, elif, and else to determine what letter grade the average grade is equal to
#if grade is greater than or equal to 90 they get an a
#or else if grade is greater or equal to 80 they get a b
#repeating down to F where then if evertyhing else if untrue it prints an F


if avg >= 90:
 print('Your grade is: A')
elif avg >= 80:
 print('Your grade is: B')
elif avg >= 70:
 print("Your grade is: C")
elif avg >= 60:
 print("Your grade is: D")
else:
 print('Your grade is: F')






