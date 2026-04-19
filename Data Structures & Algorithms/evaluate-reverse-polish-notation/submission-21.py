class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = 0
        nums = []
        while i < len(tokens):
            if tokens[i] not in ('+','-','*','/'):
                print(nums)
                nums.append(tokens[i])
                i += 1
            else:
                if tokens[i] == '+':
                    tokens[i] = int(nums.pop()) + int(nums.pop())
                elif tokens[i] == '-':
                    l = int(nums.pop()) 
                    bl = int(nums.pop()) 
                    tokens[i] = bl - l
                elif tokens[i] == '*':
                    tokens[i] = int(nums.pop()) *  int(nums.pop())
    
                elif tokens[i] == '/':
                    l = int(nums.pop()) 
                    bl = int(nums.pop()) 
                    tokens[i] = int(bl/l)
        return int(tokens[-1])

# another solution : time:o(n), space:o(n)