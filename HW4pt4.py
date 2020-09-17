#Assignmnet 4 Week 1
#Tejvir Sohi
#ECS 32A Fall 2018

#filehandle; file opened for reading
from inputCheck import canBeInt

#Opens the temperature anomaly files
inf = open("Sacramento-1880-2018.NOAA.csv","r")
outf = open("tempAnomaly.txt", "w")

# Loops until the user enters an integer between 0 and 60 inclusive
done = False
while not done:
    k = input("Enter an integer between 0 and 60:")
    if canBeInt(k):
        k = int(k)
        if (k) <= 60 and (k) >= 0:
            done = True
 
#Ignores the first 5 lines
for i in range(5):
    inf.readline()

#Prints the Header
outf.write("Year\tValue\n")

#Introduces the 2 lists we use for year and value
tempList = []
yearList = []

# read in the input file of anomalies
# into lists yearList and tempList
for line in inf:
    line = line.strip()
    (year, anomaly) = line.split(',')
    yearList.append(year)
    anomaly = float(anomaly)
    tempList.append(anomaly)

# loop through both yearList and tempList
for i in range(k,len(yearList)-k):
    #Introduces and defines the variables used to calculate the moving average
    move_sum = 0
    move_avg = 0
    #loop used to calculate the sum of all the values
    for j in range (i - k, i + k + 1):
        move_sum = move_sum + tempList[j]
    #calculates the moving average
    move_avg = (move_sum)/(2*k + 1)
    # construct a line of output
    line = yearList[i] + "\t" + ("{:.4f}".format(move_avg))
    #print(line)
    line = line + "\n"
    outf.write(line)
#Closes all the files that were opened
inf.close()
outf.close()
