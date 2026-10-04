# Aidan Davis
#10/03/2026
#P2LAB2
# Creating and using a dictionary

cars = {"Camaro" :18.21, "Prius":52.36, "Model S" :110, "Silverado":26}

#get keys from dict
keys = cars.keys()
print(keys)

#Getting car from user
car = input("Enter a vehicle to see its mpg: ")

#Get MPG for the given car
mpg = cars [car]

#Display the mpg for the given car
print(f"The {car} gets {mpg} mpg.")

#Getting number of miles the user will drive the car
miles = float(input(f"How many miles will you drive the {car}? "))

#Calculating gas needed
gallons_needed = miles/mpg

#Display results
print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {car} {miles:.1f} miles ")

