class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        s_list = []
        s = 0
        def dfs(i):
            nonlocal s
            if i >= len(nums):
                if s == target:
                    res.append(s_list.copy())
                
                return
            if s >= target:
                if s == target:
                    res.append(s_list.copy())
                
                return
          
            s += nums[i]
            s_list.append(nums[i])
            dfs(i)
            s -= s_list[-1]
            s_list.pop()
            dfs(i+1)
        dfs(0)
        return res