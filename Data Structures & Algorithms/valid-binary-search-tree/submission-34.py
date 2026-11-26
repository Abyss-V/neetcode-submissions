# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        v = True
        d_left = [float("-inf"),root.val]
        d_right = [root.val,float("inf")]
        def dfs(root,d,p):
            nonlocal v
            
            if not root:
      
                return
            if not(root.val < d[1] and d[0] < root.val):
                v = False
                return
    
          
            dfs(root.left,[d[0],root.val],"left")
            dfs(root.right,[root.val,d[1]],"right")
            d.pop()
         
        
        dfs(root.left,[d_left[0],root.val],"left")
        dfs(root.right,[root.val,d_right[1]],"right")
    
        
        return v

# time:O(n); space:O(n)