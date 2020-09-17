#ECS 36A
#Assignment 5
#Tejvir Sohi
#


def read_words():
    openfile = open("Alice.txt", "r")
    templist = []
    letterslist = []
    for lines in openfile:
        for i in lines:
            ii = i.lower()
            letterslist.append(ii)
    for p in letterslist:
        if p not in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',"'","-",' '] and p.isdigit() == False:
            letterslist.remove(p)      
    words = list("".join(letterslist).split())
    return words

class _Node:
    def __init__(self, value, left=None, right=None):
        self._left = left
        self._right = right
        self._value = value
        self._count = 1


def __init__(self):
    self.root = None
        
def isEmpty(self):
    return self.root == None
    
def insert(self, words) :
    if self.isEmpty() :
        self.root = self._Node(words)
        return
    parent = None
    pointer = self.root
    while (pointer != None) :
        if words == pointer._words:
            pointer._count += 1
            return
        elif value < pointer._value:
            parent = pointer
            pointer = pointer._left
        else :
            parent = pointer
            pointer = pointer._right            
    if (value <= parent._value) :
        parent._left = self._Node(value)
    else :
        parent._right = self._Node(value)

def printTree(self):
    pointer = self.root
    if pointer._left is not None:
        pointer._left.printTree()
    print(str(pointer._value) + " " + str(pointer._count))
    if pointer._right is not None:
        pointer._right.printTree()
        
def createTree(self,words):
    if len(words) > 0:
        for word in words:
            BinaryTree().insert(word)
        return BinaryTree()
    else:
        return None
    
def search(self,tree, word):
    node = tree
    depth = 0
    count = 0
    while True:
        print(node.value)
        depth += 1
        if node.value == word:
            count = node.count
            break
        elif word < node.value:
            node = node.left
        elif word > node.value:
            node = node.right
    return depth, count

def main():
    words = read_words()
    insert(words)
    createTree(words)
    printTree()
main()
