class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        output = None
        op = set(("+","-","*","/"))
        if len(tokens) == 1:
                return int(tokens[0])

        i = 0
        while i < len(tokens) and len(tokens) != 0:
                if tokens[i] in op:
                        
                        if tokens[i] == "+":
                                # print(output)
                                # print(n)
                                        tokens[i] =  int(tokens[i-1]) + int(tokens[i-2])
                        if tokens[i] == "-":
                                # print(tokens[i-1])
    
                                        
                                        tokens[i] =   int(tokens[i-2]) - int(tokens[i-1])
                                        
                        if tokens[i] == "/":

                                        tokens[i] =   int(int(tokens[i-2]) / int(tokens[i-1]))
                                
                        if tokens[i] == "*":
                                # print(output)
                                tokens[i] = int(tokens[i-1]) * int(tokens[i - 2])
                                # print(output)
                        tokens.pop(i - 1)
                        tokens.pop(i - 2)
                        i -= 2
           
                i += 1
    
                                        
            
        # print(stack)

        return tokens[0]
