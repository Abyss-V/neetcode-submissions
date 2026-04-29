class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        cut = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i + 1]:
                cut = i + 1
        right = cut
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        left = cut
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
                
        return -1