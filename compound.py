#Homework 4
#ECS 36A
#Tejvir Sohi

def number(n): # checks if string contains numbers
    return n in '1234567890'

def upper(n): # checks for uppercase strings
    return n == n.upper() and n != n.lower()
        
def lower(n): # checks for lowercase strings
    return n == n.lower() and n != n.upper()
 
def main():
    inf = open("atomic_weights.txt")
    m = {}
    for line in inf: #Makes dictionary of elements and weights
        line = line.strip()
        lineitems = line.split('\t')
        weight = lineitems[1]
        for element in lineitems[0]:
            element = float(lineitems[0])
            m[weight] = element
    try:
        chemical = input("Enter the chemical formula:")
    except EOFError:
        quit()
    mass = 0
    formula = chemical + "?"
    #Calculating atomic weight
    for i in range(len(formula)):
            if upper(formula[i]): # start of chemical symbol
                if formula[i+1] == "?":
                    mass += m[formula[i]]
                
                elif upper(formula[i+1]): # 1 atom, 1 letter symbol
                    mass += m[formula[i]]
                
                elif number(formula[i+1]): # multiple atoms, 1 letter symbol
                    if formula[i+2] == "?":
                        mass += (int(formula[i+1])) * (m[formula[i]])
                    if upper(formula[i+2]):
                        mass += (int(formula[i+1])) * (m[formula[i]])
                    elif number(formula[i+2]):
                        mass += (int(formula[i+1] + formula[i+2])) * (m[formula[i]])
                elif lower(formula[i+1]):
                    if formula[i+2] == "?":
                        mass += m[formula[i] + formula[i+1]]
                    if upper(formula[i+2]): # 1 atom, 2 letter symbol
                        mass += m[formula[i] + formula[i+1]]
                    elif number(formula[i+2]): # multiple atoms, 2 letter symbol
                        if formula[i+3] == "?":
                            mass += (int(formula[i+2]) *
                                     m[formula[i] + formula[i+1]])
                        if upper(formula[i+3]):
                            mass += (int(formula[i+2]) *
                                     m[formula[i] + formula[i+1]])
                        elif number(formula[i+3]):
                            mass += (int(formula[i+2] + formula[i+3]) *
                                     m[formula[i] + formula[i+1]])
    print("Molecular mass of",chemical, "=", mass)
    return main()

main()
