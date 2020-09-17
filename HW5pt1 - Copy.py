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
        print(country, pop)
    return

# function that reads drinking water file and prints out
# countries that have changed percentage of people with
# access, if population is big enough.
def readDWdata(popDict):
    return

def main():
    makePopDictionary()
    return
     
main()
