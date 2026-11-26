# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        f = None
        proot = None
        qroot = None
        search = []
        p_p = []
        p_q = [] 
        def dfs(root,p,q):
            nonlocal f,search,p_p,p_q
            if not root:
                return
            if ((root.right and root.val == p.val and root.right.val == q.val) or(root.left and root.val == p.val and root.left.val == q.val)) or ((root.left and root.val == q.val and root.left.val == p.val) or (root.right and root.val == p.val and root.right.val == p.val)):
                f = root
                return
            search.append(root)
            if root.val == p.val:
                p_p = search.copy()
          
            if root.val == q.val:
                p_q = search.copy()
            
            dfs(root.left,p,q)
            
            dfs(root.right,p,q)
            search.pop()
        dfs(root,p,q)
     
        if not f:
            if len(p_p) < len(p_q):
                for i in range(len(p_p)):
                    if p_p[i].val == p_q[i].val:
                        f = p_p[i]
            else:
                for i in range(len(p_q)):
                    if p_p[i].val == p_q[i].val:
                        f = p_q[i]
        return f
                
  