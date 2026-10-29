class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        i = 0
        a = "abcdefghijklmnopqrstuvwxyz"
        alpha_s = {u:0 for u in a}
        alpha_t = {u:0 for u in a}
        if(len(s) != len(t)):
            return False
        while i < len(s):
            alpha_s[s[i]] += 1
            alpha_t[t[i]] += 1 
            i += 1
        if alpha_s != alpha_t:
            return False
        return True