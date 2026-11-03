class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        j = 0
        i = 0
        res = 0
        count = defaultdict(int)

        while  j < len(s):
            count[s[j]] += 1
            while ((j - i) + 1 - max(count.values())) > k:
 
                count[s[i]] -= 1
                i+=1
        
            res = max(res,(j - i) + 1)
            j += 1
    
        return res
    

# time : O(n) ; space: O(m) where m is the number of unique characters