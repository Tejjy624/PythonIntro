#Assignmnet 4 Week 1
#Tejvir Sohi
#ECS 32A Fall 2018
#

#filehandle; file opened for reading
from inputCheck import canBeInt

# Loops until the user enters an integer between 0 and 60 inclusive
while True:
    num = input("Enter an integer between 0 and 60:")
    if canBeInt (num) == True:
        if int(num) <= 60 and int(num) >= 0:
            break
#Opens the temperature anomaly files
inf = open("Sacramento-1880-2018.NOAA.csv","r")
outf = open("tempAnomaly.txt", "w")

#Count is used to count extra lines
count = 0
outf.write("Year\tValue\n")

#Makes file into lists Year and Value
for line in inf:
    count = count + 1               #counts lines
    line = line.strip()             #Strips extra space around lines
    if count>5:                     #used to skip the first 5 lines
        #Manipulates the variables and informtion to allow easier printing
        line = line.split(",")      
        year = line[0]
        value = float(line[1])
        value = "{:.4f}".format(value)
        value = str(value)
        #Prints all the required information
        outf.write(year)
        outf.write("\t")
        outf.write(value)
        outf.write("\n")
inf.close()
outf.close()
