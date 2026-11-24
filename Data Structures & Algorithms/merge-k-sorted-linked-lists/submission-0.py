# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = []
        for i in range(len(lists)):
            n = lists[i]
            while n:
                l.append(n.val)
                n = n.next
        l.sort()
        if not l:
            return None
        h = ListNode(val=l[0])
        head = h
        for i in range(1,len(l)):
            node = ListNode(l[i])
            h.next = node
            h = node
        return head

