class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        count = defaultdict(int)
        m = 0
        freq = 0
        while right < len(s):
            count[s[right]] += 1
            freq = max(freq,count[s[right]])
            while  (((right - left) + 1) - freq) > k:
                count[s[left]] -= 1
                left += 1
            
            m = max(m,(right - left) + 1)
            
            right += 1
        return m
