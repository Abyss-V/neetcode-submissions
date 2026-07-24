class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        output = []
        nums.sort()
        print(nums)
        while i < len(nums):
            while i > 0 and i < len(nums) and nums[i] == nums[i - 1]:
                    i += 1
            k = i + 1
            j = len(nums) - 1
            while k < j:
                
                
                if k >= j:
                    break     
                if nums[k] + nums[j] == -nums[i] :
                    output.append([nums[i],nums[j] , nums[k]])
                    k += 1
                    j -= 1
                    while k > 0 and k < j and nums[k] == nums[k - 1]:
                        k += 1
                    while j > k and  j <= len(nums) - 2 and nums[j] == nums[j + 1]:
                        j -= 1
                    continue
                elif nums[j] + nums[k]  > -nums[i]:
                    j -= 1
                    continue
                    
                elif nums[j] + nums[k] < -nums[i]:
                    k += 1
                    continue
    
            
            i += 1
        return output
