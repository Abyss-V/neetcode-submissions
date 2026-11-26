# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depth(self,root):
        dep = 0
        def dfs(root,n):
            nonlocal dep
            if not root:
                dep = max(dep,n)
                return
            dfs(root.left,n+1)
            dfs(root.right,n+1)
        dfs(root,0)
        return dep

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        r = [[] for _ in range(self.depth(root))]
        mx =  self.depth(root)
        def dfs(root,n):
            nonlocal r,mx
            if not root:
                return
            r[n - mx].append(root.val)
            dfs(root.left,n+1)
            dfs(root.right,n+1)
        dfs(root,0)
        return r