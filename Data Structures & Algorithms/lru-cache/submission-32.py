class Node:
    def __init__(self,val,key,nxt=None,prv=None):
        self.key = key
        self.val = val
        self.next = nxt
        self.prev = prv
class LRUCache:

    def __init__(self, capacity: int):
        self.c = capacity
        self.cache = {}
        self.left = self.right = Node(0,0)
        self.left.next , self.right.prev = self.right,self.left
    def remove(self,node):
        nxt,prev = node.next,node.prev
        nxt.prev,prev.next = prev,nxt
    def insert(self,node):
        last ,prv = self.right,self.right.prev
        prv.next = last.prev = node
        node.next = last
        node.prev = prv
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(value,key)
        self.insert(self.cache[key])
        if len(self.cache) > self.c:
            lru = self.left.next
            print(self.cache)
            del self.cache[lru.key]
            self.remove(lru)
           

# time : O(1) both put and get ; space: o(n) overall
        
    