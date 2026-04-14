class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefix = 1
        for n in nums:
            output.append(prefix)
            prefix *= n
        i = len(nums) - 1
        prefix = 1
        while i >= 0:
            output[i] *= prefix
            prefix *= nums[i]
            i -= 1
        return output
# improved o(n) attempt with the help of video explanation of the algo