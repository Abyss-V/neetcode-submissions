class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(perm):
            if len(perm) == 0: 
                return [[]]
            per = dfs(perm[1:])
            r = []
            for p in per:
                for j in range(len(p)+1):
                    newper = p.copy()
                    newper.insert(j,perm[0])
                    r.append(newper)
            return r
        return dfs(nums)