# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            if isinstance(head.val,tuple):
                return True
            head.val = (head.val,"v")
            head = head.next

        return False