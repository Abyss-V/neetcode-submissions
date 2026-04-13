from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        freq = []
        for k,v in c.most_common(k):
            freq.append(k)
        return freq
# Optimized solution using Counter