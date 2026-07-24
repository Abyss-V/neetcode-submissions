class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        s_list = []
        s = 0
        def dfs(i):
            nonlocal s
            if i >= len(nums):
                if s == target:
                    res.append(s_list.copy())
                
                return
            if s >= target:
                if s == target:
                    res.append(s_list.copy())
                
                return
          
            s += nums[i]
            s_list.append(nums[i])
            dfs(i)
            s -= s_list[-1]
            s_list.pop()
            dfs(i+1)
        dfs(0)
        return res

"""
**Time Complexity:** 
The algorithm has a maximum recursion 
depth of approximately (T/m), where (T) is 
the target and (m) is the smallest value in
`nums`, since the smallest number can be
chosen at most (T/m) times before reaching
the target. Each recursive call branches
into two choices—include the current
number (`dfs(i)`) or skip it (`dfs(i+1)`), forming a binary recursion tree with approximately (2^{T/m}) recursive calls. Because the running sum `s` is updated in constant time, each call performs (O(1)) work (excluding the cost of copying a valid combination). Therefore, the overall time complexity is **(O(2^{T/m}))**.

**Space Complexity:** 
The maximum recursion depth is (O(T/m)), 
and the temporary list `s_list` can also 
contain at most (T/m) elements. Thus, the 
auxiliary space complexity (excluding the 
output list `res`) is **(O(T/m))**. The 
space required to store the resulting
combinations is not included in the 
auxiliary space complexity.

"""