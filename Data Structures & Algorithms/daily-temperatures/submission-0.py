class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
  
        for i,t in enumerate(temperatures):
            print(stack)
            while stack and t > stack[-1][1]:
                
                j,t_pop = stack.pop()
                res[j] = i - j
            stack.append((i,t))
            

        return res