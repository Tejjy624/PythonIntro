def main():
    #opent the file
    bookFileName = "RomeoAndJuliet.txt"
    #call function to read all lines and make a list of words
    words = readallwords(bookFileName)
    #call another function to find the unique words
    uniquelist = uniqueWords(words)
    #print out the count of words,
    print("The total word count", len(words))
    #print out the count of unique words
    print("Number of unique words", len(uniquelist))

def readallwords(bookFileName):
    infile = open(bookFileName):
    words = []
    for line in infile:
        for word in line..split():
            words = words.append()
    return(words)

def uniqueWords(wordlist):
    uniques = []
    for word in wordlist:
        if (word in uniques):
            continue
        else:
            uniques.append(word)
    return uniques

main()
