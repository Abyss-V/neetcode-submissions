class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pattern = {"(":")","{":"}","[":"]"}
        if len(s)==1:
            return False
        for char in s[::-1]:
            if char in pattern:
                if len(stack) == 0 or stack[-1] != pattern[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        if len(stack) != 0:
            return False
        return True