class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = defaultdict(int)
        l_2 = defaultdict(int)
        for n in s:
            l[n] += 1
        for n in t:
            l_2[n] += 1
        return l == l_2

        