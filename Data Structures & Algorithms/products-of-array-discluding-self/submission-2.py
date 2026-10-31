class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        prefix = []
        s = 1
        suffix = []
        results = []
        for i,n in enumerate(nums):
            p *= nums[i]
            prefix.append(p)
        for j in range(len(nums)-1,-1,-1):
            s *= nums[j]
            suffix.append(s)
        suffix = suffix[::-1]

        for i,n in enumerate(nums):
            if i == 0:
                results.append(suffix[i+1])
            elif i == len(nums) -1:
                results.append(prefix[i-1])
            else:
              
                results.append(prefix[i-1] * suffix[i+1])

        return results