class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 1
        u = set()
        m = 0
        res = 0
        if s.isspace() or len(s) == 1:
            return 1
        while j < len(s):
            while s[j] in u:
                m = max(m,len(u))
                u.remove(s[i])
                i += 1
                continue
            
            u.add(s[i])
            u.add(s[j])
            j += 1

        return max(m,len(u))
    


# time : o(n^2) and space:o(n)