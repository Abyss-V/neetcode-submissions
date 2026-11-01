class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
   
        i = 0
        res = []
        while i < len(nums):
            while i > 0 and i < len(nums) and nums[i-1] == nums[i]:
                i += 1
            j = i + 1
            k = len(nums) - 1
            while j < k:
                
                while k > j and k < len(nums) - 1 and nums[k+1] == nums[k]:
                    k-=1
                while j > i + 1 and j < k and nums[j-1] == nums[j]:
                    j+=1
                if j >= k:
                    break
                if nums[j] + nums[k] == -nums[i]:
                    res.append([nums[i],nums[j],nums[k]])
                    j +=1
                    k-=1
                    continue
                
                if  nums[j] + nums[k] < -nums[i]:
                  
                    j += 1
                    continue
 
                if nums[j] + nums[k] > -nums[i]:
                    
                    k -= 1
                    continue
            
                    
            i+=1

        return res

# time: O(n^2) ; space: O(1) (auxiliary space for sorting and output list is excluded)