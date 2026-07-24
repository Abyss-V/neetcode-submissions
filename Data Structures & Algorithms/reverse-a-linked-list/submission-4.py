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
        while True:
            if not prev and head.next!=None:
                n = head.next
                head.next = None
                prev = head
                head = n
            elif head.next == None:
                n = head.next
                head.next = prev
                prev = head
                break
            else:
                n = head.next
                head.next = prev
                prev = head
                head = n
                
        return head

# time:o(n) , space : o(1)