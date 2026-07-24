class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sp_pos = []
        stack = []
 
        for i,p in enumerate(position):
            sp_pos.append((speed[i],p))
        sp_pos = sorted(sp_pos,key=lambda x:x[1])
        stack = [sp_pos[0]]
        print(sp_pos)
        for i in range(1,len(sp_pos)):
            t_1 = (target - stack[-1][1]) / stack[-1][0]
            t_2 = (target - sp_pos[i][1]) / sp_pos[i][0]
            print(sp_pos[i])

            
            
            while stack and t_1 <= t_2:
                
                
                stack.pop()
                if stack:
                    t_1 = (target - stack[-1][1]) / stack[-1][0]
                    t_2 = (target - sp_pos[i][1]) / sp_pos[i][0]

                
            stack.append((sp_pos[i][0],sp_pos[i][1]))
        print(stack)
        return len(stack)
