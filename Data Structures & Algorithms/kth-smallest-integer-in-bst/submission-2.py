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
           
            
            r1 = dfs(root.left)
            res.append(root.val)
            # if r1:
            #     print(r1.val)
            #     res.append(r1.val)
            r2 = dfs(root.right)
            
            # if r2:
            #     res.append(r2.val)
            return root
        dfs(root)
        # res.sort()
        print(res)
        return res[k-1]