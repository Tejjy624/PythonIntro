#Homework 3
#ECS 36A
#Tejvir Sohi
from sys import exit
while True:
    try:
        a=int(input("Enter the integer coefficent of x^2:"))
    except:
        print("Enter the integer coefficient of x^2:")
    else:
        exit
        break
    
while True:
    try:
        b=int(input("Enter the integer coefficient of x:"))
    except:
        print("Enter the integer coefficient of x:")
    else:
        exit
        break
while True:
    try:
        c=int(input("Enter the integer costant term:"))
    except:
        print("Enter the integer costant term:")
    else:
        exit
        break

def newton(a,b,c):
    x = 1
    better = 0
    threshold = .0000000001
    while True:
        approximation = (x) - (((x**3) + (a*(x**2)) + (b*x)+c)/((3*(x**2)) + (2*a*x)+ b))
        x = approximation
        print(approximation)
        better = ((approximation - x/approximation)*.5)
        print(better)
        if abs(better - approximation) < threshold:
            print("The approximate solution of x^3+",a,"x^2+",b,"x+",c," is:",better)
            print("The error is", better - approximation)
            break
newton(a,b,c)
