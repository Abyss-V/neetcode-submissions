class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        m = 0
        while j < len(prices):
            print(prices[i])
            print(prices[j])
            print("zzzzz")
            if prices[i] <= prices[j]:
                m = max(m,prices[j] - prices[i])
                j += 1
            elif prices[i] > prices[j]:
                i = j
                j += 1
            else:
        
                i += 1
                j += 1
     
         

                
        return m