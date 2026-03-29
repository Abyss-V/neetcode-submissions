# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        h = head
        while h != None:
            l.append(h.val)
            h = h.next
        l = l[::-1]
        i = 0
        tmp = head
        while head != None:
            head.val = l[i]
            head = head.next
            i+=1
        head = tmp
        return head