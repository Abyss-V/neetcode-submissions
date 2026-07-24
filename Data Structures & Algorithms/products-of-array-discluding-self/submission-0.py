class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        pref = 1
        for n in nums:
            pref *= n
            prefix.append(pref)
        suff = 1
        for i in range(len(nums)-1,-1,-1):
            suff *= nums[i]
            suffix.append(suff)
        suffix = suffix[::-1]
        print(prefix)
        print(suffix)
        res = []

        i = -1
        j = 1
        while i < len(nums):
            if i == -1:
                res.append(suffix[j])
                i += 1
                j += 1
            if j == len(nums):
                res.append(prefix[i])
                break
            res.append(prefix[i]*suffix[j])
            i+= 1
            j+=1
        return res