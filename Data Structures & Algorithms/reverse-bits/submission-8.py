class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = res << 1
            if n & 1 == 1:
                res |= 1
            n = n >> 1
        return res

# Explaination : what we did here is looping through all 32 bits
# shifting the res to the left by 1 so we can add the next bit
# adding n right most bit to the res right most with | and & operators
# shifting n to the right so we can get the next bit and add it in the next iteration
# keep doing this process till the loops finish and we get the bits reversed