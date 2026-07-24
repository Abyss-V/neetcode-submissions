# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        path = []
        curr_max = {}
        c = 1
        current_max = root.val
        def dfs(r):
            nonlocal c,current_max,root
            if not r:
               
                return None
    
            
            if r.val >= current_max:
               path.append(r)
               c += 1
               print("eeeeeeeeeeeeeee")
               print(current_max)
               
               print(r.val)
               current_max = r.val
               curr_max[r] = current_max
            else:
                curr_max[r] = current_max
        
        
               
            dfs(r.left)
            if r.right:
                current_max = curr_max[r]
            dfs(r.right)

            return r 
        dfs(root.left)
        current_max = root.val
        dfs(root.right)
 
        return c     

