from inputCheck import canBeInt
def main():
    k = input("Please enter a number between 0 and 60.")
    if not canBeInt(k):
        print("Sorry, that is not a number between 0 and 60.")
        return
    k = int(k)
    if k > 60:
        print("Sorry, that is not a number between 0 and 60.")
        return
    inFile = open("temp.txt","r")
    line = "x"
    tempList = []
    i = k
    while line != "":
        
        line = inFile.readline()
        line = line.strip()
        words = line.split()
        
        toBeFloat = (words[-1]) #This is the last element, which will get floated
        
        tempData = float(toBeFloat) #tempData is now a float
        tempList.append(tempData)
        #tempList gets appended with tempData each iteration
        
        
        
        if "2010" in line:
            break
    tempList2 = tempList #Everything below this point is unfinished junk
    index = k
    while tempList[i]!=tempList:
        print(tempList[i])
        i = i+1
           
                                       
    print(tempList[k])
    
            
        
main()
