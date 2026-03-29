class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        j = i + 1
        k = len(nums)//2
        l = sorted(nums)
        print(l)
        res = []
        while i < len(nums):
                j = i
                while j < len(nums):
                    k = j
                    while k < len(nums): 
                        if  l[i] + l[j] + l[k] == 0 and sorted([l[i],l[j],l[k]]) not in res and k!=j and i!=j and k!=i:
                            res.append(sorted([l[i],l[j],l[k]]))
                        k+=1
                    j+=1
                i+=1
      
        return res