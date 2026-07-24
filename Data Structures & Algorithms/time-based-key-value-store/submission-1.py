class TimeMap:

    def __init__(self):
        self.dic = defaultdict(str)
        self.m = 0
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m = max(self.m,timestamp)
        self.dic[(key,timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        i = 1
        ret = 0
        while i <= self.m:
            if (key,i) in self.dic and i <= timestamp:
                ret = max(i,ret)
            i += 1
        print(ret)
        print(self.dic[(key,ret)])
        return self.dic[(key,ret)] 
