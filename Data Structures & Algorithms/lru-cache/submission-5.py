class Node:
    def __init__(self, key, value, nex = None, prev = None):
        self.key = key
        self.value = value  
        self.next = nex
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.head = None 
        self.tail = None
        self.capacity = capacity 
        self.size = 0
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            tmp = self.cache[key] 
            self.removeNode(tmp)
            self.addNode(tmp)
            return tmp.value 
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        newNode = Node(key, value)

        if key in self.cache: 
            self.removeNode(self.cache[key])
        elif self.size >= self.capacity:
            self.removeNode(self.head)

        self.addNode(newNode)
    
    def removeNode(self, node):
        if not self.cache[node.key]:
            return 
        
        if self.size == 1:
            self.head = self.tail = None 
            self.cache = {}
            self.size = 0
            return
        
        if self.head == node:
            self.head.next.prev = None 
            self.head = self.head.next 
        elif self.tail == node:
            self.tail.prev.next = None 
            self.tail = self.tail.prev
        else:
            curNode = self.cache[node.key] 
            curNode.prev.next = curNode.next 
            curNode.next.prev = curNode.prev 

        self.cache.pop(node.key, None)
        self.size -= 1
        
    def addNode(self, node):
        if self.size == 0:
            self.head = self.tail = node 
            self.head.next = self.tail 
            self.tail.prev = self.head 
            self.tail.next = self.head.prev = None  
        else:
            self.tail.next = node 
            node.prev = self.tail
            self.tail = node
        
        self.size += 1 
        self.cache[node.key] = node
            

        
        


