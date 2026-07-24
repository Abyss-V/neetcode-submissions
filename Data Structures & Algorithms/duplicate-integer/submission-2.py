class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        u = set()
        for n in nums:
            if n in u:
                return True
            u.add(n)
        return False