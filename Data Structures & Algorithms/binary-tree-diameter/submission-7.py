# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        m = 0
        if not root:
            return 0
        def dfs(root):
            nonlocal m
            if root == None:
                return 0
            d1 = dfs(root.left)
            d2 = dfs(root.right)
            m = max(m,d1+d2)
            return 1 + max(d1,d2)
        dfs(root)
        return m

"""
Time Complexity: O(n) — each node is visited once.
Space Complexity: O(h) — recursion stack, where h is the tree height (worst case O(n), balanced O(log n)).
"""