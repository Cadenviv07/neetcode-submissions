# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        count = 0
        while current:
            count += 1
            current = current.next

        end = count - n

        if end == 0:
            head = head.next
            return head

        count = 0
        start = head
        while start:
            if count == end - 1:
                start.next = start.next.next
                break
            count += 1
            start = start.next
        
        return head 

        