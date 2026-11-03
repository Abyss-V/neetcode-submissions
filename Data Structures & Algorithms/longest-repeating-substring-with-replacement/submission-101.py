class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        j = 0
        i = 0
        res = 0
        count = defaultdict(int)
        mx = 0
        while  j < len(s):
            count[s[j]] += 1
            mx = max(count[s[j]],mx)
            while ((j - i) + 1 - mx) > k:
 
                count[s[i]] -= 1
                i+=1
        
            res = max(res,(j - i) + 1)
            j += 1
    
        return res
    

# time : O(n) ; space: O(m) where m is the number of unique characters