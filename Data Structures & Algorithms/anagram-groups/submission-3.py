class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        i = 0
        dic = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            dic[tuple(count)].append(s)
        return list(dic.values())
# time : o(n*m) n = number of strings ; m = length of string, space: o(n)