class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res =[ 0 for  _ in temperatures]
        for i,t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
                
  
            stack.append(i)

        return res

# time : O(n); space:O(n)   