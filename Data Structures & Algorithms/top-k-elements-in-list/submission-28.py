
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}


        res = [[] for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1

        for key,value in freq.items():
            res[value].append(key)
        j = k
        i = len(res) - 1
        result = []
        while  i >= 0 and k > 0:
            if res[i] != []:
                result += res[i]
                k -= 1
            
            i -= 1

        return result[0:j]

# other way to solve it