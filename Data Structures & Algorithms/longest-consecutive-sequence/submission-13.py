class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consec = set(nums)
        length = 0
        mx = 0
        if nums == []:
            return 0
        for n in nums:
            if n - 1 not in consec:
                length = 0
                number = n + 1
                while number in consec:
                    number = number + 1
                    length += 1
                mx = mx if mx > length else length
            

        
        
        
        
        return mx + 1