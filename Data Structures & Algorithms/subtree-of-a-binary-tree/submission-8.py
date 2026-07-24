# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        found = True
        if not p and not q:
            return True
        depth = 0
        def dfs(root1,root2):
            nonlocal found
            if root1 == None and root2 or root1 and root2 == None:
                found = False
                return None
            elif root1 == None and root2 == None:
                return None
            
            dfs(root1.left,root2.left)
            
            dfs(root1.right,root2.right)
            
            if root1.val != root2.val:
                found = False

     
        dfs(p,q)
        return found   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        found = False
        if not root and not subRoot:
            return True
        res = False
        def dfs(root1,root2,p):

            nonlocal found,res

            if root1 == None and root2 or root1 and root2 == None:

                return False
            elif root1 == None and root2 == None:
                return True
            

            if self.isSameTree(root1,root2):
                return True
    
            
            return dfs(root1.left,root2,p) or   dfs(root1.right,root2,p)
     
        
        return dfs(root,subRoot,subRoot)