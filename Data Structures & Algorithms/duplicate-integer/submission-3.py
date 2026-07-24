class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = set()
        for n in nums:
            if n in dup:
                return True
            dup.add(n)
        return False

# time : O(n) , space : O(n)