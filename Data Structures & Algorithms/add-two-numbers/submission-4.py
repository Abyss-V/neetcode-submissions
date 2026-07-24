# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newlist = ListNode(0)
        retlist = newlist
        hold = None
        s = 0
        while l1 or l2:
            if l1 and l2:
                s = (l1.val + l2.val + hold) if hold else l1.val + l2.val
            elif l1:
                s = (l1.val + hold) if hold else l1.val
            elif l2:
                s = (l2.val + hold) if hold else l2.val
          
            if s >= 10:
                hold = s // 10
                newlist.val = s % 10
            else:   
                newlist.val = s
                hold = None
            if (l2 and l2.next) or (l1 and l1.next):
                newlist.next = ListNode(0)
                newlist = newlist.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if hold:
            newlist.next = ListNode(hold)
        return retlist

# time : o(n) , space : o(1)