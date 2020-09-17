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
    value = list("".join(letterslist).split())
    return value

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.count = 1

#    def __str__(self):
#        return 'value: {0}, count: {1}'.format(self.value, self.count)

class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        if self.root != None:
            return Node(value)
        elif root.value == value:
            root.count += 1
        elif value < root.value:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
        return root

    def create(seq):
        root = None
        for word in seq:
            root = insert(root, word)
        return root

    def search(root, word, depth=1):
        if not root:
            return 0, 0
        elif root.value == word:
            return depth, root.count
        elif word < root.value:
            return search(root.left, word, depth + 1)
        else:
            return search(root.right, word, depth + 1)

    def print_tree(root):
        if root:
            print_tree(root.left)
            print (root)
            print_tree(root.right)

def main():
    b = BinaryTree()
    read_words()
    b.insert(value)
    b.create(words)
    b.print_tree()

main()
#for word in src:
#    print 'search {0}, result: {1}'.format(word, search(tree, word))

# Output
# value: bar, count: 2
# value: barfoo, count: 1
# value: foo, count: 1
# value: foobar, count: 1
# search foo, result: (1, 1)
# search bar, result: (2, 2)
# search foobar, result: (2, 1)
# search bar, result: (2, 2)
# search barfoo, result: (3, 1)
