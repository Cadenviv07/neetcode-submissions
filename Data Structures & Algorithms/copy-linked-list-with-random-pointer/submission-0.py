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
        copy = {None:None}
        curr = head
        while curr:
            node = Node(curr.val)
            copy[curr] = node
            curr = curr.next 
        
        dummy = Node(0)
        deep = dummy 
        curr = head
        while curr:
            deep.next = copy[curr]
            random = curr.random
            deep.next.random = copy[random]
            curr = curr.next
            deep = deep.next 
        
        deep.next = None

        return dummy.next

        