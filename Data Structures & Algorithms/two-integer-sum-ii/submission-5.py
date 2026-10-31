class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        nums = numbers
        while i < j:
            if nums[i] + nums[j] == target:
                return [i+1,j+1]
            elif nums[i] + nums[j] < target:
                i +=1
            else:
                j -= 1
        return []
    
# time: O(n); space: O(n)