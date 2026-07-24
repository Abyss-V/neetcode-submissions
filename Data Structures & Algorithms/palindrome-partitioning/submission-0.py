class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0 
        j = len(s) - 1
    
        while i < j:
            if not s[j].isalnum():
                j -= 1
                continue
            if not s[i].isalnum():
                i += 1
                continue

            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
    def partition(self, s: str) -> List[List[str]]:
        pal = []
        res = []
        def dfs(i):
            nonlocal pal
            if i >= len(s):
               
                res.append(pal.copy())
              
                return
   
            for j in range(i,len(s)):
                print(i,j)
                print(s[i:j])
                if s[i:j+1] and self.isPalindrome(s[i:j+1]):
                    pal.append(s[i:j+1])
                    dfs(j+1)
                    pal.pop()
            
            
           
            
           
            
            
         
                
            
            
           
 
           
            
            
    
        dfs(0)
        
        print()
        return res