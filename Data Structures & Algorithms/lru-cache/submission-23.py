class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()  

    def get(self, key: int) -> int:
        
        if key in self.cache:
            self.cache.move_to_end(key)
        
        return self.cache[key] if key in self.cache else -1

    def put(self, key: int, value: int) -> None:

        if  key not in self.cache and len(self.cache.keys()) >= self.capacity:
            self.cache.popitem(last=False)
            self.cache[key] = value
        else:
            if key in self.cache:
                self.cache.move_to_end(key)
                self.cache[key] = value
            else:
                self.cache[key] = value

# time : O(1) both put and get ; space: o(n) overall
        
    