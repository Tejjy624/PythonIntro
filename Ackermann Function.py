#Homework 3
#ECS 36A
#Tejvir Sohi
from sys import exit

#Main ackermann function
def ackermann(m,n):
    #First condition provided by the function
     if m == 0:
          return (n + 1)
    #Second condition provided by the function
     elif n == 0:
          return ackermann(m - 1, 1)
    #Third condition provided by the funtion
     else:
          return ackermann(m - 1, ackermann(m, n - 1))
        
#Loop to ask for an m ("x") value for the ackermann formula
while True:
    try:
        x=int(input("Please enter a nonnegative integer:"))
    except:
        print("That aint it chief. Ya gotta enter a nonnegative integer")
        exit()
    else:
        break
        
#Loop to ask for an n ("y") value for the ackermann formula
while True:
    try:
        y=int(input("Please enter a nonnegative integer: "))
    except:
        print("That aint it chief. Ya gotta enter a nonnegative interger")
        exit()
    else:
        break

print ("The Ackermann function returns a value of", ackermann(x, y))
print ("Please enter a nonnegative integer:")


