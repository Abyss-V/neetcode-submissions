class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []
        temp = temperatures
        i = 1
        for j in range(len(temp)-1,-1,-1):
            stack.append((temp[j],j))
        while stack:
            
            if i == len(temp):
                res.append(0)
                i = stack[-1][1] + 1
                stack.pop()
                continue


       
            if temp[i] > stack[-1][0]:
                res.append(i - stack[-1][1])
                i = stack[-1][1] + 1
                stack.pop()
            i += 1
      
        return res

