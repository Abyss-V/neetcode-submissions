class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        path = {"(":")","[":"]","{":"}"}
        i  = 0
        while i  < len(s):
            if s[i] not in path:
                if not stack:
                    return False
                while stack:
                    if i < len(s) and s[i]  not in path and path[stack[-1]] == s[i]:
                        stack.pop()
                        i+=1
                
                    elif i < len(s) and s[i]  not in path and path[stack[-1]] != s[i]:
                        return False
                    else:
                       
                        break
        

            else:
        
                stack.append(s[i])
                i+=1

        if stack:
            return False
        return True