class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = 0
        nums = []
        for t in tokens:
            if t not in ('+','-','*','/'):
                nums.append(int(t))
            else:
                val_1 = nums.pop()
                val_2 = nums.pop()
                if t == '+':
                    nums.append(val_1 + val_2)
                elif t == '-':
                   nums.append(val_2 - val_1)
                
                elif t == '*':
                    nums.append(val_1 * val_2)
    
                elif t == '/':
                   nums.append(int(val_2/val_1))
                
        return nums[0]

# solution with a hint : time:o(n), space:o(n)