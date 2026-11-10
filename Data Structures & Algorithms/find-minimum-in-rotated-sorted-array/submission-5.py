class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        m = float("inf")
        middle = 0
        while l <= r:
            middle = (l+r) // 2
            m = min(m,nums[middle])
            m = min(m,nums[r])
            m = min(m,nums[l])
            print(l,r,middle)
            if nums[-1] > nums[0] and nums[middle] <= nums[-1]:
                print("dd")
                
                r = middle - 1
            if nums[-1] > nums[0] and nums[middle] > nums[-1]:
                
                l = middle + 1
            if nums[-1] < nums[0] and nums[middle] <= nums[-1]:
                
                r = middle - 1
            else:
                
                l = middle + 1
   
        return min(nums[middle],m)

            

