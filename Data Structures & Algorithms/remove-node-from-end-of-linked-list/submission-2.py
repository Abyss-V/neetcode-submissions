# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        dump = None
        h = head
        length = 0
        while h != None:
            length += 1
            h = h.next
        h = head

        while h != None:
            if n == length:
                head = head.next
                h.next = None
                break
            elif i + 1 == length - n:
                dump = h
            elif dump:
                dump.next = h.next
                h.next = None
                dump = None
                break
            i += 1
            h = h.next
        if dump:
            return None
        return head