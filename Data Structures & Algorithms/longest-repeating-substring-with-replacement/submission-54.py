class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        score = 1
        m = 0
        s_list = []
        frq = 0
        count = defaultdict(int)
        for c in s:
            s_list.append(c)
        while right < len(s_list):
            count[s_list[right]] += 1
            frq  = max(frq,count[s_list[right]])

            while abs(((right - left) + 1) - frq) > k:
                count[s_list[left]] -=  1
                left += 1
                
   
    
            m = max(m,(right + 1 - left))

            right += 1 

        return m  