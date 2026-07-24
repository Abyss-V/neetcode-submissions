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
        newhead = Node(0)
        rethead = newhead
        h = head
        visited = {}
        if not head:
            return None
        while h:
            newhead.val = h.val
            if h.next:
                newhead.next = Node(0)

            visited[h] = newhead
            newhead = newhead.next
            h = h.next
        newhead = rethead
        while head:
            if head.random:
                
                newhead.random = visited[head.random]
            else:
                newhead.random = None
            newhead = newhead.next
            head = head.next
        return rethead
