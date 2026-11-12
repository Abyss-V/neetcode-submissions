class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            middle = (l+r) // 2
            
            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            elif nums[middle] == target:
                return middle
            elif l == r:
                return -1
            elif nums[middle] > nums[l] and target < nums[middle] and target > nums[l]:
                r = middle - 1
            elif nums[middle] > nums[l] and target > nums[middle] and target > nums[l]:
                l = middle + 1
            elif nums[middle] < nums[l] and target > nums[middle] and target > nums[l]:
                r = middle - 1
            elif nums[middle] < nums[l] and target > nums[middle] and target < nums[l]:
                l = middle + 1
            elif nums[middle] < nums[l] and target < nums[middle] and target < nums[l]:
                r = middle - 1
            else:
                l = middle + 1
        return -1
    

    # time: O(logn); space:O(1)