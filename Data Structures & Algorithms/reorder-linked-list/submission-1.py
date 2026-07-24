# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0 
        l = head 
        dump = ListNode()
        top = None
        h = head
        stack = []
            
        while h != None:
            if top == None:
                top = h
                h = h.next
            else:
                stack.append(h)
                h = h.next
                length += 1


        l = length // 2
        while  l and head and len(stack) > 0:
            n = stack.pop()
            tmp = head.next
            head.next = n
            n.next = tmp
            if stack:
                print(stack[-1].val)
                stack[-1].next = None
            head = n.next
            l -= 1
        
            
        # print(stack)
    

