class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha_1 = [0] * 26
        alpha_2 = [0] * 26
        for n in s:
            alpha_1[ord(n) - ord('a')] += 1
        for n in t:
            alpha_2[ord(n) - ord('a')] += 1
        return alpha_1 == alpha_2


# time : o(n+m) ,space:o(1) because of array is fixed 26 alpha length