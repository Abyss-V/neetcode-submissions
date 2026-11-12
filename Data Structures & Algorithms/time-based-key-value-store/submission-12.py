class TimeMap:

    def __init__(self):
        self.timestamp = defaultdict(list)
        
     
    def set(self, key: str, value: str, timestamp: int) -> None:
        


        self.timestamp[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        r = len(self.timestamp[key]) - 1
        l = 0
        m = (-1,-1)
        while l<=r:
            middle = (l+r) // 2

            if self.timestamp[key][middle][1] == timestamp:
                return  self.timestamp[key][middle][0]
            elif self.timestamp[key][middle][1] > timestamp:
                r = middle - 1
            else:
                m = (self.timestamp[key][middle][1],self.timestamp[key][middle][0]) if self.timestamp[key][middle][1] > m[0] else m
                l = middle + 1
        if m[0] == -1:
            return ""
        return m[1]
    

# set : time:O(1)
# get : time:O(logn)
# space: o(m*n); m number of keys and n number of values