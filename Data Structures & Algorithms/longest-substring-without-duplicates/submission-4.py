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

                i += 1
                m = max(m,len(u))
                u = set()
                j = i + 1
            if s[i] not in u:

                u.add(s[i])
            if s[j] not in u:
                u.add(s[j])
            j += 1

        return max(m,len(u))
    


# time : o(n^2) and space:o(n)