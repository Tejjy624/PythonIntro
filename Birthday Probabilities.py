#Tejvir Sohi
#ECS 36A
#Homework 4

#Part 2D:Questions
#We need about 41 people to get a probability of over .9
#To get at least .5, we need 23 people   
import random

def hasduplicates(L):#Checks for duplicates
    unique= set(L)
    return len(set(L))!= len(L)
   
def onetest(count):#Used to generate list of random integers
    x=[]
    for i in range(0, count):
        x.append(random.randint(1,365))
    return hasduplicates(x)

def probab(count,num):#Calculates probability of 2 birthdays
    counter=0
    for i in range(0,num):
        if onetest(count)==True:
            counter=counter+1
        dups=counter/num
    return dups

def main(count,num):#Prints results until a probability of .9 is reached
    while probab(count,num)<=0.9:
        count=count+1
        print("For",count,"people, the probability of 2 birthdays is",probab(count,num))

main(1,5000)    
