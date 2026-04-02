class Solution:
    def count_bits(self,n):
        count = 0
        while n:
            if n & 1: 
                count += 1
            n = n >> 1
        return count
    def countBits(self, n: int) -> List[int]:
        output = []
        count = 0 
        i = n
        while i >= 0:
            count = self.count_bits(i)
            output.append(count)
            i -= 1
        return output[::-1]