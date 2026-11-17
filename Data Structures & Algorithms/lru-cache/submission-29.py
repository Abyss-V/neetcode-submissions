class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.c = capacity
        self.i = 0
    def get(self, key: int) -> int:
        if key not in self.cache:
            return  -1
        self.cache.move_to_end(key)
        return self.cache[key]
      

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            self.cache[key] = value
            self.i += 1
        if len(self.cache) > self.c:
            self.cache.popitem(last=False)