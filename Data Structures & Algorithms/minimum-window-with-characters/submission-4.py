class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        alpha_s = defaultdict(int)
        alpha_t = defaultdict(int)
        have = 0
        m = (float("inf"),0)
        need=0
        if s == t:
            return t
        for c in t:
            alpha_t[c] += 1
        for k in alpha_t:
            need +=1
        for r in range(len(s)):
            alpha_s[s[r]] += 1
            if alpha_t[s[r]] != 0 and alpha_s[s[r]] == alpha_t[s[r]]:
                print(s[r],alpha_s[s[r]])
                have += 1
                print(have)
                print(need)
            
            while have == need:
                print("ehr")
                m = (r-l+1,(l,r)) if m[0] > r-l+1 else m
                
                if l < len(s) and s[l] in alpha_t:
                    alpha_s[s[l]] -= 1
                    if alpha_s[s[l]] < alpha_t[s[l]]:
                        have -= 1
                  
                    
                l+=1
        if not m[1]:
            return ""
        return s[m[1][0]:m[1][1] + 1]
            


           