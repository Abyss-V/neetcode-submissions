# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        m = 0
        if not root:
            return 0
        depth = 1
        def dfs(lastroot,root,depth):
            nonlocal m
            if root == None:

                return None,depth - 1
            _,d = dfs(root,root.left,depth + 1)
            m = max(m,d)
            _,d = dfs(root,root.right,depth + 1)
            m = max(m,d)

            return root,depth
        dfs(root,root, 1)

        return m