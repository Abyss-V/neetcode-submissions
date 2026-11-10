class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        m = float("inf")
        middle = 0
        while l <= r:
            middle = (l+r) // 2
            m = min(m,nums[middle])

            if nums[-1] > nums[0] and nums[middle] <= nums[-1]:

                r = middle - 1
     
            elif nums[-1] > nums[0] and nums[middle] > nums[-1]:
                
                l = middle + 1
            elif nums[-1] < nums[0] and nums[middle] <= nums[-1]:
                
                r = middle - 1
            else:
                
                l = middle + 1
   
        return m


# time: O(log n); space: O(1)

