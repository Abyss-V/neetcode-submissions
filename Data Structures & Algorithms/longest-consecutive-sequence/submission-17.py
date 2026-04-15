class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        i = 0
        m = 0
        for n in nums:
            if n - 1 not in s:
                while n + i in s:
                    i += 1
                m = max(m,i)
                i = 0
            i = 0
        return m
           

# solved with o(n) with the help of the video