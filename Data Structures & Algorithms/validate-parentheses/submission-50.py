class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        path = {"(":")","{":"}","[":"]"}
        i = 0
        if len(s) == 1:
            return False
        while i < len(s):
            if s[i] not in path:
                if not stack:
                    return False
                if stack and i < len(s) and path[stack[-1]] != s[i]:
                    return False
                while stack:
                    
                        if  i < len(s) and stack[-1] in path and path[stack[-1]] == s[i]:
                            stack.pop()
                            i += 1
                        else:
                            break
                
            else:
                    stack.append(s[i])
                    i+=1
        if stack:
            return False
        return True