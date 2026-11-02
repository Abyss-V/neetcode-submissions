class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        found = set()
        leng = 0
        i = 0
        mx = 0
        j = 0
        if len(s) == 1:
            return 1
        while j < len(s):
            if s[j] in found:
                while s[j] in found:
                    mx = max(leng,mx)
                    found.remove(s[i])
                    leng -= 1
                    i+=1
                found.add(s[j])
                j+=1
                leng += 1
           
            else:
            
                found.add(s[j])
                leng += 1
                j += 1
            
        
        return max(leng,mx)
