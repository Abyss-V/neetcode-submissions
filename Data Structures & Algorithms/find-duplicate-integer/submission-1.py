class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        rep = defaultdict(int)
        m = (0,-1)
        for i,n in enumerate(nums):
            rep[n] += 1
            m = (rep[n],i) if rep[n] > m[0] else m
        return nums[m[1]] if m[1] > -1 else 0 
            