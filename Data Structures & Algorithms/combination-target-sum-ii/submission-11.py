class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        s = 0 
        nums = []
        candidates.sort()
        print(candidates)
        def dfs(i):
            nonlocal s
            if s == target:
                res.append(nums.copy())
                return None
            if i >= len(candidates) or s > target:
                return None
            
            nums.append(candidates[i])
            s += candidates[i]
            
            dfs(i + 1)
            while i < len(candidates) - 1 and candidates[i+1] == candidates[i]:
                i += 1
            s -= nums[-1]
            nums.pop()
            
            dfs(i + 1)
            
        dfs(0)
        return res
        