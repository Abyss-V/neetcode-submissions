class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        op = set(["+","-","/","*"])         
        for t in tokens:
            if len(s)>=2 and t in op:
            
                fnum = s.pop()
                snum = s.pop()
                if t == "+":
                    s.append(int(snum) + int(fnum)) 
                if t == "-":
                    s.append(int(snum) - int(fnum)) 
                if t == "*":
                    s.append(int(snum) * int(fnum)) 
                if t == "/":
                    s.append(int(int(snum) / int(fnum)))
            elif t not in op:
                s.append(t)

        return int(s.pop())

# time: O(n); space:O(n)