# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSame(self,root1,root2):
        if root1 and not root2 or root2 and not root1 :
            return False

        if not root1 and not root2:
            return True
        if root1.val != root2.val:
            return False
        
        
        return self.isSame(root1.left,root2.left) and self.isSame(root1.right,root2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.isSame(root,subRoot):
            return True
        return  self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

"""
Time Complexity: O(n × m) — in the worst case, you compare the entire subRoot (size m) at each node of root (size n).
Space Complexity: O(h₁ + h₂) — recursion stacks for traversing root and comparing subRoot, where h₁ and h₂ are the heights of the two trees (worst case O(n + m), balanced O(log n + log m)).
"""