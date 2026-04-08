class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res ^= i ^ nums[i]
        return res

# Explanaition : we take advantage of xor operator when two numbers xor each other result is 0
# We intialize res with len of the nums and we use 2 xor operators
# canceling out matching numbers that appears in both i and inside nums list leaving the missing number
# this is what it does : res = n ^ (0 ^ nums[0]) ^ (1 ^ nums[1]) ^ (2 ^ nums[2])
# Which become's : xorr = (0 ^ 1 ^ 2 ^ 3) ^ (3 ^ 0 ^ 1) Leaving 2