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
    value = list("".join(letterslist).split())
    return value

class Node:
    def __init__(self, word = None):
        self.word = word
        self.count = 0
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, word) :
        if self.root == None :
            self.root = Node(word)
        else:
            self._insert(word,self.root)
            return

    def _insert(self,word,cur_node):
        if len(word) < cur_node.word:
            if cur_node.left == None:
                cur_node.left = Node(word)
            else:
                self._insert(word,cur_node.left)
        elif word > cur_node.word:
            if cur_node.right == None:
                cur_node.right = Node(word)
            else:
                self._insert(word,cur_node.right)
        else:
            print("Value already in tree!")

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self,cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left)
            print (str(cur_node.word))
            self._print_tree(cur_node.right)
            
    def find(self,word):
        if self.root != None:
            return self._find(word,self.root)
        else:
            return None
        
    def _find(self,word,cur_node):
        if word == cur_node.word:
            return cur_node
        elif word < cur_node.word and cur_node.left != None:
            return self._find(word,cur_node.left)
        elif word > cur_node.word and cur_node.right != None:
            return self._find(word,cur_node.right)

    def delete_value(self,word):
        return self.delete_node(self.find(word))

    def search(self,word):
        if self.root != None:
            return self._search(word,self.root)
        else:
            return False

    def _search(self,word,cur_node):
        if word == cur_node.word:
            return True
        elif word < cur_node.word and cur_node.left != None:
            return self._search(word,cur_node.left)
        elif word > cur_node.word and cur_node.right != None:
            return self._search(word,cur_node.right)
        return False 
def main():
    tree = BST()
    word = read_words()
    tree.insert(word)
    tree.print_tree()
    print (tree.search(10))
    print (tree.search(30))
main()
