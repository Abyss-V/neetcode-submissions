class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed))
        fleet = []
        res = []
        for c in cars:
          
            while fleet and target//fleet[-1][1] <= target//c[1]:
                res.append(fleet[-1])
                fleet.pop()
            fleet.append(c)            
        return len(res)