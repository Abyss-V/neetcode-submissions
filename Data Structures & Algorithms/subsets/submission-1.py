class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        substs = []
        def dfs(i):
            if i >= len(nums):
                res.append(substs.copy())
                return None
            
            substs.append(nums[i])
            dfs(i + 1)
            substs.pop()
            dfs(i + 1)

        dfs(0)
        return res

# Time: O(n · 2ⁿ)
# Space: O(n · 2ⁿ)