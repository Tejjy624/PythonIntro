# ECS 32A
# Assignment 4 Week 1
# Tejvir Sohi
# Temperature Anomaly
from inputCheck import canBeInt


# Loop until the user enters an integer between
# 0 and 60 inclusive.
done = False
while not done:
    k = input("Enter an integer between 0 and 60:")
    if canBeInt(k):
        k = int(k)
        if k >= 0 and k <= 60:
            done = True

# opens the temerature anomaly file
inFile = open('Sacramento-1880-2018.NOAA.csv')

# ignore the first five lines of the file
for i in range(5):
    inFile.readline()

# floating point; list of anomalies 
tempList = []
# string; list of years
yearList = []

# read in the input file of anomalies
# into lists yearList and tempList
for line in inFile:
    line = line.strip()
    (year, anomaly) = line.split(',')
    yearList.append(year)
    anomaly = float(anomaly)
    tempList.append(anomaly)

# open the output file
outFile = open("tempAnomaly.txt", "w")

#write out header
#print("Year\tValue")
outFile.write("Year\tValue\n")

# loop through both yearList and tempList
for i in range(len(yearList)):
    # construct a line of output
    line = yearList[i] + "\t" + "{:.4f}".format(tempList[i])
    #print(line)
    line = line + "\n"
    outFile.write(line)
