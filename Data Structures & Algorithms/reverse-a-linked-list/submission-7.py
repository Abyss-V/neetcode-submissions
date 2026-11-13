# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last = None
        h = head
        while h != None:
            l2 = h.next
            h.next = last
            last = h
            if h.next:
                print(h.val,h.next.val)
            h = l2
            
          
        return last