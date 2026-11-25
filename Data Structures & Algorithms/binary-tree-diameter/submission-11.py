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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        m = 0
        dep = 0

        def dfs(root):
            nonlocal m,dep
            if not root:
           
                return 
    
            dep = max(self.maxDepth(root.left) + self.maxDepth(root.right),dep)
            dfs(root.left)
            dfs(root.right)
   
            
            

        dfs(root)
        
        return dep 

# time: O(n); space:O(1)