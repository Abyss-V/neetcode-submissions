# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        p = []
        goods = []
        r = root
        f = True
        lastvalid = root
        def dfs(root):
            nonlocal lastvalid,goods,p
            if not root:
      
                return 
       
            if lastvalid.val <= root.val:
                goods.append(root.val)
                p.append(root)
                lastvalid = root
            
            # if not p:
            #     goods.append(root.val)

            dfs(root.left)
            
            dfs(root.right)
            if p and root.val  == p[-1].val:
                p.pop()
                if p:
                    lastvalid = p[-1]
    
        dfs(root)
       
        return len(goods)
