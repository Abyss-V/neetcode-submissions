class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = set(("+","-","*","/"))
        if len(tokens) == 1:
                return int(tokens[0])

       
        for t in tokens:
                if t in op and len(stack) >= 2:
                        n_2 = stack.pop()
                        n_1 = stack.pop()
                        if t == "+":
                                        stack.append(int(n_1) + int(n_2))
                        if t == "-":

                                        stack.append(int(n_1) - int(n_2))
                                       
                        if t == "/":
                                        stack.append(int(int(n_1) / int(n_2)))
                                
                        if t == "*":
                                        stack.append(int(n_1) * int(n_2))
                              
                else:
                        stack.append(t)
                        
           
               
    
                                        
        print(stack)

        return stack[0]
