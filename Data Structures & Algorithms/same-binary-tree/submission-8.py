# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        f = True
        def dfs(ptr,qtr):
            nonlocal f
            if ptr and qtr and ptr.val != qtr.val:
                f = False
                return f
            if ptr and not qtr or qtr and not ptr:
                f = False
                return f
            if not ptr or not qtr:
                return f
            
        
            dfs(ptr.left,qtr.left)
            dfs(ptr.right,qtr.right)
        dfs(p,q)
        return f
# time : O(n) , space: O(n)   