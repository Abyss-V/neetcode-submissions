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
        def search(root,t,r):
            if not root:
                return
            r.append(root)
            if root.val == t.val:
                return
            elif root.val > t.val:
                search(root.left,t,r)
            else:
                search(root.right,t,r)
            
        search(root,p,p_p)
        search(root,q,p_q)
    
        if len(p_p) < len(p_q):
                for i in range(len(p_p)):
                    if p_p[i].val == p_q[i].val:
                        f = p_p[i]
        else:
                for i in range(len(p_q)):
                    if p_p[i].val == p_q[i].val:
                        f = p_q[i]
        return f
                
# time: O(h+n) h is the height and n is nodes in to reach p or q nodes height is always greater so O(h) time; space:O(h+n+n+n) which is O(h) 