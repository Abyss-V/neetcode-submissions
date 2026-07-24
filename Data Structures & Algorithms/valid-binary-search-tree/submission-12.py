# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        valid = True

        def dfs(root,limit):
            nonlocal valid
            if not root:
                return None
            if not (root.val > limit[0] and root.val < limit[1]):
                valid = False
            dfs(root.left,(limit[0],root.val))
            dfs(root.right,(root.val,limit[1]))
        dfs(root.left,(float("-inf"),root.val))
        
        dfs(root.right,(root.val, float("inf")))
        
        return valid

# time : O(n), space: O(n)