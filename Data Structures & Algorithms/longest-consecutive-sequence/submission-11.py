class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        mx = 0
        count = 0
        if nums == []:
            return 0
        prev = nums[0]
        i = 1
        print(nums)
        while i < len(nums):
            if prev == nums[i]:
                i += 1
                continue
            if prev + 1 == nums[i]:
                count += 1
            else:
                 mx = max(mx,count)
                 count = 0

            prev = nums[i]
            i += 1
    
        return count + 1 if count > mx else mx + 1