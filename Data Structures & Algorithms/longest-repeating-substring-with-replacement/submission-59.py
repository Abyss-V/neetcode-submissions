class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        d = defaultdict(int)
        m = 0
        s_list = []
        freq = 0
        while right < len(s):
            d[s[right]] += 1
            freq = max(freq,d[s[right]])
            while ((right - left + 1) - freq) > k:
                
                d[s[left]] -= 1
                left += 1
            
            m = max(m, right - left + 1) 
            
            right += 1
        return m 
        