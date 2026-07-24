class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1
        m = float("inf")
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] <= nums[right]:
                m = min(m,nums[middle])
                right = middle - 1

            elif nums[middle] > nums[right]:
                print("here")
                m = min(m,nums[middle])
                left = middle + 1

        return m