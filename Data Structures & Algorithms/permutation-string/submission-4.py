class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1) - 1
        count = defaultdict(int)
        s1_count =  Counter(s1)

        if s1_count == Counter(s2):
            return True
        while right < len(s2):
            k = left
            while k <= right:
                count[s2[k]] += 1
                k += 1

            if s1_count == count:
                return True
            else:
                left += 1
                right += 1
                count = defaultdict(int)
            
        return False