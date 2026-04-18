class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = 0
        nums = []
        while len(tokens) != 1:
            nums = []
            i = 0
            while  len(tokens) != 1  and tokens[i] not in ('+','-','*','/'):
                nums.append(tokens[i])
                i += 1
            if len(nums)>=2:
                print(tokens)
                if tokens[i] == '+':
                    tokens[i] = int(nums.pop()) + int(nums.pop())
                    tokens.pop(i - 1)
                    tokens.pop(i - 2)
                elif tokens[i] == '-':
                    f = int(nums.pop()) 
                    bf = int(nums.pop()) 
                    tokens[i] = bf - f
                    tokens.pop(i - 1)
                    tokens.pop(i - 2)
                
                elif tokens[i] == '*':
                    tokens[i] = int(nums.pop()) *  int(nums.pop())
                    tokens.pop(i - 1)
                    tokens.pop(i - 2)
    
                elif tokens[i] == '/':
                    f = int(nums.pop()) 
                    bf = int(nums.pop()) 
                    tokens[i] = int(bf/f)
                    tokens.pop(i - 1)
                    tokens.pop(i - 2)
                
        print(tokens)
        return int(tokens[0])