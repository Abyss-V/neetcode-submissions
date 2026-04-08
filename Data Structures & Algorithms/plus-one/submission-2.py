class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i >= 0:
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                i -= 1 
                continue
        if digits[0] == 0:
            digits.append(1)
            return digits[::-1]
        return digits

# My brute force way