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
    def generateParenthesis(self, n: int) -> List[str]:    
        res = []

        i = 0
        opn = 0
        stack = []
        close = 0
        def dfs(perm,opn,close):

            if opn == close == n: 
                
                res.append(perm)
                return
            if opn < n:
                dfs(perm +"(",opn+1,close)
                

            if close < opn:
                dfs(perm +")",opn,close+1)
            
          
        dfs("(",opn+1,close)
        
        return res

# Time: O(4ⁿ)
# Space: O(n · 4ⁿ)