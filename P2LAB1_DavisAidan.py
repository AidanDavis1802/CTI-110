# Aidan Davis
# 10/03/2026
#P2Lab1
# Using a the radius of a circle to make calculations

# Importing math module to use the constnt, math.pi
import math

#Asking the user for the radius of a circle
radius = float(input("What is the radius of the circle? "))
print()

#Calculating diameter
diameter = 2 * radius

#Displaying diamter with one decimal point
print(f"The diamter of the circle is {diameter:.1f}")

print()


#Calculating circumference
circumfrence= 2 * math.pi * radius

#Displaying circumference with two decimal points
print(f'The circumfrence of the circle is {circumfrence:.2f}\n')

#Calculating area
area = math.pi * radius **2

#Displaying area with three decimal points
print(f'The area of the circle is {area:.3f}')





