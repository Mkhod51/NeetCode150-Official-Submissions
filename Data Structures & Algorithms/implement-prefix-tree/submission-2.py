class Node:
        def __init__(self, char):
            self.char = char 
            self.children = {} #char, Node
            self.endOfSomeWord = False

class PrefixTree:

    def __init__(self):
        self.trieNodes = {} #char, Node
        self.size = 0


    def insert(self, word: str) -> None:
        cur = self.trieNodes
        i = 0
        while i < len(word):
            if word[i] not in cur:
                cur[word[i]]  = Node(word[i])
            nextNode = cur[word[i]]
            cur = nextNode.children

            i += 1 

        nextNode.endOfSomeWord = True    
            
        
    def search(self, word: str) -> bool:
        cur = self.trieNodes 
        i = 0
        while i < len(word):
            if (not cur) or (word[i] not in cur):
                return False 
            nextNode = cur[word[i]]
            cur = nextNode.children
            i += 1 
        
        #If word acc finished
        if nextNode.endOfSomeWord: 
            return True

        return False 

    def startsWith(self, prefix: str) -> bool:
        cur = self.trieNodes 
        i = 0 

        while i < len(prefix):
            if (not cur) or (prefix[i] not in cur):
                return False 
            nextNode = cur[prefix[i]]
            cur = nextNode.children

            i += 1
        
        return True
        
        