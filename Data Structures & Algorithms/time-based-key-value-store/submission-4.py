class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
            self.dic[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        left = 0
        res = ""
        stamps = self.dic.get(key, [])
        print(stamps)
        right = len(stamps) - 1
        while left <= right:
            middle = (left + right) // 2
            if stamps[middle][1] <= timestamp:
                res = stamps[middle][0]
                left = middle + 1
            else:
                right = middle - 1 
        return res

# set : time: O(1) , space : O(n) ; get: time: O(log k) , space: O(1)