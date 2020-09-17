#Homework 3
#ECS 36A
#Tejvir Sohi

def newton(a,b,c):
    x = 1
    better = 1
    threshold = 10^-10
    while True:
        x = better
        approximation = (x - (((x**3) + (a*(x**2) + ((b*x)+c))))/((3*(x**2)) + ((2*(a*x)+ b))))
        better = (approximation + x/approximation)/2
        if abs(approximation - better) < threshold:
            print("The approximate solution is:",better)
            break
newton(6,11,6)
