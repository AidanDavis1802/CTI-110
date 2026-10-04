#Aidan Davis
#10/04/2026
#P2HW2
#A simple program that calculates grades

#Collecting module grade information from the user
module_1 = float(input("Enter grade for Module 1: " ))
module_2 = float(input("Enter grade for Module 2: " ))
module_3 = float(input("Enter grade for Module 3: " ))
module_4 = float(input("Enter grade for Module 4: " ))
module_5 = float(input("Enter grade for Module 5: " ))
module_6 = float(input("Enter grade for Module 6: " ))

#Creating the list of module grades
module_grades = [module_1, module_2, module_3, module_4, module_5, module_6]

#Seperating line
print()
print("------------Results------------")

#Calculating and displaying the lowest grade
grade_minimum = min(module_grades)
print(f"{'Lowest Grade:' :<20}{grade_minimum}")

#Calculating and displaying the highest grade
grade_maximum = max(module_grades)
print(f"{'Highest Grade:' :<20}{grade_maximum}")

#Calculating and displaying the sum of grades
grade_sum = module_grades[0] + module_grades[1] + module_grades[2] + module_grades[3] + module_grades[4] + module_grades[5]
print(f"{'Sum of Grades:' :<20}{grade_sum}")

#Calculating and displaying the average of the grades
grade_average = grade_sum / len(module_grades)
print(f"{'Average:' :<20}{grade_average:.2f}")

#Clean dash line at the bottom
print("-" * 32)


