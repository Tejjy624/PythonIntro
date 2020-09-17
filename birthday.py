##chelsea aguilar
##ECS 36A
##hw 4


##questions
##1. for the birthday to be over 0.9 it takes about 41 people,
##and for the probablity of people having the same birthday for 0.5 is 23 people   

import random

def hasduplicates(inlist):
    unique= set(inlist)
    return len(set(inlist))!= len(inlist)
   
def onetest(count):
    l=[]
    for i in range(0, count):
        l.append(random.randint(1,365))
    return hasduplicates(l)

##print(onetest(40))

def probab(count,num):
    counter=0
    for i in range(0,num):
        if onetest(count)==True:
            counter=counter+1
        dups=counter/num
    return dups

##print(onetest(2))

def main(count,num):
    while probab(count,num)<=0.9:
        count=count+1
        print("for",count,"the probability of  2 birthdays is",probab(count,num))
main(1,5000)    
