class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed))
   
        fleet = []
        fl = 0
        if len(position) == 1:
            return 1
        for c in cars:
       
            # if fleet:
            #     print(fleet[-1],(target-fleet[-1][0])//fleet[-1][1])
            #     print(c,(target-c[0])//c[1])
            while fleet and (target-fleet[-1][0])/fleet[-1][1] <= (target-c[0])/c[1]:
   
                fl += 1
                fleet.pop()
            
            fleet.append(c)

        return len(fleet)