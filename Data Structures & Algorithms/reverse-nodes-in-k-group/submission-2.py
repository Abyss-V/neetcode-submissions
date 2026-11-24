# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def printlinked(self,head):
        while head:
            print(head.val)
            head = head.next
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last = None
        h = head
        while h != None:
            l2 = h.next
            h.next = last
            last = h
            h = l2
            
          
        return last
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = head
        i = 0
        b = None
        h = None
        n = ListNode(next=l)
        l2 = None
        if k == 1:
            return head
        while l:
            i = 0
            
            l2 = l
            while l2 and i < k-1:
                l2 = l2.next  
                i +=1
            if k < 2:
                break
            if not l2:
                break
            temp = l2.next
            l2.next = None
         
            f = l
            # print(l.val)
            l = self.reverseList(l)
            if b:
                # print(b.val,l.val)
                b.next = l
            else:
                
                h = l2
                # print("first",h.val)
            # if temp:
            #     print(temp.val)
            
            f.next = temp
            # print("ehre")
            # self.printlinked(l)
            if not f.next:
                # self.printlinked(n.next)
                return h
            l = f.next
            b = f
            # print(l.val)
        
        return h
            