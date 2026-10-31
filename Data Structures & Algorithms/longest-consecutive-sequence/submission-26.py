class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)

        m = 0
        i = 0
        while i < len(nums):
            while i < len(nums) and nums[i] - 1 in seq:
                i+=1
          
            if i == len(nums):
                break

            mx = 1
            num = nums[i] + 1
            while num in seq:
                num += 1
                mx += 1 
        
            m = max(m,mx)
        
            i += 1
        return m

