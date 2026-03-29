# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def reverse(node):
#             print(node)
#             if node == None:
#                 return
#             tmp = node.right
#             node.right = node.left
#             node.left = tmp
#             reverse(node.right)
#             reverse(node.left)
#         reverse(root)
#return root
    
class Solution:
    import collections
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        q = collections.deque([root])
        while q:
            node = q.popleft()
            node.left,node.right =  node.right,node.left
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            
        return root