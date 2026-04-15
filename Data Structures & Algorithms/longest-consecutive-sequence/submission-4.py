class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        consecutive = 0
        m = 0
        if nums == []:
            return 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i + 1] - 1:
                consecutive += 1
            else:
                if nums[i] != nums[i + 1]:
                    m = max(m,consecutive)
                    consecutive = 0
        if max(m,consecutive) == 0:
            return 1
        return max(m,consecutive) + 1

# my brute force way