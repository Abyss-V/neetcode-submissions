class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha_1 = [0] * 26
        alpha_2 = [0] * 26
        for n in s:
            alpha_1[ord(n) - ord('a')] += 1
        for n in t:
            alpha_2[ord(n) - ord('a')] += 1
        return alpha_1 == alpha_2
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        i = 0
        dic = defaultdict(list)
        while i < len(strs):
                dic[''.join(sorted(strs[i]))].append(strs[i])
                i += 1

        return list(dic.values())
