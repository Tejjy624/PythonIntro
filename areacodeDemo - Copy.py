# main function first building the dictionary
# and then calls a function to lookup the dictionary

def main():
    areaCodeToState = readAllAreaCodes()
#    print(areaCodeToState)
    lookupAreaCodes(areaCodeToState)


def readAllAreaCodes():
    mydict = {}
    infile = open("areacodes.txt")
    for linerecord in infile:
        linerecord = linerecord.strip()
        lineitems = linerecord.split(',')
        state = lineitems[0]
        for num in lineitems[1:]:
            mydict[num.lstrip()] = state
            print("Added area code", num, "for state", state)
    return mydict

def lookupAreaCodes(areaCodeToState):
    while True:
        areacode = input("Please enter valid area code :")
        if (areacode == 'done'):
            break
        if (areacode in areaCodeToState):
            print ("The State for that area code is", areaCodeToState[areacode])
        else:
            print("Not a known area code")

main()

        
        
