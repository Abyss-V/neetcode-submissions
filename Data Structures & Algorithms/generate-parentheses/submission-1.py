# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         perm = ""
#         res = []
        
       
#         i = 0
#         opn = 0
#         close = 0
#         def dfs(par):
#             nonlocal opn,close,n,perm
#             if len(perm) == n*2:
#                 res.append(perm)
#                 perm = ""
#                 return
            
                

            
          
#         dfs("(")
 
#         print(perm)
#         return res



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
            print(opn)
            print(close)
            print(n)
            if opn == close == n: 
                
                res.append(perm)
                return
            if opn < n:
                dfs(perm +"(",opn+1,close)
                

            if close < opn:
                dfs(perm +")",opn,close+1)
            
          
        print(dfs("(",opn+1,close))
        
        return res

