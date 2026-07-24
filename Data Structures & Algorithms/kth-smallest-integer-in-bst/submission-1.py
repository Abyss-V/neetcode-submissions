# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        found = 0
        count = 1
        res = []
        def dfs(root):
            nonlocal k,found,count
            if found:
                return None
            if not root:
                return None
           
            res.append(root.val)
                

            dfs(root.left)
            dfs(root.right)
        dfs(root)
        res.sort()
        return res[k - 1]