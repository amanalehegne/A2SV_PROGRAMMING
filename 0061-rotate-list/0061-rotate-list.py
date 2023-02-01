# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        count = 0
        while temp:
            temp = temp.next
            count += 1
        if count == 0 or n % count == 0 or n == 0:
            return head
        n = n % count
        
        slow, fast = head, head
        for i in range(n):
            fast = fast.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            
        res = slow.next
        slow.next = None
        fast.next = head
        return res
        
