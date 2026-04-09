class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1]*len(cost)
        def dfs(i):
            if i >= len(cost):
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return dp[i]
        n = dfs(0)
        p = dfs(1)
        return min(n,p)

# Solution made by looking at hints
