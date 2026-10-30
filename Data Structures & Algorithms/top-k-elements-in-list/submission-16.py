class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mx = defaultdict(int)
        

        m = 0
        for n in nums:
            mx[n] += 1
     
        res = [[] for _ in range(len(nums))]
        for key in mx:
            res[mx[key] - 1].append(key)
        r = [n for n in res if n!=[]][-k:]
        results = []
        for j in range(len(r) - 1,-1,-1):
            if k == 0:
                break
            if len(r[j]) <= k:
                results += r[j]
                k -= len(r[j])
          
            else:
            
                l = len(r[j]) - k
                results += r[j][-l:]
                k -= l
                
        return results