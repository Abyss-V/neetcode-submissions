# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        def dfs(lastroot,root):
            if root == None:
                return lastroot
            left = dfs(root,root.left)
            right = dfs(root,root.right)

            tmp = root.left
            root.left = root.right
            root.right = tmp
            return root
        dfs(root,root)
        
        return root