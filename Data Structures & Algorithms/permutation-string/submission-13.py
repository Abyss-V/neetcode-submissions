class Solution:
    def isPerm(self,i,j,s):
        alpha = "abcdefghijklmnopqrstuvwxyz"
        a_c = [0 for _ in alpha]
        k = i
        while k <= j:
            a_c[ord(s[k]) - ord('a')] += 1
            k+=1
        return a_c

    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        j = len(s1) - 1
        perm_s1 = self.isPerm(i,j,s1) 
        while j < len(s2):
            if perm_s1 == self.isPerm(i,j,s2):
                return True 
            i+=1
            j+=1
        return False