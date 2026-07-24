class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 1
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                return nums[slow]
            
            slow += 1
            fast += 1
        slow = 0
        fast = 2
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                return nums[slow]
            
            slow += 1
            fast += 1
        slow = 0
        fast = 3
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                return nums[slow]
            
            slow += 1
            fast += 1
        slow = 0
        fast = len(nums) - 1
        while slow < fast:
            if nums[slow] == nums[fast]:
                return nums[slow]
            slow += 1
            fast -= 1
        return 0 
            