# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        m = 0
        if not root:
            return 0
        depth = 1
        def dfs(lastroot,root,depth):
            nonlocal m
            if root == None:

                return None,depth - 1
            dfs(root,root.left,depth + 1)
            dfs(root,root.right,depth + 1)
            m = max(m,depth)

            return root,depth
        dfs(root,root, 1)
        return m
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        max_levels = self.maxDepth(root)
        print(max_levels)
        levels = [0 for _ in range(max_levels)]
        def dfs(root, depth):
            if not root:
                return None
            levels[depth] = root.val
            dfs(root.left,depth + 1)
            dfs(root.right,depth + 1)
        dfs(root,0)
        return levels
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return self.levelOrder(root)
    
# time: O(n) , space: O(n)