# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = list1
        h2 = list2
        if not list1:
            return list2
        elif not list2:
            return list1
        if list1.val <= list2.val:
            while h1.next and h2:
                if h1.val <= h2.val and h2.val <= h1.next.val:
                    d = ListNode(h2.val,h1.next)
                    h1.next = d
                    h2 = h2.next
                else:
                    h1 = h1.next
            if h2 and not h1.next:
                h1.next = h2
            return list1
        if list2.val <= list1.val:
            while h2.next and h1:
                if h2.val <= h1.val and h1.val <= h2.next.val:
                    d = ListNode(h1.val,h2.next)
                    h2.next = d
                    h1 = h1.next
                else:
                    h2 = h2.next
            if h1 and not h2.next:
                h2.next = h1
            return list2
        return list1