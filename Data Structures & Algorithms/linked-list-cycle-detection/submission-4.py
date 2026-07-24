# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        p1 = head
        p2 = head.next
        while p2 and p2.next != None:
            if p2.next == p1:
                return True
            p2 = p2.next.next
            p1 = p1.next
        return False