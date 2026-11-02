class Solution:
    def isAnagram(self, s: str) -> bool:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        alpha_s = [0 for a in alpha]

        for a in s:
            alpha_s[ord(a) - ord('a')] += 1

        
        return tuple(alpha_s)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)
        for s in strs:
            ana[self.isAnagram(s)].append(s)
        res = []
        for k in ana:
            res.append(ana[k])
        return res
            