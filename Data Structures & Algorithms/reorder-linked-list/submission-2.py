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
            h = l2
            
          
        return last
    def reorderList(self, head: Optional[ListNode]) -> None:
        h = head
        l = 0
        i = 0


        while head:
            l +=1
            head = head.next
        head = h
  
        while i <= l:
            if i == l//2:
                break 
            h = h.next
            i += 1
        first , second = head, self.reverseList(h)
        while first.next and second.next:
            tmp1 , tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first  = tmp1
            second = tmp2
            i+=1
        

