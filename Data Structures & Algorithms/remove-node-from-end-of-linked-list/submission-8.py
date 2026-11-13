# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        h = head
        leng = 0
        while head:
            leng  += 1
            head = head.next
        head = h
        while head:
            if leng == 1 and n==leng:
                return None
            elif leng - 1 == n - 1:
                tmp = head.next
                h.next = None
                h = tmp

            if leng - l -  1 == n:
             
                head.next = head.next.next
            head = head.next
            l += 1
        return h
    

# time: O(n);space: O(1)