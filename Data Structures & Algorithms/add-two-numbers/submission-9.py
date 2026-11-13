# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d = n = ListNode()
        while l1 or l2:
            if l1 and l2:
                if n.val + (l1.val + l2.val) >= 10:
                    n1 = (n.val + (l1.val+l2.val)) % 10
                    n2 = (n.val + (l1.val+l2.val)) // 10
    
                    n.val = n1
                    n.next = ListNode(n2)
                    
                    n = n.next
                else:
                    n.val = n.val + l1.val+l2.val
                    if l1.next or l2.next:
                        n.next = ListNode()
                        n = n.next
                l1 = l1.next
                l2 = l2.next
            elif l1 and not l2:
                if n.val + (l1.val) >= 10:
                    print(n.val)
                    n1 = (n.val + (l1.val)) % 10
                    print(n1)
                    n2 = (n.val + (l1.val)) // 10
                    print(n2)
              
                    n.val = n1
                    n.next = ListNode(n2)
              
                    n = n.next
                else:
                    n.val = n.val + l1.val
                    if l1.next:
                        n.next = ListNode()
                        n = n.next
                l1 = l1.next
            elif l2 and not l1:
                if n.val + (l2.val) >= 10:
                    n1 = (n.val + (l2.val)) % 10
                    n2 = (n.val + (l2.val)) // 10
              
                    n.val = n1
                    n.next = ListNode(n2)
                 
                    n = n.next
                else:
                    n.val = n.val + l2.val
                    if l2.next:
                        n.next = ListNode()
                        n = n.next
         
                l2 = l2.next
            
              
                
            

            
            
        #     while l1:
        #         n.next = ListNode()
        #         n = n.next
        #         n.val = n.val + l1.val
        #         l1 = l1.next
        # if l2:
        #     while l2:
        #         n.next = ListNode()
        #         n = n.next
        #         n.val = n.val + l2.val
        #         l2 = l2.next          
        return d