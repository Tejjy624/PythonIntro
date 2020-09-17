#Assignmnet 4 Week 1
#Tejvir Sohi
#ECS 32A Fall 2018
#

#filehandle; file opened for reading
f = open("Sacramento-1880-2018.NOAA.csv","r")
count = 0

for line in f:
    count = count + 1 # counts lines
    line = line.strip() #Strips extra space around lines
    if count>5: # used to skip the first 5 lines
        print(line)

