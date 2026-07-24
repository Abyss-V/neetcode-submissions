class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        s_list = []
        s = 0
        candidates.sort()
        def dfs(i):
            nonlocal s
            if s == target :
                res.append(s_list.copy())
                return
            if i == len(candidates) or s > target:
                   
                return 
            
    
            s_list.append(candidates[i])
            s += candidates[i]
            dfs(i + 1)
            s -= s_list[-1]
            s_list.pop()
            while i + 1 < len(candidates) and candidates[i+1] == candidates[i]:
                i += 1
            dfs(i + 1)
        dfs(0)
  
        return res
            
            