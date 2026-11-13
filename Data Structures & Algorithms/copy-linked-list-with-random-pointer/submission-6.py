"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        d = n = Node(str(head.val))
        h = head
        l = {}
        l[head] = n
        while head.next:
            
            n.next = Node(head.next.val)
            l[head.next] = n.next
            n = n.next
            head =  head.next
        n = d
        head = h

        while head:
            if head.random:
                n.random = l[head.random]
            else:
                n.random = None
            n = n.next
            head = head.next
        head = h
        return d
