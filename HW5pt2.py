# Assignment 5
#Tejvir Sohi
#ECS 32A Fall 2018

# function that reads population file and builds dictionary
def makePopDictionary():
    inf = open("world_population_2017.tsv","r")
    mydict = {}
    for line in inf:
        line = line.strip()
        lineitems = line.split('\t')
        country = lineitems[1]
        for pop in lineitems[2:]:
            pop = int(pop.replace(',','')) #Removes commas and converts to int           
            mydict[pop] = country #Makes dictionary from pop and country
    return

# function that reads drinking water file and prints out
# countries that have changed percentage of people with
# access, if population is big enough.
def readDWdata():
    infwater = open("drinkingWater.csv","r")
    count = 0 #Count is used to skip the first few lines
    for line in infwater:
        count = count + 1
        line = line.strip()
        lineitem = line.split(',')
        if count>3:
            if lineitem[1] != "" and lineitem[21] != "": #Used to skip the empty values
                country = lineitem[0]
                year1990 = int(lineitem[1])
                year2010 = int(lineitem[21])
                change = (year2010 - year1990) #Used to find the difference in values
                print(country,year1990,year2010,change)
    return

def main():
    makePopDictionary()
    readDWdata()
    return
     
main()
