# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        second = None
        count = 0 

        while first is not None:
            if second is not None:
                second = second.next

            if count == n:
                second = head

            first = first.next
            count += 1

    
        if second is None:
            return head.next

    
        second.next = second.next.next
        return head
            

        

        