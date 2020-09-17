#  Julio Beas
# ECS 36A, Winter 2019
# Assignment 4 Part 2
#
# Helped by James CS tutor club
# birthday problem

import random

def hasduplicates(L):
    foundDup = False
    for num in L:
        if L.count(num) > 1:
            foundDup = True
    return foundDup

def onetest(count):
    L = []
    for i in range(count):
        L.append(random.randint(1,356))
    
    return hasduplicates(L)

def probab(count, num):
    duplicates = 0
    for i in range(num):
        if onetest(count) == True:
            duplicates = duplicates + 1
        else:
            duplicates = duplicates + 0
    probability = duplicates/num
            
    return "{:.5f}".format(probability)



count = 2
num = 5000
p = 0
while p < 0.9:
    p = float(probab(count, num))
    print("For", count,"people, the probablility of 2 birthddays is", p)
    count += 1


