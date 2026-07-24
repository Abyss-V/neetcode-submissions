# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        if not head:
            return None
        def dfs(h):
            nonlocal new_head
            if h.next == None:
                new_head = h
                return h

            n = dfs(h.next)
            n.next = h
            return h
        h = dfs(head)
        h.next = None
        print(new_head)
        return new_head