class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        alpha_s = [0 for a in alpha]
        alpha_t = [0 for a in alpha]
        for a in s:
            alpha_s[ord(a) - ord('a')] += 1
        for a in t:
            alpha_t[ord(a) - ord('a')] += 1
        if alpha_s != alpha_t:
            return False
        
        return True
        