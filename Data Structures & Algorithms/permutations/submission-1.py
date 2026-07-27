class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        pal = []
        res = []
        def dfs(nums):
            
            if len(nums) == 0:
                return [[]]
            re = dfs(nums[1:])
            res = []
            for p in re:
                for i in range(len(nums)):
                    
                    copy = p.copy()
                    copy.insert(i,nums[0])
                    res.append(copy) 
            
            return res 
        print(dfs(nums))
        return dfs(nums)