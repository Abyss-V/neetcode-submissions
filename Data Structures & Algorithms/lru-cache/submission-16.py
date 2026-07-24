class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.recent = None
        self.old = None
        self.cache = OrderedDict()  

    def get(self, key: int) -> int:
        
        if key in self.cache:
            v = self.cache[key]
            del self.cache[key]
            self.cache[key] = v
        
        return self.cache[key] if key in self.cache else -1

    def put(self, key: int, value: int) -> None:
        v = list(self.cache.keys())
        print(v)
        if  key not in self.cache and len(v) >= self.capacity:
            print(self.cache[v[0]])
            del self.cache[v[0]]
            self.cache[key] = value
        else:
            if key in self.cache:
                del self.cache[key]
            self.cache[key] = value

# use hashmap as history instead of deque
        
    