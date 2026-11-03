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
        if len(s1) > len(s2):
            return False
        i = 0 
        j = len(s1) - 1 
        perm_s1 = self.isPerm(i,j,s1) 
        perm_s2 = self.isPerm(i,j,s2)
        print(perm_s1)
        if perm_s1 == perm_s2:
                return True 
        while j < len(s2):
            
            
            i+=1
            j+=1
            if j < len(s2):
                perm_s2[ord(s2[i-1]) - ord('a')] -= 1
                perm_s2[ord(s2[j]) - ord('a')] += 1
                print(s2[i:j+1],perm_s2)
                if perm_s1 == perm_s2:
                    return True 
        if perm_s1 == perm_s2:
                return True 
        return False