class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        j = 1
        nums.sort()
        while j < len(nums):
            if not (nums[i] < nums[j]):
                return nums[j]
            i+=1
            j+=1
        return -1