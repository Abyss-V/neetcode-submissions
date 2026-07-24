class Solution:
    def isValid(self, s: str) -> bool:
        pat = {']':'[',')':'(','}':'{'}
        stack = []
        for i in range(0,len(s)):
            print(stack)
            if s[i] in pat  and stack and stack[-1] == pat[s[i]]:
                stack.pop()
            elif s[i] in pat and stack  and stack[-1] != pat[s[i]] :
                return False
            else:
                stack.append(s[i])
        return True if not stack else False