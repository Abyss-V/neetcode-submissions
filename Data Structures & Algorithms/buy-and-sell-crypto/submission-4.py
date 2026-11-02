class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 0
        maxProfit = 0
        while j < len(prices):
            if prices[i] > prices[j]:
                i += 1
            else:
                maxProfit = max(maxProfit,(prices[j]-prices[i]))
                j += 1
        return maxProfit