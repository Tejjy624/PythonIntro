#Assignmnet 4 Week 1
#Tejvir Sohi
#ECS 32A Fall 2018
#

#filehandle; file opened for reading
inf = open("Sacramento-1880-2018.NOAA.csv","r")
outf = open("tempAnomaly.txt", "w")
count = 0
outf.write("Year\tValue\n")
for line in inf:
    count = count + 1 # counts lines
    line = line.strip() #Strips extra space around lines
    if count>5: # used to skip the first 5 lines
        line = line.split(",")
        year = line[0]
        value = float(line[1])
        value = "{:.4f}".format(value)
        value = str(value)
        outf.write(year)
        outf.write("\t")
        outf.write(value)
        outf.write("\n")
inf.close()
outf.close()
