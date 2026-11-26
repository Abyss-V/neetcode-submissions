# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        p = [root]
        goods = []
        def dfs(root):
            nonlocal goods,p
            if not root:
      
                return 
       
            if p and p[-1].val <= root.val:
                goods.append(root.val)
                p.append(root)
            dfs(root.left)
            dfs(root.right)
            if p and root.val  == p[-1].val:
                p.pop()
         
    
        dfs(root)
       
        return len(goods)
# time:O(n); space:O(n)