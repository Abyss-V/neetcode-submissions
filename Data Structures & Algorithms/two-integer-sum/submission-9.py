class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict={}
        for i,n in enumerate(nums):
                if my_dict.get(n):
                    my_dict[n].append(i)
                my_dict[n] = [i]
       
        for i,n in enumerate(nums):
            if my_dict.get(target - n) is not None and my_dict.get(n) is not None and my_dict[target - n].count(i) != 1:
                    return [i, my_dict[target - n][0]]
        return []