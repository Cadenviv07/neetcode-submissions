# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        prev =  set()

        current = head 

        while current is not None:
            if current in prev:
                return True
            else:
                prev.add(current)
            current = current.next
        return False
        
       