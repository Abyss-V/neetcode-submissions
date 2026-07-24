class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        m = float("inf")
        while left <= right:
            middle = (left + right) // 2
            if nums[middle]  == target:
                return middle
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right


            if nums[right] > nums[left]  and target < nums[middle] and target > nums[left]:
                right = middle - 1
  
            elif target < nums[left] and nums[middle] > target and nums[middle] < nums[right]:

                right = middle - 1

            elif target > nums[left] and nums[middle] > target and nums[middle] > nums[right]:
                right = middle - 1
                

            else:
                left = middle + 1

        return -1