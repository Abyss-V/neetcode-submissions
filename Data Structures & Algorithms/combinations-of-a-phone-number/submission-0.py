class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        comb = []
        phone = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        s = ""
        if len(digits) == 0:
            return []
        def dfs(j,s):
            if j >= len(digits):
                comb.append(s)
                return
            for i in range(len(phone[int(digits[j])])):
                
                dfs(j+1,s+phone[int(digits[j])][i])
        dfs(0,s)
        return comb