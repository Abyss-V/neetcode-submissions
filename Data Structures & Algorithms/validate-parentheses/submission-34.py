class Solution:
    def isValid(self, s: str) -> bool:
        path = {"{":"}","(":")","[":"]"}
        stack = []
   
        for c in s:
            if c not in path:
                if stack:
                    if path[stack[-1]] != c:
                        return False
                    else:
                        stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if stack:
            return False
        return True