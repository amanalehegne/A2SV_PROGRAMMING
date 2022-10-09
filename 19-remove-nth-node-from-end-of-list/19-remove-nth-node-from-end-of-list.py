# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        size = 0
        while temp:
            size += 1
            temp = temp.next
        if n < 1 or n > size:
            return head
        if n == size:
            return head.next
        prev = head
        for i in range(size - n - 1):
            prev = prev.next
        prev.next = prev.next.next
        return head