#Homework 2
#Tejvir Sohi
#ECS 36A Winter 2019
from random import randint
import random
import turtle


while True:
    try:
        numgames = int(input("How many games did you want to play?"))
    except:
        print("That aint it chief. Ya gotta enter a positive integer :D")
    else:
        break
print("Out of",numgames,"games:")
def main():
    # Contestant switches doors
    # Counting wins
    win1 = 0
    for i in range(numgames):
        # Randomly selects winning door
        windoor = randint(1,3)
    
        # Randomly selects door chosen by contestant
        doorchose = randint(1,3)

        # Creat list with 3 doors. Remove winning door
        opendoor = [1,2,3]
        opendoor.remove(windoor)
        if doorchose != windoor : opendoor.remove(doorchose)

        # Door opened by monty
        montyopens = random.choice(opendoor)

        # player changes his first choice
        opendoor = [1,2,3]
        opendoor.remove(montyopens)
        opendoor.remove(doorchose)
        doorchose = opendoor[0]

        # Did you win?
        if windoor == doorchose:
            win1 = win1 + 1
    print("Always switching wins:",(win1/numgames),"(", win1, "games)")
        # Contestant doesnt switch doors
        # Counting wins
    win2 = 0
    for i in range(numgames):
        # Randomly selects winning door
        windoor2 = randint(1,3)
    
        # Randomly selects door chosen by contestant
        doorchose2 = randint(1,3)
        
        # Creat list with 3 doors. Remove winning door
        opendoor2 = [1,2,3]
        opendoor2.remove(windoor2)
        if doorchose2 != windoor2 : opendoor2.remove(doorchose2)
    
        # Door opened by monty
        montyopens2 = random.choice(opendoor2)

        # Did you win?
        if windoor2 == doorchose2:
            win2 = win2 + 1
    print("Never switching wins:",(win2/numgames),"(",win2, "games)")
    hist = turtle.Turtle()
    values = [(win1/numgames),(win2/numgames)]
    colors = ['black']
    hist.up()
    hist.goto(-60,-60)
    hist.write("Percentage of games won if you switch always or never", False, "center", ("Arial", 10, "normal"))
    hist.down()
    def dobar(h,c):
        hist.begin_fill()
        hist.color(c)
        hist.setheading(90)
        hist.forward(h)
        hist.right(90)
        hist.forward(40)
        hist.right(90)
        hist.forward(h)
        hist.end_fill()

    for value in values:
        dobar(value, colors[0])
    
main()
