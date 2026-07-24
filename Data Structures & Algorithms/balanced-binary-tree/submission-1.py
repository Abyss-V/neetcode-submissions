# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        m = 0
        found = True
        if not root:
            return True
        depth = 0
        def dfs(lastroot,root,depth):
            nonlocal m,found
            if root == None:

                return 0
            
            d1 = dfs(root,root.left,depth + 1)
            
            d2 = dfs(root,root.right,depth + 1)
            
            if d1 > d2 + 1 or d2 > d1 + 1:
                print(root.val,d1,d2)
                found = False

            return 1 + max(d1,d2)
        dfs(root,root,depth)
        return found

"""
Time Complexity: O(n) — each node is visited once.
Space Complexity: O(h) — recursion stack, where h is the tree height (worst case O(n), balanced O(log n)).
"""