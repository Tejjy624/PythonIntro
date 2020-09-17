inf = open("atomic_weights.txt")
m = {}
for line in inf:
    line = line.strip()
    lineitems = line.split('\t')
    weight = lineitems[1]
    for element in lineitems[0]:
        element = float(lineitems[0])
        m[weight] = element
print(m)
def number(n): # tests if a string character is a number
    return n in '1234567890'
        
def upper_case(n): # tests if a string character is upper case
    return n == n.upper() and n != n.lower()
        
def lower_case(n): # tests if a string character is lower case
    return n == n.lower() and n != n.upper()
 
def main():
    while True:
        raw = input('Enter molecular formula: ')
        formula = raw + "?"
        mass = 0
        for i in range(len(formula)):
            if upper_case(formula[i]): # start of chemical symbol
                if formula[i+1] == "?":
                    mass = m[formula[i]]
                elif upper_case(formula[i+1]): # 1 atom, 1 letter symbol
                    mass = m[formula[i]]
                elif number(formula[i+1]): # multiple atoms, 1 letter symbol
                    if formula[i+2] == "?":
                        mass = (int(formula[i+1])) * (m[formula[i]])
                    if upper_case(formula[i+2]):
                        mass = (int(formula[i+1])) * (m[formula[i]])
                    elif number(formula[i+2]):
                        mass = (int(formula[i+1] + formula[i+2])) * (m[formula[i]])
                elif lower_case(formula[i+1]):
                    if formula[i+2] == "?":
                        mass = m[formula[i] + formula[i+1]]
                    if upper_case(formula[i+2]): # 1 atom, 2 letter symbol
                        mass = m[formula[i] + formula[i+1]]
                    elif number(formula[i+2]): # multiple atoms, 2 letter symbol
                        if formula[i+3] == "?":
                            mass = (int(formula[i+2]) *
                                     m[formula[i] + formula[i+1]])
                        if upper_case(formula[i+3]):
                            mass = (int(formula[i+2]) *
                                     m[formula[i] + formula[i+1]])
                        elif number(formula[i+3]):
                            mass = (int(formula[i+2] + formula[i+3]) *
                                     m[formula[i] + formula[i+1]])
        print("Molecular mass of", raw, "=", mass)
 
main()
