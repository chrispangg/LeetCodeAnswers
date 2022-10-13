class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0,0) #holds LRU
        self.right = Node(0,0) #holds recently placed
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    def insert(self, node): # insert right side of right node
        #adjust nextRight
        nxtRight = self.right.prev
        nxtRight.next = node
        #adjust Right
        self.right.prev = node
        # insert node
        node.next = self.right
        node.prev = nxtRight
    
    def get(self, key: int) -> int:
        # use remove and insert to reorder LRU
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        # if key already in, remove first, then update
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            delete = self.left.next
            self.remove(delete)
            del self.cache[delete.key]
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)