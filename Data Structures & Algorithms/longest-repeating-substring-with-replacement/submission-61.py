class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        count = defaultdict(int)
        m = 0
        freq = 0
        while right < len(s):
            
            freq = max(freq,count[s[right]])
            while  (((right - left)) - freq) > k:
                # m = max(m,(right - left))
                count[s[left]] -= 1
                left += 1
            
            m = max(m,(right - left) + 1)
            count[s[right]] += 1
            right += 1
        return m
