class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1) - 1
        alpha_1 = [0] * 26
        alpha_2 = [0] * 26
        k = 0


        if len(s1) > len(s2):
            return False
    
        for c in s1:
            alpha_1[ord(c) - ord('a')] += 1

        while k <= right:
            alpha_2[ord(s2[k]) - ord('a')] += 1 
            k += 1
 
        while right < len(s2):
            if alpha_2 == alpha_1:
                return True
            alpha_2[ord(s2[left]) - ord('a')] -= 1 
            left += 1 
            right += 1
            if right < len(s2):
                alpha_2[ord(s2[right]) - ord('a')] += 1
            
        
        return False
# Time: O(n)
# Space: O(1)