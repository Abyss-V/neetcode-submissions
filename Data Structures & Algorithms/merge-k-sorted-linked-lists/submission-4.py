# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
       
        d = node = ListNode()
       
        while list1  and list2:
            if list1.val <= list2.val:
                node.next = list1
                list1 = list1.next 
            else:
                node.next = list2
                list2 = list2.next 
            node = node.next
        node.next = list1 or list2
        return d.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        i = 0
        j = len(lists) - 1
        if not lists:
            return None
        while len(lists) > 1:
            mergedlists = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i +1 < len(lists) else None
                mergedlists.append(self.mergeTwoLists(l1,l2))

            lists = mergedlists
        return lists[0]

