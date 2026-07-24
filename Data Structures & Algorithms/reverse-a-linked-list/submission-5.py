# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        n = None
        if not head:
            return head
        while head!=None:
            if not prev and head.next != None:
                n = head.next
                head.next = None
                prev = head
                head = n
            else:
                n = head.next
                head.next = prev
                prev = head
                head = n
                
        return prev

# time:o(n) , space : o(1)