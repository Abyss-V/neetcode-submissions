class Solution:
    def isAnagram(self, s: str) -> bool:
        i = 0
        a = "abcdefghijklmnopqrstuvwxyz"
        alpha_s = [0 for _ in a]
 
   
        while i < len(s):
            alpha_s[ord(s[i])-ord('a')] += 1
   
            i += 1

        return alpha_s
 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {tuple(self.isAnagram(s)):[] for s in strs}
    
        for s in strs:
            res[tuple(self.isAnagram(s))].append(s)
        return [l for l in res.values()]