#Homework 1
#Tejvir Sohi
#ECS 36A Winter 2019

import turtle

#Assigning variables
t = turtle.Pen()

#User enters the number of sides
sides = int(input("Enter the number of sides you want:"))

#Arbitrarily assigning a length
length = 50

#Every angle should be the same so we divide 360 by the number of sides
angle = 360 / sides

#Loop that loops the same number of times as the number of sides
for i in range(sides):
    #moves turtle forward, drawing a line
    t.forward(length)
    #turns turtle to the right an exact amount(refer to "angle")
    t.right(angle)
