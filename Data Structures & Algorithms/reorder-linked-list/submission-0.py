# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head 
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        
        current = slow.next
        slow.next = None
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        begin = head
        while prev:
            temp1 = begin.next 
            temp2 = prev.next
            begin.next = prev
            prev.next = temp1
            prev = temp2 
            begin = temp1



        