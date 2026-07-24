class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = defaultdict(int)
        for n in nums:
            if dup[n]:
                return True
            dup[n] = 1
        return False

# time : O(n) , space : O(n)