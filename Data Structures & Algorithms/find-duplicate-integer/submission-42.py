class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        m = max(nums)
        j = 0
        if m != len(nums):
    
            while True:
                
                i = nums[i]
                j = nums[nums[j]]

                if j == i:
                    break
            j = 0
            while True:
                i = nums[i]
                j = nums[j]
                if  i == j:
                    break
            return i
        return -1