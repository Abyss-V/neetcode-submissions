# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h = l1
        h2 = l2
        l_1  = 0
        l_2 = 0
        while l1:
            l_1+=1
            l1 = l1.next
        l1 = h
        while l2:
            l_2+=1
            l2 = l2.next
        l2 = h2
        if l_1 >= l_2:
            while l1 or l2:

                if l1 and l2:
                    l1.val = l1.val+l2.val
                    if l1.val  >= 10:
                        n1 = l1.val % 10
                        n2 = l1.val // 10
                        l1.val = n1
                        if l1.next:
                            l1.next.val = l1.next.val + n2
                        else:
                            l1.next = ListNode(n2)

                    l1 = l1.next
                    l2 = l2.next
                elif l1 and not l2:

                    if l1.val >= 10:
                
                        n1 =  l1.val % 10
                        n2 = l1.val // 10
                        l1.val = n1
                
                        if l1.next:
                            l1.next.val = l1.next.val+n2
                        else:
                            l1.next = ListNode(n2)
                
                    
                    l1 = l1.next
            return h
        else:
                while l1 or l2:

                    if l1 and l2:
                        l2.val = l1.val+l2.val
                        if l2.val  >= 10:
                            n1 = l2.val % 10
                            n2 = l2.val // 10
                            l2.val = n1
                            if l2.next:
                                l2.next.val = l2.next.val + n2
                            else:
                                l2.next = ListNode(n2)

                        l1 = l1.next
                        l2 = l2.next
                    elif l2 and not l1:

                        if l2.val >= 10:
                    
                            n1 =  l2.val % 10
                            n2 = l2.val // 10
                            l2.val = n1
                    
                            if l2.next:
                                l2.next.val = l2.next.val+n2
                            else:
                                l2.next = ListNode(n2)
                    
                        
                        l2 = l2.next

        
        return h2

# time: O(m+n); space:O(1)