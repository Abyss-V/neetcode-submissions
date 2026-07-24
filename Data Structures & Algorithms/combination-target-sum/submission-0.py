class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        s_list = []
        s = 0
        def dfs(i):
            if i >= len(nums):
                if sum(s_list) == target:
                    res.append(s_list.copy())
                
                return
            if sum(s_list) >= target:
                if sum(s_list) == target:
                    res.append(s_list.copy())
                
                return
          
            s_list.append(nums[i])
            dfs(i)
            s_list.pop()
            dfs(i+1)
        dfs(0)
        return res