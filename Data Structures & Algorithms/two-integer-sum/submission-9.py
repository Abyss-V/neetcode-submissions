class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        dic = {}
        for i,n in enumerate(nums):
            if n in dic and n + n == target:
                return [dic[n],i]
            if n not in dic:    
                dic[n] = i
        for n in nums:
            if 2*n != target and target - n in dic:
                return [dic[n], dic[target - n]]
            

        return []
    

# time : o(n) , space: o(n)