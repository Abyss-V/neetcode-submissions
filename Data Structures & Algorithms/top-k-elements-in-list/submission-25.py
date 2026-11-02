class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = defaultdict(int)
        for n in nums:
            c[n] += 1

      
        buck = [[] for _ in nums]
        for key in c:
            buck[c[key] - 1].append(key)

        res = []
        for l in buck:
            res += l

        return res[-k:]