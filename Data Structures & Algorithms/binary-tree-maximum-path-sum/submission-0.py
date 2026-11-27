# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        dep = [root.val]
        m = 0
        def dfs(root):
            nonlocal dep,m
            if not root:
                
                return 0 
            
         
            left = dfs(root.left)
            right = dfs(root.right)
            l = max(left,0)
            r = max(right,0)
            dep[0] = max(dep[0],root.val+l+r)
            return root.val + max(l,r)

        dfs(root)
        return dep[0]

#time:O(n);space:O(n)