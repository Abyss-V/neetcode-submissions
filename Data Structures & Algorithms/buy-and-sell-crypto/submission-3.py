class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        m = 0
        while j < len(prices):
            if prices[i] <= prices[j]:
                m = max(m,prices[j] - prices[i])
                j += 1
            elif prices[i] > prices[j]:
                i = j
                j += 1

                
        return m
# Time: O(n)
# Space: O(1)