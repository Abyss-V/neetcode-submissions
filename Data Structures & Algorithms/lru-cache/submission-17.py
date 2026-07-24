class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()  

    def get(self, key: int) -> int:
        
        if key in self.cache:
            v = self.cache[key]
            del self.cache[key]
            self.cache[key] = v
        
        return self.cache[key] if key in self.cache else -1

    def put(self, key: int, value: int) -> None:
        v = iter(self.cache.keys())

        if  key not in self.cache and len(self.cache.keys()) >= self.capacity:
            del self.cache[next(v)]
            self.cache[key] = value
        else:
            if key in self.cache:
                del self.cache[key]
            self.cache[key] = value

# time : O(1) both put and get ; space: o(n) both uses self.cache
        
    