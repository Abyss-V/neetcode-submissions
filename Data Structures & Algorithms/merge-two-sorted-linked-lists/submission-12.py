# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        list3 = ListNode(-1)
        top = list3
        prev = None
        n = None
        while list3 and (list1 or list2):
            if not list2 or (list1 and list1.val <= list2.val):

                    list3.next = ListNode(list1.val)
                    list1 = list1.next
            elif not list1 or (list2 and list1.val > list2.val):
                    list3.next = ListNode(list2.val)
                    list2 = list2.next

            list3 = list3.next
        ret = top.next
        top.next = None
        return ret

              