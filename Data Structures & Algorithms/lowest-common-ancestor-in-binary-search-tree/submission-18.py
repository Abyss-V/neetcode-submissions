# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        found = None
        def dfs(root,p,q):
            nonlocal found
            if found:
                return found
            if not root:
                return
            if (root.val > p.val and root.val < q.val) or (root.val > q.val and root.val < p.val):
                found = root
            elif root.val == p.val or root.val == q.val:
                found = root
            if root.val > p.val and root.val > q.val:
                r1 = dfs(root.left,p,q)
            if root.val < p.val and root.val < q.val:
                r2 = dfs(root.right,p,q)

            return root
       
        dfs(root,p,q)
        return found

# time : O(n) worst case and space: o(n)