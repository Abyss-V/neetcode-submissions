class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        substs = []
        nums.sort()
        def dfs(i):
            if i >= len(nums):
                res.append(substs.copy())
                return
            substs.append(nums[i])
            dfs(i + 1)
            while i < len(nums) - 1 and nums[i + 1] == nums[i]:
                i += 1
            substs.pop()
            dfs(i + 1)
        dfs(0)
        return res
