class Solution:
    def isValid(self, s: str) -> bool:
        path = {'}':'{',')':'(',']':'['}
        stack = []
        if len(s) == 1:
            return False
        for c in s:

  
                if stack and c in path and path[c] == stack[-1]:
                    stack.pop()
                elif stack and c in path and path[c] != stack[-1]:
                    return False
                
                else:
                    stack.append(c)
        if len(stack) !=0:
            return False
        return True
