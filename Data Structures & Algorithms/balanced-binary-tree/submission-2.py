# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        dep = 0
        def dfs(root,m):
            nonlocal dep
            if not root:
                dep = max(m,dep)
               
                return None
       
            dfs(root.left,m+1)
            dfs(root.right,m+1)
            
        dfs(root,0)
        return dep
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
 
        f = True
        def dfs(root):
            nonlocal f
            if not root:

                return f
            if self.maxDepth(root.left) > self.maxDepth(root.right) + 1 or self.maxDepth(root.left) +1 < self.maxDepth(root.right):
                f = False
                return False
            
            
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return f