# Aidan Davis
# 11/1/2026
#P4LAB1
#Using turtle graphics and loops to draw a house

#Import the turtle library
import turtle

#Creating turtle window and drawing object
win = turtle.Screen()
pen = turtle.Turtle()

#Setting turtle options
pen.pensize(5)
pen.pencolor("blue")
pen.shape("arrow")
win.bgcolor("teal")

#While loop creating the square
sides_remaining = 4
while sides_remaining != 0:
    pen.forward(100)
    pen.left(90)
    sides_remaining -= 1

#Moving the turtle to the top of the square
pen.left(90)
pen.forward(100)

pen.right(90)

#Creating a for loop to draw the triangle on the roof
for side in range(3):
    pen.forward(100)
    pen.left(120)



#Waits for user to close window
win.mainloop()
 