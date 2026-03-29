class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = float("-inf")
        i = 0
        while i < len(prices)-1:
            j = i + 1
            while j < len(prices):
                if prices[i]<prices[j]:
                    profit = prices[j] - prices[i]
                    max_profit = max(max_profit,profit)
                j+=1
            i += 1
        if max_profit == float("-inf"):
            return 0
        return  max_profit
