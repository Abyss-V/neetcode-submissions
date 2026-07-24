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
                return None
            dfs(root,root.left)
            dfs(root,root.right)
            tmp = root.left
            root.left = root.right
            root.right = tmp
            return root
        dfs(root,root)
        
        return root
"""
Time Complexity: O(n) — each node is visited exactly once.
Space Complexity: O(h) — recursion stack, where h is the tree height (worst case O(n), balanced O(log n)).
"""