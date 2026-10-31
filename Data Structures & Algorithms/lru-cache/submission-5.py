class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key 
        self.val = val 
        self.next = next 
        self.prev = prev 

class LRUCache:

    def __init__(self, capacity: int):
        self.hm = {}
        self.head = None
        self.tail = None
        self.size = 0 
        self.capacity = capacity
    
    def add(self, key, value):
        node = Node(key, value)
        if self.size >= self.capacity:
            self.remove(self.tail.key)

        if not self.head:
            self.head = self.tail = node

        else:
            node.next = self.head 
            self.head.prev = node 
            self.head = node 

        self.hm[key] = node
        self.size += 1 
    
    def remove(self, key):
        node = self.hm[key] 
        value = node.val

        if not node.prev:
            self.head = node.next 
            
            if self.head:
                self.head.prev = None
            else:
                self.tail = None 

        elif not node.next:
            self.tail = node.prev 
            if self.tail:
                self.tail.next = None 
        else:
            node.prev.next = node.next 
            node.next.prev = node.prev 

        self.hm.pop(key)
        self.size -= 1

        return(key, value)


    def get(self, key: int) -> int:
        if key not in self.hm:
            return -1 
        key,value = self.remove(key)
        self.add(key, value)
        return value 

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            self.remove(key) 

        self.add(key, value)
