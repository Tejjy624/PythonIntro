#Homework 2
#Tejvir Sohi
#ECS 36A Winter 2019
from random import randint
import random

def montyalways(): # Contestant switches doors
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
    final = windoor == doorchose
    
def montynever(): # Contestant doesnt switch doors
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

    # Did you win?
    final = windoor == doorchose

montyalways()
montynever()
